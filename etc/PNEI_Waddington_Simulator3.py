import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd

# --- SETUP ---
st.set_page_config(layout="wide", page_title="Laboratorio Topologia PNEI")

# Inizializza session_state per i parametri
if 'width' not in st.session_state:
    st.session_state.width = 1.5
if 'depth' not in st.session_state:
    st.session_state.depth = 1.5
if 'noise' not in st.session_state:
    st.session_state.noise = 0.5
if 'sim_duration' not in st.session_state:
    st.session_state.sim_duration = 1000

st.title("🧪 Modello Dinamico del Paesaggio Epigenetico PNEI")
st.markdown("""
### Stati Transitori, Non Categorie Fisse

Questo simulatore **non descrive patologie**, ma **stati accessibili a tutti** sotto determinate condizioni.

**Il Paradigma:**
- **"Neurotipico"** = Istantanea di un essere umano nelle *giuste condizioni* (riposo, supporto sociale, salute)
- **"ASD-like"** = Stato di *rigidità* che chiunque può sperimentare (burnout, ipervigilanza, trauma)
- **"ADHD-like"** = Stato di *dispersione* accessibile a tutti (privazione del sonno, sovraccarico cognitivo, stress cronico)

**L'obiettivo:** Costruire un modello *a posteriori* dell'essere umano, pragmatico e basato sulla neuroplasticità, non categorie idealistiche.

Manipola i parametri per esplorare **come il paesaggio epigenetico** cambia in risposta allo stress e alle condizioni ambientali.
""")

# --- COLONNA SINISTRA: CONTROLLI ---
with st.sidebar:
    st.markdown("### ⚡ Stati Transitori (Preset)")
    st.caption("*Accessibili a tutti sotto stress o condizioni specifiche*")
    
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        if st.button("🟢 Baseline", use_container_width=True, help="Stato di riposo, condizioni ottimali"):
            st.session_state.width = 1.5
            st.session_state.depth = 1.5
            st.session_state.noise = 0.5
            st.toast("✅ Stato: Omeostasi Bilanciata")
            st.rerun()
    
    with col_b:
        if st.button("🔵 Rigidità", use_container_width=True, help="Ipervigilanza, burnout, trauma"):
            st.session_state.width = 0.8
            st.session_state.depth = 4.0
            st.session_state.noise = 0.4
            st.toast("✅ Stato: Canalizzazione Rigida")
            st.rerun()
    
    with col_c:
        if st.button("🟡 Dispersione", use_container_width=True, help="Sovraccarico, privazione sonno, stress"):
            st.session_state.width = 3.0
            st.session_state.depth = 0.5
            st.session_state.noise = 0.8
            st.toast("✅ Stato: Instabilità Dispersiva")
            st.rerun()
    
    st.divider()
    
    st.header("1. Modella il Paesaggio")
    st.info("Questi parametri definiscono la struttura (Genetica/Apprendimento).")
    
    width = st.slider("LARGHEZZA (Tolleranza)", 0.5, 5.0, st.session_state.width, 0.1,
                      key="width_slider",
                      help="Quanto è larga la valle? Stretta = Rigida. Larga = Dispersiva.")
    
    depth = st.slider("PROFONDITÀ (Attrazione)", 0.1, 5.0, st.session_state.depth, 0.1,
                      key="depth_slider",
                      help="Quanto è ripida la discesa? Alta = Forte ritorno all'equilibrio. Bassa = Instabilità.")
    
    st.header("2. Aggiungi Stress")
    st.info("Questi parametri definiscono l'ambiente attuale.")
    
    noise = st.slider("RUMORE (Stress/Caos)", 0.0, 3.0, st.session_state.noise, 0.1,
                      key="noise_slider",
                      help="Quanto 'trema' il sistema? Rappresenta input sensoriali, ansia, eventi esterni.")
    
    sim_duration = st.slider("Durata Osservazione", 100, 2000, st.session_state.sim_duration,
                              key="duration_slider")
    
    # Aggiorna session_state con i valori correnti degli slider
    st.session_state.width = width
    st.session_state.depth = depth
    st.session_state.noise = noise
    st.session_state.sim_duration = sim_duration

# --- LOGICA MATEMATICA ---

# 1. Creiamo lo Spazio
x = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(np.linspace(-5, 5, 50), np.linspace(-5, 5, 50))

# 2. Funzione Potenziale (La forma della valle)
# U(x) = -Depth * exp(-x^2 / Width)
# Aggiungiamo x^4 per creare i "muri" esterni (limiti biologici vitali)
def potential(val, w, d):
    return -d * np.exp(-(val**2) / (2 * w**2)) + 0.02 * val**4

U_1D = potential(x, width, depth)
U_2D = potential(np.sqrt(X**2 + Y**2), width, depth)

# 3. Simulazione Dinamica (La Pallina)
traj = []
pos = 1.5 # Partiamo spostati dal centro
np.random.seed(42)

