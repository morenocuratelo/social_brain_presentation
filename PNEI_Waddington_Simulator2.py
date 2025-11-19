import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(layout="wide", page_title="Simulatore PNEI: Modello Pragmatico Universale")

# --- TITOLO E FILOSOFIA ---
st.title("🏔️ Modello PNEI Universale: Lo Spazio degli Stati")
st.markdown("""
### Dal "Patologico" al "Dimensionale"
Questo simulatore non classifica le persone in "sane" o "malate". 
Assume invece un **Modello Pragmatico dell'Essere Umano**: ogni individuo possiede lo stesso macchinario biologico che, **sottoposto a diverse condizioni** (genetiche, ambientali, stress), assume configurazioni topologiche differenti.

* **L'Ipotesi:** Le condizioni cliniche (ASD, ADHD) non sono "errori", ma **modalità di funzionamento** del sistema umano portate ai loro limiti asintotici. 
* **L'Universalità:** Sotto stress estremo, lutto o infiammazione, un cervello "statisticamente normale" può transire in una topologia rigida (simil-ASD) o labile (simil-ADHD).
""")

# --- SIDEBAR: CONTROLLI CONTESTUALI ---
st.sidebar.header("1. Configurazione della Topologia")

# Ridenominazione semantica: Dalla Diagnosi allo Stato
state_preset = st.sidebar.selectbox(
    "Seleziona lo Stato del Sistema (Snapshot)",
    (
        "Stato Basale (Equilibrio/Neurotipico)", 
        "Stato Iper-Rigido (Pattern ASD o Stress Cronico)", 
        "Stato Iper-Labile (Pattern ADHD o Esaurimento)", 
        "Transizione Critica (Punto di Rottura)"
    )
)

# Logica dei parametri basata sullo STATO, non sulla PERSONA
if state_preset == "Stato Basale (Equilibrio/Neurotipico)":
    def_depth = 1.5
    def_width = 1.5
    def_noise = 0.5
    desc = "Il sistema è flessibile ma stabile. Rappresenta l'omeostasi ideale o statistica."
elif state_preset == "Stato Iper-Rigido (Pattern ASD o Stress Cronico)":
    def_depth = 4.5
    def_width = 0.6
    def_noise = 0.4
    desc = "Il sistema è profondamente canalizzato. Utile per focus intenso, ma resistente al cambiamento. Rappresenta tratti ASD o meccanismi di difesa rigidi."
elif state_preset == "Stato Iper-Labile (Pattern ADHD o Esaurimento)":
    def_depth = 0.4
    def_width = 3.5
    def_noise = 0.9
    desc = "Il paesaggio è appiattito. Bassa capacità di trattenere lo stato (attenzione). Rappresenta tratti ADHD o stanchezza metabolica acuta."
elif state_preset == "Transizione Critica (Punto di Rottura)":
    def_depth = 0.8
    def_width = 2.0
    def_noise = 1.8 # Rumore altissimo
    desc = "Il sistema è sotto un carico allostatico (rumore) talmente alto che la topologia non riesce più a contenerlo."

st.sidebar.info(f"**Interpretazione:** {desc}")

# Sliders per manipolazione fine
st.sidebar.subheader("Parametri del Paesaggio $U(x)$")
depth = st.sidebar.slider("Profondità (Resilienza/Attrazione)", 0.1, 5.0, float(def_depth), 0.1)
width = st.sidebar.slider("Larghezza (Flessibilità)", 0.5, 4.0, float(def_width), 0.1)

st.sidebar.subheader("Condizioni Esterne")
noise_level = st.sidebar.slider("Carico Allostatico (Rumore/Stress)", 0.0, 3.0, float(def_noise), 0.1, help="Rappresenta eventi esterni: lutto, malattia, input sensoriale eccessivo.")
steps = st.sidebar.slider("Durata Simulazione", 100, 1000, 600, 50)

# --- CALCOLO MATEMATICO (Langevin Dinamica) ---

x_range = np.linspace(-4, 4, 60)
y_range = np.linspace(-4, 4, 60)
X, Y = np.meshgrid(x_range, y_range)

# Potenziale: U(x) = -Depth * exp(...) + Muri
U = -depth * np.exp(-(X**2 + Y**2) / (2 * width**2))
Boundary = 0.02 * (X**4 + Y**4) # Muri morbidi
U_total = U + Boundary

dt = 0.05
# Punto di partenza: Sempre leggermente fuori centro per vedere se torna
traj_x = [1.5] 
traj_y = [1.5] 

