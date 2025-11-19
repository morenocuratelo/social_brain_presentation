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

st.title("🧪 PNEI Experimental Design: From Hypothesis to Physiological Signal")
st.markdown("""
### Transitory States, Not Fixed Categories

This simulator visualizes **human states as accessible to everyone** under specific conditions, not pathologies.

**The Paradigm:**
- **"Neurotypical"** = Snapshot of a human in optimal conditions (rest, social support, health)
- **"ASD-like"** = State of *rigidity* anyone can experience (burnout, hypervigilance, trauma)
- **"ADHD-like"** = State of *dispersion* accessible to all (sleep deprivation, cognitive overload, chronic stress)

**The Goal:** Build an *a posteriori* pragmatic model of the human being based on neuroplasticity, not idealistic categories.

This tool bridges the **Epigenetic Landscape** (The Model) with **Multi-Modal Physiological Sensors** (The Measure):
- **fNIRS** (rTPJ for Social Load, DLPFC for Executive Control, Amygdala for Emotion)
- **HRV** (Heart Rate Variability - Vagal Tone/Resilience)
- **GSR** (Galvanic Skin Response - Sympathetic Arousal/Stress)
""")

# --- LOGIC: COMPREHENSIVE PNEI OPERATIONALISATION MAP ---
def get_interaction_params(profile, condition):
    """
    Maps experimental design (Population × Environment) to Waddington parameters 
    and predicts multi-modal physiological responses.
    
    Returns: width, depth, noise, hypothesis_text, comprehensive_sensor_predictions
    
    PHILOSOPHY: Clinical groups (ASD, ADHD) are not pathological categories, 
    but accessible topological states that anyone can reach under specific conditions.
    """
    
    # 1. BASELINE DEFINITIONS (Transitory States, Not Fixed Categories)
    if profile == "Neurotypical (NT)":
        w, d, n = 1.5, 1.5, 0.4
    elif profile == "ASD-like (Rigid)":
        w, d, n = 0.6, 4.0, 0.3
    elif profile == "ADHD-like (Dispersed)":
        w, d, n = 3.0, 0.5, 0.6

    # 2. INTERACTION EFFECTS (The Experiment)
    
    if condition == "G3: Book (Control)":
        return w, d, n, "Baseline Control", {
            "fNIRS (Amygdala)": "Low (Blue)",
            "fNIRS (rTPJ - Social)": "Low (Baseline)",
            "fNIRS (DLPFC - Logic)": "Moderate (Green)",
            "HRV (Vagal Tone)": "Stable",
            "GSR (Stress)": "Low"
        }

    elif condition == "G1: Human Tutor":
        if profile == "Neurotypical (NT)":
            # Scaffolding: High DLPFC efficiency, Moderate Social
            return w, d * 1.5, n * 0.5, "Social Scaffolding", {
                "fNIRS (Amygdala)": "Moderate (Social Engagement)",
                "fNIRS (rTPJ - Social)": "Moderate (Theory of Mind Active)",
                "fNIRS (DLPFC - Logic)": "High (Boosted by Scaffolding)",
                "HRV (Vagal Tone)": "High (Co-regulation)",
                "GSR (Stress)": "Optimal Arousal"
            }
        elif profile == "ASD-like (Rigid)":
            # Social Friction: Massive rTPJ load acts as Noise
            return w, d, n + 1.5, "Social Friction (High Cost)", {
                "fNIRS (Amygdala)": "🚨 HIGH ALERT (Red - Limbic Activation)",
                "fNIRS (rTPJ - Social)": "🚨 SPIKE (Social Processing Overload)",
                "fNIRS (DLPFC - Logic)": "Low (Resource Steal Effect)",
                "HRV (Vagal Tone)": "📉 Collapsing (Vagal Withdrawal)",
                "GSR (Stress)": "📈 Spiking (Sympathetic Dominance)"
            }
        elif profile == "ADHD-like (Dispersed)":
            # External Regulation: Human supports DLPFC
            return w, d * 3.0, n, "External Regulation", {
                "fNIRS (Amygdala)": "Low (Reduced Anxiety)",
                "fNIRS (rTPJ - Social)": "Moderate (Social Anchor)",
                "fNIRS (DLPFC - Logic)": "✅ Supported (External Pacing)",
                "HRV (Vagal Tone)": "Increased (External Co-regulation)",
                "GSR (Stress)": "Moderate (Managed)"
            }

    elif condition == "G4: LLM (Active)":
        if profile == "Neurotypical (NT)":
            # Logical Depuration: Low Social, High Logic
            return w, d * 0.8, n + 0.2, "Logical Depuration", {
                "fNIRS (Amygdala)": "Low (No Social Cues)",
                "fNIRS (rTPJ - Social)": "📉 Low (Social Depuration)",
                "fNIRS (DLPFC - Logic)": "High (Utilitarian Processing)",
                "HRV (Vagal Tone)": "Baseline",
                "GSR (Stress)": "Low"
            }
        elif profile == "ASD-like (Rigid)":
            # Social Bypass: rTPJ stays quiet, DLPFC works well
            return w, d, n, "✅ Social Bypass (Low Cost)", {
                "fNIRS (Amygdala)": "✅ Low/Baseline (No Social Friction)",
                "fNIRS (rTPJ - Social)": "✅ Low (Energy Conservation)",
                "fNIRS (DLPFC - Logic)": "📈 High (Resources Freed for Task)",
                "HRV (Vagal Tone)": "Stable (Safety Signal)",
                "GSR (Stress)": "Low"
            }
        elif profile == "ADHD-like (Dispersed)":
            # Burnout: High DLPFC demand without support -> Fatigue
            return w, d, n + 1.0, "⚠️ Executive Burnout (Constructivist Overload)", {
                "fNIRS (Amygdala)": "Rising (Frustration/Anxiety)",
                "fNIRS (rTPJ - Social)": "Phantom Activation (Seeking Support)",
                "fNIRS (DLPFC - Logic)": "📉 Fading (Metabolic Fatigue)",
                "HRV (Vagal Tone)": "📉 Dropping Fast (Exhaustion)",
                "GSR (Stress)": "High (Sustained Effort)"
            }
            
    return w, d, n, "Undef", {}

