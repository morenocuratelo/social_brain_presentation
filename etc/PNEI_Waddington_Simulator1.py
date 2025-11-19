import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(layout="wide", page_title="Simulatore Paesaggio Epigenetico PNEI")

# --- TITOLO E INTRODUZIONE ---
st.title("🏔️ Modello Dinamico del Paesaggio Epigenetico (PNEI)")
st.markdown("""
Questo simulatore visualizza lo stato di una persona come una particella in un **Paesaggio di Waddington**.
L'evoluzione temporale segue l'equazione differenziale stocastica (Langevin):

$$ \\frac{dx}{dt} = -\\nabla U(x) + \\xi(t) $$

Dove:
* **$U(x)$ (Potenziale):** La forma del paesaggio (Genetica/Ontogenesi).
* **$-\\nabla U(x)$ (Forza deterministica):** La tendenza a tornare all'omeostasi.
* **$\\xi(t)$ (Rumore):** Fluttuazioni stocastiche (Stress, Ambiente).
""")

# --- SIDEBAR: CONTROLLI ---
st.sidebar.header("1. Configurazione Clinica (Topografia)")

# Preset per i profili
profile = st.sidebar.selectbox(
    "Seleziona Neuroprofilo",
    ("Neurotipico (Bilanciato)", "ASD (Iper-Canalizzato/Rigido)", "ADHD (Instabile/Piatto)", "Personalizzato")
)

# Valori di default basati sulla selezione
if profile == "Neurotipico (Bilanciato)":
    def_depth = 1.5  # Profondità media
    def_width = 1.5  # Larghezza media
    def_noise = 0.5  # Rumore standard
elif profile == "ASD (Iper-Canalizzato/Rigido)":
    def_depth = 4.0  # Molto profondo (attrazione forte)
    def_width = 0.8  # Molto stretto (canalizzato)
    def_noise = 0.4  # Rumore percepito (o rigidità al rumore)
elif profile == "ADHD (Instabile/Piatto)":
    def_depth = 0.5  # Molto piatto (bassa attrazione)
    def_width = 3.0  # Molto largo (dispersivo)
    def_noise = 0.8  # Alta suscettibilità alla distrazione
else:
    def_depth = 1.5
    def_width = 1.5
    def_noise = 0.5

# Sliders per manipolazione fine (L'equazione del potenziale)
st.sidebar.subheader("Parametri del Paesaggio $U(x)$")
depth = st.sidebar.slider("Profondità Valle (Resilienza/Attrazione)", 0.1, 5.0, float(def_depth), 0.1, help="Quanto è forte il richiamo verso l'equilibrio? Alto = Forte omeostasi.")
width = st.sidebar.slider("Larghezza Valle (Flessibilità)", 0.5, 4.0, float(def_width), 0.1, help="Quanto è stretto il canale? Basso = Rigido/Canalizzato.")

st.sidebar.subheader("Parametri Dinamici")
noise_level = st.sidebar.slider("Intensità Rumore (Stress/Ambiente)", 0.0, 2.0, float(def_noise), 0.1, help="Ampiezza delle perturbazioni stocastiche.")
steps = st.sidebar.slider("Tempo di Simulazione (Steps)", 100, 1000, 500, 50)

# --- CALCOLO MATEMATICO ---

# 1. Definizione dello Spazio (Grid)
x_range = np.linspace(-4, 4, 50)
y_range = np.linspace(-4, 4, 50)
X, Y = np.meshgrid(x_range, y_range)

# 2. Definizione della Funzione Potenziale U(x,y)
# Usiamo una Gaussiana invertita per creare la valle centrale (Omeostasi)
# U(x) = -Depth * exp(-(x^2 + y^2) / Width)
# Nota: Matematicamente, il sistema cerca il MINIMO di U.
U = -depth * np.exp(-(X**2 + Y**2) / (2 * width**2))

# Aggiungiamo "muri" ai bordi per evitare che la pallina scappi all'infinito (vincoli fisiologici)
Boundary = 0.05 * (X**4 + Y**4) 
U_total = U + Boundary

# 3. Simulazione della Traiettoria (Metodo di Eulero-Maruyama)
dt = 0.05
traj_x = [2.5] # Posizione iniziale (fuori equilibrio)
traj_y = [2.5] # Posizione iniziale

current_x = traj_x[0]
current_y = traj_y[0]

np.random.seed(42) # Per riproducibilità demo

