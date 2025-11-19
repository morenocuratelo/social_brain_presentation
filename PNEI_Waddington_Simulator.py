import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd

# --- SETUP ---
st.set_page_config(layout="wide", page_title="Laboratorio Topologia PNEI")

if 'width' not in st.session_state: st.session_state.width = 1.5
if 'depth' not in st.session_state: st.session_state.depth = 1.5
if 'noise' not in st.session_state: st.session_state.noise = 0.5
if 'sim_duration' not in st.session_state: st.session_state.sim_duration = 1000

st.title("🧪 Experimental Design: From Hypothesis to Signal")
st.markdown("""
This tool bridges the gap between the **Epigenetic Landscape** (The Model) and the **Physiological Sensors** (The Measure).
It demonstrates how we operationalise abstract states into concrete **fNIRS** and **HRV** signals.
""")

# --- LOGIC: OPERATIONALISATION MAP ---
def get_interaction_params(profile, condition):
    # Returns: width, depth, noise, hypothesis_text, sensor_prediction
    
    # 1. BASELINE DEFINITIONS
    if profile == "Neurotypical (NT)":
        w, d, n = 1.5, 1.5, 0.4
        physio = "Baseline HRV, Balanced DLPFC activation."
    elif profile == "ASD-like (Rigid)":
        w, d, n = 0.6, 4.0, 0.3
        physio = "High HRV (Rigid Reg.), Low Noise (if isolated)."
    elif profile == "ADHD-like (Dispersed)":
        w, d, n = 3.0, 0.5, 0.6
        physio = "Variable HRV, Low DLPFC sustain."

    # 2. INTERACTION EFFECTS (The Experiment)
    
    if condition == "G3: Book (Control)":
        return w, d, n, "Baseline Control", {
            "fNIRS (Amygdala)": "Low (Blue)",
            "fNIRS (DLPFC)": "Moderate (Green)",
            "HRV (Vagal Tone)": "Stable",
            "GSR (Stress)": "Low"
        }

    elif condition == "G1: Human Tutor":
        if profile == "Neurotypical (NT)":
            return w, d * 1.5, n * 0.5, "Social Scaffolding", {
                "fNIRS (Amygdala)": "Moderate (Social engagement)",
                "fNIRS (DLPFC)": "High (Boosted by scaffolding)",
                "HRV (Vagal Tone)": "High (Co-regulation)",
                "GSR (Stress)": "Optimal Arousal"
            }
        elif profile == "ASD-like (Rigid)":
            # High Social Cost
            return w, d, n + 1.5, "Social Friction (High Cost)", {
                "fNIRS (Amygdala)": "🚨 HIGH ALERT (Red)",
                "fNIRS (DLPFC)": "Low (Steal effect)",
                "HRV (Vagal Tone)": "📉 Collapsing (Vagal Withdrawal)",
                "GSR (Stress)": "📈 Spiking"
            }
        elif profile == "ADHD-like (Dispersed)":
            # External Regulation
            return w, d * 3.0, n, "External Regulation", {
                "fNIRS (Amygdala)": "Low",
                "fNIRS (DLPFC)": "High (Supported)",
                "HRV (Vagal Tone)": "Increased (External Pacing)",
                "GSR (Stress)": "Moderate"
            }

    elif condition == "G4: LLM (Active)":
        if profile == "Neurotypical (NT)":
            return w, d * 0.8, n + 0.2, "Neutral / Low Social", {
                "fNIRS (Amygdala)": "Low (No social cues)",
                "fNIRS (DLPFC)": "Moderate",
                "HRV (Vagal Tone)": "Baseline",
                "GSR (Stress)": "Low"
            }
        elif profile == "ASD-like (Rigid)":
            # Social Bypass
            return w, d, n, "✅ Social Bypass (Low Cost)", {
                "fNIRS (Amygdala)": "✅ Low/Baseline (No friction)",
                "fNIRS (DLPFC)": "📈 High (Resources freed)",
                "HRV (Vagal Tone)": "Stable (Safety)",
                "GSR (Stress)": "Low"
            }
        elif profile == "ADHD-like (Dispersed)":
            # Constructivist Burnout
            return w, d, n + 1.0, "⚠️ Constructivist Burnout", {
                "fNIRS (Amygdala)": "Rising (Frustration)",
                "fNIRS (DLPFC)": "📉 Fading (Fatigue)",
                "HRV (Vagal Tone)": "📉 Dropping fast",
                "GSR (Stress)": "High (Effort)"
            }
            
    return w, d, n, "Undef", {}

