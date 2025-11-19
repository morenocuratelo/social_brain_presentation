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

st.title("🧪 Experimental Design: fNIRS Specifics")
st.markdown("""
This tool maps the **Experimental Variables** to the **Waddington Landscape**, with a specific focus on **fNIRS signals**.
We distinguish between **Social Load (rTPJ)** and **Executive Effort (DLPFC)**.
""")

# --- LOGIC: OPERATIONALISATION MAP ---
def get_interaction_params(profile, condition):
    # Returns: width, depth, noise, hypothesis_text, sensor_prediction
    
    # 1. BASELINE DEFINITIONS
    if profile == "Neurotypical (NT)":
        w, d, n = 1.5, 1.5, 0.4
    elif profile == "ASD-like (Rigid)":
        w, d, n = 0.6, 4.0, 0.3
    elif profile == "ADHD-like (Dispersed)":
        w, d, n = 3.0, 0.5, 0.6

    # 2. INTERACTION EFFECTS (The Experiment)
    
    if condition == "G3: Book (Control)":
        return w, d, n, "Baseline Control", {
            "fNIRS (rTPJ - Social)": "Low (Baseline)",
            "fNIRS (DLPFC - Logic)": "Moderate",
            "HRV (Stress)": "Stable"
        }

    elif condition == "G1: Human Tutor":
        if profile == "Neurotypical (NT)":
            # Scaffolding: High DLPFC efficiency, Moderate Social
            return w, d * 1.5, n * 0.5, "Social Scaffolding", {
                "fNIRS (rTPJ - Social)": "Moderate (Engaged)",
                "fNIRS (DLPFC - Logic)": "High (Efficient)",
                "HRV (Stress)": "High (Good Tone)"
            }
        elif profile == "ASD-like (Rigid)":
            # Social Friction: Massive rTPJ load acts as Noise
            return w, d, n + 1.5, "Social Friction (High Cost)", {
                "fNIRS (rTPJ - Social)": "🚨 SPIKE (Overload)",
                "fNIRS (DLPFC - Logic)": "Low (Resource Steal)",
                "HRV (Stress)": "📉 Low (Distress)"
            }
        elif profile == "ADHD-like (Dispersed)":
            # External Regulation: Human supports DLPFC
            return w, d * 3.0, n, "External Regulation", {
                "fNIRS (rTPJ - Social)": "Moderate",
                "fNIRS (DLPFC - Logic)": "✅ Supported (Focus)",
                "HRV (Stress)": "Stable"
            }

    elif condition == "G4: LLM (Active)":
        if profile == "Neurotypical (NT)":
            # Logical Depuration: Low Social, High Logic
            return w, d * 0.8, n + 0.2, "Logical Depuration", {
                "fNIRS (rTPJ - Social)": "📉 Low (Depurated)",
                "fNIRS (DLPFC - Logic)": "High (Utilitarian)",
                "HRV (Stress)": "Baseline"
            }
        elif profile == "ASD-like (Rigid)":
            # Social Bypass: rTPJ stays quiet, DLPFC works well
            return w, d, n, "✅ Social Bypass", {
                "fNIRS (rTPJ - Social)": "✅ Low (Saved Energy)",
                "fNIRS (DLPFC - Logic)": "📈 High (Task Focus)",
                "HRV (Stress)": "Stable"
            }
        elif profile == "ADHD-like (Dispersed)":
            # Burnout: High DLPFC demand without support -> Fatigue
            return w, d, n + 1.0, "⚠️ Executive Burnout", {
                "fNIRS (rTPJ - Social)": "Phantom Activation",
                "fNIRS (DLPFC - Logic)": "📉 Fading (Fatigue)",
                "HRV (Stress)": "Dropping"
            }
            
    return w, d, n, "Undef", {}