# --- SIDEBAR ---
with st.sidebar:
    st.header("1. Design Matrix")
    sel_profile = st.selectbox("Population", ["Neurotypical (NT)", "ASD-like (Rigid)", "ADHD-like (Dispersed)"])
    sel_condition = st.selectbox("Environment", ["G3: Book (Control)", "G1: Human Tutor", "G4: LLM (Active)"])
    
    c_w, c_d, c_n, hyp_text, sensor_data = get_interaction_params(sel_profile, sel_condition)
    
    st.divider()
    st.subheader("2. Expected Multi-Modal Signals")
    st.info("Comprehensive PNEI Validation: How we operationalize the model")
    
    # Comprehensive Dashboard
    st.markdown("**🧠 fNIRS (Brain Hemodynamics)**")
    col_f1, col_f2, col_f3 = st.columns(3)
    col_f1.metric("Amygdala (Emo)", sensor_data.get("fNIRS (Amygdala)", "-"))
    col_f2.metric("rTPJ (Social)", sensor_data.get("fNIRS (rTPJ - Social)", "-"))
    col_f3.metric("DLPFC (Exec)", sensor_data.get("fNIRS (DLPFC - Logic)", "-"))
    
    st.markdown("**❤️ Autonomic System**")
    col_a1, col_a2 = st.columns(2)
    col_a1.metric("HRV (Vagal)", sensor_data.get("HRV (Vagal Tone)", "-"))
    col_a2.metric("GSR (Stress)", sensor_data.get("GSR (Stress)", "-"))
    
    st.metric("🔬 Interpretation", hyp_text)
    
    st.divider()
    st.caption("Waddington Landscape Parameters (PNEI Operationalization)")
    width = st.slider("Width (Rigidity/Flexibility)", 0.5, 5.0, float(c_w), 0.1, disabled=True)
    depth = st.slider("Depth (Resilience/HRV Proxy)", 0.1, 6.0, float(c_d), 0.1, disabled=True)
    noise = st.slider("Noise (Allostatic Load/Stress)", 0.0, 3.0, float(c_n), 0.1, disabled=True)
    sim_duration = st.slider("Simulation Time", 100, 2000, 1000)

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
    st.subheader("🏞️ The Waddington Landscape (Mechanism)")
    fig_2d = go.Figure()
    fig_2d.add_trace(go.Scatter(x=x, y=U_1D, mode='lines', name='Landscape', line=dict(color='gray', width=2), fill='tozeroy'))
    final_energy = potential(traj[-1], width, depth)
    fig_2d.add_trace(go.Scatter(x=[traj[-1]], y=[final_energy], mode='markers', name='State', marker=dict(size=15, color='#ef4444')))
    
    fig_2d.add_annotation(x=0, y=min(U_1D), text=f"Depth → HRV Resilience", showarrow=True, arrowhead=2, ay=40)
    
    fig_2d.update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20), showlegend=False, yaxis_title="Potential U(x)")
    st.plotly_chart(fig_2d, use_container_width=True)