current_x = traj_x[0]
current_y = traj_y[0]

np.random.seed(42) 

for _ in range(steps):
    # Calcolo forze
    dist_sq = current_x**2 + current_y**2
    exp_factor = np.exp(-dist_sq / (2 * width**2))
    
    # Gradiente della buca (forza di richiamo)
    # Nota: stiamo minimizzando U, quindi andiamo opposti al gradiente
    grad_U_x = (current_x * depth / width**2) * exp_factor - 0.08 * current_x**3
    grad_U_y = (current_y * depth / width**2) * exp_factor - 0.08 * current_y**3
    
    # Forza = -Gradiente
    force_x = -grad_U_x
    force_y = -grad_U_y # Errore nel codice precedente corretto qui logicamente (segno meno) ma l'implementazione precedente simulava bene visivamente
    
    # Correzione segno per la simulazione visiva corretta verso il centro (che è minimo negativo)
    # Se U è negativo al centro, il gradiente punta FUORI. Quindi -Gradiente punta DENTRO.
    # La formula sopra: (x * depth...) è positiva per x positivi. Quindi il gradiente spinge fuori.
    # Noi vogliamo scendere, quindi andiamo contro il gradiente: - (positivo) = verso il centro.
    # Corretto.
    
    # Equazione Langevin
    dx = - (current_x * depth / width**2) * exp_factor * dt + noise_level * np.sqrt(dt) * np.random.normal()
    dy = - (current_y * depth / width**2) * exp_factor * dt + noise_level * np.sqrt(dt) * np.random.normal()
    
    current_x += dx
    current_y += dy
    
    traj_x.append(current_x)
    traj_y.append(current_y)

# --- VISUALIZZAZIONE ---

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Il Paesaggio Epigenetico (Stato Attuale)")
    
    fig = go.Figure(data=[go.Surface(z=U_total, x=X, y=Y, colorscale='Cividis', opacity=0.8)])
    
    # Calcolo Z traiettoria per visualizzazione
    traj_arr_x = np.array(traj_x)
    traj_arr_y = np.array(traj_y)
    traj_z = -depth * np.exp(-(traj_arr_x**2 + traj_arr_y**2) / (2 * width**2)) + 0.02 * (traj_arr_x**4 + traj_arr_y**4)
    
    fig.add_trace(go.Scatter3d(
        x=traj_x, y=traj_y, z=traj_z + 0.2,
        mode='lines',
        line=dict(color='white', width=3),
        name='Evoluzione Stato'
    ))
    
    # Punto finale
    fig.add_trace(go.Scatter3d(
        x=[traj_x[-1]], y=[traj_y[-1]], z=[traj_z[-1] + 0.2],
        mode='markers',
        marker=dict(size=6, color='red'),
        name='Stato Finale'
    ))

    fig.update_layout(
        scene=dict(xaxis_title='Struttura', yaxis_title='Funzione', zaxis_title='Energia Potenziale'),
        height=600,
        margin=dict(l=0, r=0, b=0, t=0)
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Analisi Pragmatica")
    
    st.markdown(f"""
    **Topologia:** `{state_preset}`
    
    In questo modello, non stiamo osservando un "Autistico" o un "Neurotipico". Stiamo osservando un sistema umano universale configurato con:
    * **Canalizzazione (Rigidità):** {1/width:.2f} (Alta = Valli strette)
    * **Profondità (Resilienza):** {depth}
    """)
    
    dist_data = np.sqrt(np.array(traj_x)**2 + np.array(traj_y)**2)
    
    # Grafico a linee semplice
    st.line_chart(pd.DataFrame(dist_data, columns=["Distanza dall'Equilibrio"]))
    
    avg_dist = np.mean(dist_data[-100:])
    
    st.markdown("### Diagnosi A Posteriori")
    if avg_dist < 0.5:
        st.success("Il sistema ha mantenuto l'omeostasi (Comportamento Adattivo).")
    elif avg_dist < 1.5:
        st.warning("Il sistema è in stato di allostasi (Stress Compensato).")
    else:
        st.error("Il sistema è entrato in uno stato disfunzionale/caotico.")
        
    st.markdown("""
    ---
    **Messaggio Chiave:**
    Se prendiamo un soggetto "Normale" e aumentiamo il **Carico Allostatico (Slider Rumore)** a livelli estremi, il suo tracciato diventerà indistinguibile da quello di un profilo clinico. 
    
    *La patologia non è una classe diversa di esseri umani, è lo stesso sistema umano sotto condizioni limite.*
    """)