# --- SIDEBAR ---
with st.sidebar:
    st.header("1. Design Matrix")
    sel_profile = st.selectbox("Population", ["Neurotypical (NT)", "ASD-like (Rigid)", "ADHD-like (Dispersed)"])
    sel_condition = st.selectbox("Environment", ["G3: Book (Control)", "G1: Human Tutor", "G4: LLM (Active)"])
    
    c_w, c_d, c_n, hyp_text, sensor_data = get_interaction_params(sel_profile, sel_condition)
    
    st.divider()
    st.subheader("2. Expected Signal (The Measure)")
    st.info("How we validate the model via sensors:")
    
    # Simulated Dashboard
    col_s1, col_s2 = st.columns(2)
    col_s1.metric("fNIRS (Emo)", sensor_data.get("fNIRS (Amygdala)", "-"))
    col_s2.metric("HRV (Reg)", sensor_data.get("HRV (Vagal Tone)", "-"))
    st.metric("Interpretation", hyp_text)
    
    st.divider()
    st.caption("Model Parameters (Operationalised)")
    width = st.slider("Width", 0.5, 5.0, float(c_w), 0.1, disabled=True)
    depth = st.slider("Depth (HRV proxy)", 0.1, 6.0, float(c_d), 0.1, disabled=True)
    noise = st.slider("Noise (GSR proxy)", 0.0, 3.0, float(c_n), 0.1, disabled=True)
    sim_duration = st.slider("Time", 100, 2000, 1000)

# --- PHYSICS ---
x = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(np.linspace(-5, 5, 50), np.linspace(-5, 5, 50))

def potential(val, w, d):
    return -d * np.exp(-(val**2) / (2 * w**2)) + 0.02 * val**4

U_1D = potential(x, width, depth)
traj = []
pos = 1.5 
np.random.seed(42)

for _ in range(sim_duration):
    force = -(pos * (depth / width**2)) * np.exp(-(pos**2) / (2 * width**2)) - 0.08 * pos**3
    displacement = force * 0.05 + noise * np.sqrt(0.05) * np.random.normal()
    pos += displacement
    traj.append(pos)
traj = np.array(traj)

# --- VISUALISATION ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Mechanism (The Landscape)")
    fig_2d = go.Figure()
    fig_2d.add_trace(go.Scatter(x=x, y=U_1D, mode='lines', name='Landscape', line=dict(color='gray', width=2), fill='tozeroy'))
    final_energy = potential(traj[-1], width, depth)
    fig_2d.add_trace(go.Scatter(x=[traj[-1]], y=[final_energy], mode='markers', name='State', marker=dict(size=15, color='#ef4444')))
    
    # Annotations for measures
    fig_2d.add_annotation(x=0, y=min(U_1D), text=f"Depth = HRV Resilience", showarrow=True, arrowhead=2, ay=40)
    
    fig_2d.update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20), showlegend=False, yaxis_title="Potential U(x)")
    st.plotly_chart(fig_2d, use_container_width=True)

with col2:
    st.subheader("Outcome (The Signal)")
    df_traj = pd.DataFrame({'Time': range(len(traj)), 'Position': traj})
    fig_time = go.Figure()
    fig_time.add_trace(go.Scatter(x=df_traj['Time'], y=df_traj['Position'], mode='lines', line=dict(color='#3b82f6', width=1)))
    
    # Thresholds mapped to measures
    fig_time.add_hrect(y0=-0.5, y1=0.5, fillcolor="green", opacity=0.1, line_width=0, annotation_text="High HRV Zone")
    fig_time.add_hrect(y0=2.5, y1=5, fillcolor="red", opacity=0.1, line_width=0, annotation_text="GSR Spike Zone")
    fig_time.add_hrect(y0=-5, y1=-2.5, fillcolor="red", opacity=0.1, line_width=0)
    
    fig_time.update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20), yaxis_range=[-4, 4], yaxis_title="State Deviation x(t)")
    st.plotly_chart(fig_time, use_container_width=True)

# --- EXPLANATION ---
st.divider()
st.markdown("### 🔬 Operationalisation Table")
st.markdown("""
| Landscape Parameter | Physiological Measure (The Tool) | Interpretation |
|---------------------|----------------------------------|----------------|
| **Depth ($k$)** | **HRV (RMSSD)** | High Depth = High HRV (Strong Vagal Tone). The ability to self-regulate and return to baseline. |
| **Noise ($\zeta$)** | **GSR / fNIRS (Amygdala)** | High Noise = Sympathetic Arousal / Emotional reactivity. The "friction" of the environment. |
| **Width ($\sigma$)** | **Behavioral Rigidity** | Narrow = Repetitive behaviours or hyper-focus. Wide = Distractibility. |
""")