with col2:
    st.subheader("📊 State Trajectory Over Time (The Signal)")
    df_traj = pd.DataFrame({'Time': range(len(traj)), 'Position': traj})
    fig_time = go.Figure()
    fig_time.add_trace(go.Scatter(x=df_traj['Time'], y=df_traj['Position'], mode='lines', line=dict(color='#3b82f6', width=1)))
    
    # Thresholds mapped to PNEI measures
    fig_time.add_hrect(y0=-0.5, y1=0.5, fillcolor="green", opacity=0.1, line_width=0, annotation_text="High HRV Zone (Homeostasis)")
    fig_time.add_hrect(y0=2.5, y1=5, fillcolor="red", opacity=0.1, line_width=0, annotation_text="GSR Spike Zone (Sympathetic Arousal)")
    fig_time.add_hrect(y0=-5, y1=-2.5, fillcolor="red", opacity=0.1, line_width=0, annotation_text="Withdrawal/Dissociation")
    
    fig_time.update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20), yaxis_range=[-4, 4], yaxis_title="State Deviation x(t)")
    st.plotly_chart(fig_time, use_container_width=True)

# --- COMPREHENSIVE PNEI EXPLANATION ---
st.divider()
st.markdown("### 🔬 PNEI Operationalization: Bridging Physics and Physiology")

st.markdown("""
This table explicates how **abstract landscape parameters** map to **concrete physiological measurements**, 
enabling empirical validation of the Waddington model through multi-modal sensors.

| Landscape Parameter | Physiological Measure | Interpretation | Neural/Peripheral System |
|---------------------|----------------------|----------------|-------------------------|
| **Depth ($k$)** | **HRV (RMSSD)** | High Depth = High HRV (Strong Vagal Tone). The ability to self-regulate and return to baseline after perturbation. Deep valleys = high resilience. | **Autonomic NS** (Parasympathetic) |
| **Noise ($\\xi$)** | **GSR / fNIRS (Amygdala)** | High Noise = Sympathetic Arousal / Limbic reactivity. The "friction" of the environment. Represents unprocessed stress or social load. | **Autonomic NS** (Sympathetic) + **Limbic System** |
| **Width ($\\sigma$)** | **Behavioral Rigidity / Flexibility** | Narrow = Channelized (repetitive behaviors, hyper-focus). Wide = Dispersed (distractibility). Measured via task switching or stereotypy scales. | **Executive Function** (DLPFC) |
| **rTPJ Activation** | **Social Load (fNIRS)** | Right Temporo-Parietal Junction mediates Theory of Mind and social cognition. Overload (e.g., ASD + Human) increases noise, destabilizing trajectory. | **Social Brain Network** |
| **DLPFC Activation** | **Executive Support (fNIRS)** | Dorsolateral Prefrontal Cortex manages executive control. Scaffolding (e.g., Human Tutor) "deepens the valley", enhancing stability and focus. | **Executive Network** |
""")

st.divider()
st.markdown("""
### 🎯 Key Insight: Clinical Groups as System Limits

**Why study ASD and ADHD alongside neurotypicals?**

In a PNEI state-space model, the neurotypical population occupies the **central attractor basin** (homeostasis). 
However, to understand **resilience mechanisms** and **system breaking points** (allostasis → allostatic overload), 
we must observe the **outliers** represented by clinical groups.

They are not "errors" of the model, but **explorers of the boundaries**. 
Studying a depressed brain or hyperactive immune system reveals the **mechanical rules** governing health itself—rules that remain silent when the system is in equilibrium.

**The Paradigm:** Under extreme stress, bereavement, inflammation, or sleep deprivation, 
a "statistically normal" brain can transition into rigid (ASD-like) or labile (ADHD-like) topologies. 
**Clinical groups show us the landscape's limits that everyone can reach under certain conditions.**
""")