for _ in range(sim_duration):
    # Forza = Derivata negativa del potenziale (la gravità che ti spinge giù)
    # d/dx di (-A * exp(-x^2/B)) = x * (2A/B) * exp(...)
    force = -(pos * (depth / width**2)) * np.exp(-(pos**2) / (2 * width**2)) - 0.08 * pos**3
    
    # Movimento = Forza + Rumore Casuale
    displacement = force * 0.05 + noise * np.sqrt(0.05) * np.random.normal()
    pos += displacement
    traj.append(pos)

traj = np.array(traj)

# --- VISUALIZZAZIONE ---

# LAYOUT: Riga 1 (2D Cross Section + Time Series), Riga 2 (3D)
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. Vista in Sezione (Profilo 2D)")
    st.caption("Immagina di tagliare la sfera a metà. Questa è la forma della 'buca'.")
    
    fig_2d = go.Figure()
    
    # Disegna la montagna/valle
    fig_2d.add_trace(go.Scatter(x=x, y=U_1D, mode='lines', name='Paesaggio', line=dict(color='gray', width=2), fill='tozeroy'))
    
    # Disegna la pallina (posizione finale)
    final_energy = potential(traj[-1], width, depth)
    fig_2d.add_trace(go.Scatter(x=[traj[-1]], y=[final_energy], mode='markers', name='TU (Ora)', marker=dict(size=15, color='red')))
    
    # Annotazioni dinamiche
    fig_2d.add_annotation(x=0, y=min(U_1D), text="Omeostasi (Centro)", showarrow=True, arrowhead=1)
    
    fig_2d.update_layout(
        yaxis_title="Energia Potenziale (Sforzo)",
        xaxis_title="Stato (Deviazione dalla norma)",
        height=350,
        margin=dict(l=20, r=20, t=30, b=20)
    )
    st.plotly_chart(fig_2d, use_container_width=True)
    
    # Spiegazione contestuale
    if width < 1.0:
        st.warning(f"⚠️ **STATO RIGIDO**: Caratteristico di ipervigilanza post-traumatica, burnout professionale, o stati ossessivi. Le pareti ripide indicano bassa tolleranza alla deviazione.")
    elif width > 3.0:
        st.warning(f"⚠️ **STATO DISPERSIVO**: Tipico di sovraccarico cognitivo, privazione del sonno, o stress cronico. Il sistema vaga senza ancoraggio.")
    else:
        st.success(f"✅ **STATO OMEOSTASI**: Condizioni ottimali. Il sistema ha resilienza e flessibilità.")

with col2:
    st.subheader("2. Comportamento nel Tempo")
    st.caption("Dove si trova la pallina momento per momento?")
    
    df_traj = pd.DataFrame({'Tempo': range(len(traj)), 'Posizione': traj})
    
    # Coloriamo le zone di pericolo
    fig_time = go.Figure()
    fig_time.add_trace(go.Scatter(x=df_traj['Tempo'], y=df_traj['Posizione'], mode='lines', line=dict(color='blue', width=1)))
    
    # Zone di soglia
    fig_time.add_hrect(y0=-0.5, y1=0.5, fillcolor="green", opacity=0.1, line_width=0, annotation_text="Zona Comfort")
    fig_time.add_hrect(y0=2.5, y1=5, fillcolor="red", opacity=0.1, line_width=0, annotation_text="Patologia/Crani")
    fig_time.add_hrect(y0=-5, y1=-2.5, fillcolor="red", opacity=0.1, line_width=0)
    
    fig_time.update_layout(height=350, yaxis_range=[-4, 4], yaxis_title="Posizione", margin=dict(l=20, r=20, t=30, b=20))
    st.plotly_chart(fig_time, use_container_width=True)
    
    # Calcolo stabilità
    deviazione_media = np.mean(np.abs(traj))
    st.metric("Carico Allostatico (Dispersione)", f"{deviazione_media:.2f}", delta="Più basso = Omeostasi")
    
    # Interpretazione pragmatica
    if deviazione_media > 2.0:
        st.error("⚠️ Sistema fuori equilibrio - Richiede intervento (riposo, supporto, riduzione carico)")
    elif deviazione_media > 1.0:
        st.warning("⚡ Carico allostatico elevato - Attenzione a non cronicizzare")
    else:
        st.success("✅ Sistema in stato di resilienza attiva")

# VISTA 3D (Sotto)
st.subheader("3. Vista Globale 3D")
st.caption("La visione d'insieme del tuo modello sferico/topologico.")

fig_3d = go.Figure(data=[go.Surface(z=U_2D, x=X, y=Y, colorscale='Viridis', opacity=0.9)])
fig_3d.update_layout(height=500, scene=dict(zaxis=dict(range=[-5, 2])))
st.plotly_chart(fig_3d, use_container_width=True)