# --- SIDEBAR ---
with st.sidebar:
    st.header("1. Design Matrix")
    sel_profile = st.selectbox("Population", ["Neurotypical (NT)", "ASD-like (Rigid)", "ADHD-like (Dispersed)"])
    sel_condition = st.selectbox("Environment", ["G3: Book (Control)", "G1: Human Tutor", "G4: LLM (Active)"])
    
    c_w, c_d, c_n, hyp_text, sensor_data = get_interaction_params(sel_profile, sel_condition)
    
    st.divider()
    st.subheader("2. Expected fNIRS Signal")
    st.info("Predicted Hemodynamic Response (HbO)")
    
    # Simulated Dashboard
    col_s1, col_s2 = st.columns(2)
    col_s1.metric("rTPJ (Social)", sensor_data.get("fNIRS (rTPJ - Social)", "-"))
    col_s2.metric("DLPFC (Exec)", sensor_data.get("fNIRS (DLPFC - Logic)", "-"))
    
    st.metric("Interpretation", hyp_text)
    
    st.divider()
    st.caption("Waddington Parameters")
    width = st.slider("Width", 0.5, 5.0, float(c_w), 0.1, disabled=True)
    depth = st.slider("Depth (Scaffolding)", 0.1, 6.0, float(c_d), 0.1, disabled=True)
    noise = st.slider("Noise (Social Load)", 0.0, 3.0, float(c_n), 0.1, disabled=True)
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
    st.subheader("The Landscape (DLPFC Scaffolding)")
    fig_2d = go.Figure()
    fig_2d.add_trace(go.Scatter(x=x, y=U_1D, mode='lines', name='Landscape', line=dict(color='gray', width=2), fill='tozeroy'))
    final_energy = potential(traj[-1], width, depth)
    fig_2d.add_trace(go.Scatter(x=[traj[-1]], y=[final_energy], mode='markers', name='State', marker=dict(size=15, color='#ef4444')))
    
    fig_2d.add_annotation(x=0, y=min(U_1D), text=f"Depth = Executive Support", showarrow=True, arrowhead=2, ay=40)
    
    fig_2d.update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20), showlegend=False, yaxis_title="Potential U(x)")
    st.plotly_chart(fig_2d, use_container_width=True)

with col2:
    st.subheader("The Trajectory (rTPJ Noise)")
    df_traj = pd.DataFrame({'Time': range(len(traj)), 'Position': traj})
    fig_time = go.Figure()
    fig_time.add_trace(go.Scatter(x=df_traj['Time'], y=df_traj['Position'], mode='lines', line=dict(color='#3b82f6', width=1)))
    
    # Thresholds
    fig_time.add_hrect(y0=-0.5, y1=0.5, fillcolor="green", opacity=0.1, line_width=0, annotation_text="Cognitive Flow")
    fig_time.add_hrect(y0=2.5, y1=5, fillcolor="red", opacity=0.1, line_width=0, annotation_text="Social Overload")
    fig_time.add_hrect(y0=-5, y1=-2.5, fillcolor="red", opacity=0.1, line_width=0)
    
    fig_time.update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20), yaxis_range=[-4, 4], yaxis_title="State Deviation x(t)")
    st.plotly_chart(fig_time, use_container_width=True)

# --- EXPLANATION ---
st.divider()
st.markdown("### 🧠 fNIRS Operationalisation")
st.markdown("""
| fNIRS Channel | Waddington Parameter | Why? |
|---------------|----------------------|------|
| **rTPJ (Right Temporo-Parietal Junction)** | **Noise ($\zeta$)** | L'rTPJ gestisce la "Teoria della Mente" e il calcolo sociale. Se sovraccarica (es. ASD + Umano), introduce "rumore" nel sistema, rendendo la traiettoria instabile. |
| **DLPFC (Dorsolateral Prefrontal Cortex)** | **Depth ($k$)** | La DLPFC gestisce il controllo esecutivo. Un ambiente che supporta la DLPFC (es. Human Scaffolding) "scava" la valle, rendendo lo stato più stabile e resiliente. |
""")