for _ in range(steps):
    # Calcolo del Gradiente (Pendenza) nel punto corrente
    # Derivata parziale approssimata di U rispetto a x e y
    # dU/dx = x * (depth/width^2) * exp(...) + 0.2*x^3
    
    exp_factor = np.exp(-(current_x**2 + current_y**2) / (2 * width**2))
    
    grad_x = (current_x * depth / width**2) * exp_factor - 0.2 * current_x**3
    grad_y = (current_y * depth / width**2) * exp_factor - 0.2 * current_y**3
    
    # Equazione: dx = Forza * dt + Rumore * sqrt(dt)
    # Forza = Gradiente positivo perché abbiamo definito U come buca negativa (quindi vogliamo salire verso 0 se usiamo U negativo, 
    # MA nella fisica standard dx/dt = -grad U. 
    # Qui la nostra valle è un minimo locale negativo. Il gradiente punta verso l'alto (uscita).
    # Quindi dobbiamo sottrarre il gradiente della funzione "buca".
    # Semplifichiamo: Forza di richiamo verso 0.
    
    force_x = - (current_x / width**2) * depth * exp_factor # Semplificata per stabilità numerica
    force_y = - (current_y / width**2) * depth * exp_factor
    
    # Aggiornamento posizione
    dx = force_x * dt + noise_level * np.sqrt(dt) * np.random.normal()
    dy = force_y * dt + noise_level * np.sqrt(dt) * np.random.normal()
    
    current_x += dx
    current_y += dy
    
    traj_x.append(current_x)
    traj_y.append(current_y)

# --- VISUALIZZAZIONE ---

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Visualizzazione 3D: Il Paesaggio")
    
    # Surface Plot (Il Paesaggio)
    fig = go.Figure(data=[go.Surface(z=U_total, x=X, y=Y, colorscale='Viridis', opacity=0.8, name='Epigenetic Landscape')])
    
    # Scatter 3D (La Traiettoria)
    # Calcoliamo Z per la traiettoria per farla aderire alla superficie
    traj_z = -depth * np.exp(-(np.array(traj_x)**2 + np.array(traj_y)**2) / (2 * width**2)) + 0.05 * (np.array(traj_x)**4 + np.array(traj_y)**4)
    
    fig.add_trace(go.Scatter3d(
        x=traj_x, y=traj_y, z=traj_z + 0.1, # Lift slightly above surface
        mode='lines+markers',
        marker=dict(size=4, color='red'),
        line=dict(color='red', width=2),
        name='Stato PNEI (t)'
    ))

    fig.update_layout(
        title='Topologia dello Stato',
        scene=dict(
            xaxis_title='Asse X (Struttura)',
            yaxis_title='Asse Y (Funzione)',
            zaxis_title='Potenziale (Energia)',
        ),
        height=600,
        margin=dict(l=0, r=0, b=0, t=40)
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Analisi Dinamica")
    
    st.markdown(f"**Profilo Attuale:** {profile}")
    
    # Time Series Plot
    df_traj = pd.DataFrame({'Step': range(len(traj_x)), 'X (Struttura)': traj_x, 'Y (Funzione)': traj_y})
    
    st.write("##### Evoluzione Temporale delle Variabili")
    st.line_chart(df_traj.set_index('Step'))
    
    st.info("""
    **Interpretazione Grafico:**
    * **Oscillazioni ampie:** Il sistema è instabile o sotto alto stress (Noise). tipico ADHD o Stress Acuto.
    * **Linea piatta:** Il sistema è bloccato in uno stato (Rigidità). tipico Depressione o ASD rigido.
    * **Convergenza a 0:** Ritorno all'omeostasi (Salute).
    """)

    dist_from_center = np.sqrt(np.array(traj_x)**2 + np.array(traj_y)**2)
    avg_dist = np.mean(dist_from_center[100:]) # Ignora fase iniziale
    
    st.metric("Dispersione Media (Allostasi)", f"{avg_dist:.2f}", delta_color="inverse")
    
    if avg_dist > 2.0:
        st.error("⚠️ ATTENZIONE: Sistema fuori equilibrio (Patologia)")
    elif avg_dist > 1.0:
        st.warning("⚠️ Carico Allostatico Elevato")
    else:
        st.success("✅ Sistema in Omeostasi")

# --- SPIEGAZIONE ACCADEMICA ---
st.divider()
st.subheader("Legenda Accademica per il Modello")
st.markdown("""
1.  **La Superficie ($U$) = Genotipo + Storia:**
    La forma delle valli non cambia rapidamente. È determinata dalla genetica e dalle esperienze precoci. Le valli rappresentano gli **Attrattori**.
    
2.  **Larghezza della Valle ($\sigma$) = Flessibilità Cognitiva/Immunitaria:**
    * *Stretta (ASD):* Il sistema tollera poche deviazioni. Basta poco per uscire dalla "zona di comfort", ma è difficile rientrarci se si viene spinti fuori.
    * *Larga (ADHD):* Il sistema accetta molti stati diversi, ma fatica a focalizzarsi su uno stabile.
    
3.  **Profondità della Valle ($k$) = Resilienza:**
    Quanto è forte la forza che ti riporta alla salute dopo uno stress?
    * *Profonda:* Recupero rapido.
    * *Piatta:* Recupero lento, vulnerabilità.
    
4.  **Posizione della Pallina ($x, y$) = Fenotipo Attuale:**
    L'intersezione istantanea tra i livelli di cortisolo, citochine infiammatorie e tono dell'umore.
""")