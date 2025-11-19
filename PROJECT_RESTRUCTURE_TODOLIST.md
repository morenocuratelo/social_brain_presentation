# **🤖 Social Brain Presentation - PNEI Model Integration & Restructure - To-Do List Dettagliata**

**Data Creazione:** 19/11/2025

**Stato Attuale:** 🟡 IN CORSO

**Priorità Generale:** CRITICA

**Risorsa Assegnata:** Moreno Curatelo / Development Team

## **🎯 Obiettivo della Task**

L'obiettivo è ristrutturare l'intera presentazione (sia web che Python) per posizionare il modello PNEI Waddington come **fondamento teorico** (Sezione 1c) da cui derivano tutte le ipotesi sperimentali (RQ1 & RQ2). Il modello deve essere **pienamente implementato e referenziato** in tutte le sezioni successive, con particolare enfasi su:

1. **Riorganizzazione strutturale**: Spostare PNEI Model da Sezione 5 → Sezione 1c
2. **Integrazione profonda**: RQ1 e RQ2 devono mostrare esplicitamente come ogni ipotesi deriva dal modello PNEI
3. **Conclusioni potenziate**: Sezione 4 (Implications → Conclusions) deve sintetizzare i risultati nel framework PNEI
4. **Coerenza visiva**: Grafici e visualizzazioni devono riflettere parametri Waddington in tutte le sezioni

---

## **📋 Task Breakdown (Scomposizione delle Attività)**

### **🔥 Fase 1: Analisi & Pianificazione Strutturale**

**Stima Sforzo:** 2 ore

| ID Task | Attività | Stato | Priorità | Note |
|---------|----------|-------|----------|------|
| 1.1 | Analizzare struttura attuale di index.html e identificare tutte le dipendenze della sezione "5-pnei" | [ ] | CRITICA | Mappare riferimenti, variabili JavaScript, funzioni correlate |
| 1.2 | Creare schema di navigazione revised: 0.Premises → 1.Setting (Design/Procedure/PNEI Model) → RQ1 → RQ2 → Conclusions | [ ] | CRITICA | Documentare in PROJECT_NAVIGATION_SCHEMA.md |
| 1.3 | Identificare tutti i punti in RQ1/RQ2 dove inserire riferimenti espliciti al modello PNEI | [ ] | ALTA | Creare matrice: Hypothesis → PNEI Parameters → Expected Physiology |
| 1.4 | Analizzare tutti i 4 simulatori Python per verificare coerenza nella presentazione del modello PNEI | [ ] | ALTA | Verificare che tutti usino stessa terminologia e parametri |
| 1.5 | Backup completo del progetto prima delle modifiche | [ ] | CRITICA | Creare branch: feature/pnei-restructure |

---

### **🔨 Fase 2: Ristrutturazione index.html - Core Implementation**

**Stima Sforzo:** 6-8 ore

#### **2.A: Spostamento Sezione PNEI (5 → 1c)**

| ID Task | Attività | Stato | Priorità | File Coinvolti |
|---------|----------|-------|----------|----------------|
| 2.1 | Rimuovere "5-pnei" dalla struttura deck e rinominare in "1c-pnei-model" | [ ] | CRITICA | index.html (linee ~600-700) |
| 2.2 | Aggiornare label navigazione: "5. PNEI Model" → inserire in "1. Exp. Setting" come sotto-tab "1c. PNEI Model" | [ ] | CRITICA | index.html - sezione deck['1-setting'] |
| 2.3 | Riordinare chiavi dell'oggetto deck: 0-premises → 1-setting (design/procedure/pnei-model) → 2-rq1 → 3-rq2 → 4-conclusions | [ ] | CRITICA | index.html - Variabile globale deck |
| 2.4 | Aggiornare sistema di navigazione per supportare 3 sub-tab in "1. Exp. Setting" invece di 2 | [ ] | ALTA | index.html - funzione renderSubNav() |
| 2.5 | Testare navigazione: verificare che clic su "1. Exp. Setting" mostri correttamente le 3 sotto-sezioni | [ ] | ALTA | Browser testing |

#### **2.B: Potenziamento Contenuto PNEI Model (ora 1c)**

| ID Task | Attività | Stato | Priorità | Note |
|---------|----------|-------|----------|------|
| 2.6 | Espandere sezione PNEI Model con "Theoretical Framework" introduttivo | [ ] | ALTA | Aggiungere: perché Waddington? Perché PNEI? Collegamenti alla letteratura |
| 2.7 | Creare sottosezione "Operationalization Logic" che spiega la mappatura parametri → fisiologia | [ ] | ALTA | Tabella interattiva: click su parametro → highlight nel grafico 3D |
| 2.8 | Aggiungere sottosezione "Predictive Power": come il modello genera ipotesi testabili | [ ] | ALTA | Esempio: "Se Depth=alto → aspettiamo HRV alto → test in RQ1" |
| 2.9 | Inserire riferimenti forward: "Questo modello verrà applicato in RQ1 (Social Bypass) e RQ2 (Interactivity)" | [ ] | MEDIA | Link interni cliccabili che portano a RQ1/RQ2 |
| 2.10 | Aggiungere visualizzazione: "3 Stati nel Paesaggio" - overlay delle 3 configurazioni (Baseline/Rigid/Dispersed) sul 3D plot | [ ] | MEDIA | Implementare con Plotly: mostrare 3 traiettorie simultanee in colori diversi |

#### **2.C: Integrazione PNEI in RQ1 (Social Weight)**

| ID Task | Attività | Stato | Priorità | File Coinvolti |
|---------|----------|-------|----------|----------------|
| 2.11 | **RQ1 - Social Bypass (2a)**: Aggiungere sezione "PNEI Framework Link" prima dell'ipotesi | [ ] | CRITICA | index.html - deck['2-rq1'].slides['bypass'] |
| 2.12 | Inserire diagramma: "Rigid State Topology → High Noise (Social Load) → Prediction: LLM bypasses noise" | [ ] | ALTA | Visualizzazione Waddington con overlay: Human (red trajectory) vs LLM (green trajectory) |
| 2.13 | Tabella predizioni PNEI esistente: aggiungere colonna "Waddington Parameter" per ogni misura | [ ] | ALTA | Es: "HRV Collapsing → Depth insufficiente per contenere Noise" |
| 2.14 | **RQ1 - Logical Depuration (2b)**: Collegare al concetto di "Noise Reduction" nel modello | [ ] | ALTA | "LLM riduce Noise sociale → paesaggio più 'pulito' per ragionamento logico" |
| 2.15 | Aggiungere mini-widget Waddington interattivo: mostrare come Amygdala activation cambia la superficie del paesaggio | [ ] | MEDIA | Widget ridotto (200px) che mostra deformazione del potenziale U(x) |

#### **2.D: Integrazione PNEI in RQ2 (Interactivity)**

| ID Task | Attività | Stato | Priorità | File Coinvolti |
|---------|----------|-------|----------|----------------|
| 2.16 | **RQ2 - Phantom ToM (3a)**: Aggiungere "PNEI Interpretation": rTPJ activation = perturbazione locale del paesaggio | [ ] | CRITICA | index.html - deck['3-rq2'].slides['phantom'] |
| 2.17 | Creare visualizzazione: curva rTPJ over time sovrapposta a grafico di "Noise temporale" nel modello | [ ] | ALTA | Dual-axis chart: asse Y1 = rTPJ activation, Y2 = ξ(t) noise |
| 2.18 | Spiegare "Habituation" NT vs "Sustained Engagement" ASD in termini di adattamento del parametro Width | [ ] | ALTA | "NT: Width aumenta nel tempo (adattamento). ASD: Width rimane costante (rigidità)" |
| 2.19 | **RQ2 - Burnout (3b)**: Collegare al concetto di "Depth Erosion" nel modello | [ ] | CRITICA | "Executive load costante erode Depth → valle diventa più piatta → HRV drop" |
| 2.20 | Aggiungere grafico: "Survival Curve" esistente + overlay "Predicted Depth(t) Trajectory" | [ ] | MEDIA | Mostrare che Depth decresce parallelamente alla probabilità di burnout |
| 2.21 | Inserire formula esplicita: "Allostatic Load = σ(Noise) × Duration / Depth" | [ ] | MEDIA | Derivazione matematica che giustifica perché ADHD in LLM → alto rischio |

#### **2.E: Trasformazione Implications → Conclusions**

| ID Task | Attività | Stato | Priorità | File Coinvolti |
|---------|----------|-------|----------|----------------|
| 2.22 | Rinominare sezione "4-implications" → "4-conclusions" | [ ] | CRITICA | index.html - chiave oggetto deck |
| 2.23 | Aggiornare label navigazione: "4. Implications" → "4. Conclusions" | [ ] | CRITICA | index.html - deck['4-conclusions'].label |
| 2.24 | Riorganizzare contenuto: da "When to use X" → "What the PNEI Model Tells Us" | [ ] | ALTA | Struttura: Theory → Evidence → Clinical Translation |
| 2.25 | Aggiungere sottosezione "Validation of the Model": come i risultati confermano le predizioni PNEI | [ ] | ALTA | Tabella: Prediction vs Observed (placeholder per dati futuri) |
| 2.26 | Inserire "Limitations & Future Directions" con riferimento al modello | [ ] | MEDIA | Es: "Need to measure cytokines for full PNEI validation", "Longitudinal studies to track state transitions" |
| 2.27 | Creare visualizzazione finale: "Unified PNEI Map" - tutti i 9 scenari (3×3) nel paesaggio | [ ] | ALTA | Heatmap 3D: X=Population state, Y=Environment, Z=Outcome, colorato per HRV/GSR/fNIRS |
| 2.28 | Sostituire "Doughnut chart" con "State Space Diagram": plottare i 9 scenari come punti nel piano (Depth, Noise) | [ ] | ALTA | Scatter plot con regioni colorate (Homeostasis/At-Risk/Crisis zones) |

---

### **🔨 Fase 3: Aggiornamento Simulatori Python**

**Stima Sforzo:** 6-9 ore (espanso per includere visualizzazione multi-partecipante)

#### **3.A: Simulatore Principale (PNEI_Waddington_Simulator.py)**

| ID Task | Attività | Stato | Priorità | File Coinvolti |
|---------|----------|-------|----------|----------------|
| 3.1 | Aggiungere sezione "Predictive Framework" prima dei controlli | [ ] | ALTA | PNEI_Waddington_Simulator.py - sidebar |
| 3.2 | Creare tabella "From Model to Hypotheses": linking parametri → RQ1/RQ2 predictions | [ ] | ALTA | Streamlit expander widget con cross-references |
| 3.3 | Implementare "Hypothesis Testing Mode": utente seleziona uno scenario (es: ASD+Human) → mostra predizioni PNEI | [ ] | MEDIA | Dropdown: 9 scenari → auto-set parameters + show expected physiology |
| 3.4 | Aggiungere annotazioni sui grafici: "This trajectory validates Social Bypass hypothesis (RQ1)" | [ ] | MEDIA | Plotly annotations dinamiche basate su stato selezionato |
| 3.5 | Creare sezione "Model Validation" in fondo: come confrontare predizioni con dati empirici | [ ] | BASSA | Placeholder per future data upload feature |
| 3.6 | **Implementare visualizzazione multi-partecipante in tempo reale** | [ ] | ALTA | Menu a tendina per selezionare: "Single Participant" vs "All Participants (Real-Time)" |
| 3.7 | Creare dashboard "All Participants View": griglia 3×N mostrando paesaggio Waddington di ogni partecipante | [ ] | ALTA | Layout: colonne = partecipanti, righe = (3D landscape, HRV/GSR time series, State label) |
| 3.8 | Implementare aggiornamento automatico: ogni 2-5 secondi ricalcola traiettorie con nuovi dati fisiologici | [ ] | ALTA | Usare st.rerun() con timer per simulare stream, collegare a futuro data pipeline (CSV/API) |
| 3.9 | Aggiungere statistiche comparative: media HRV gruppo, distribuzione stati (Baseline/Rigid/Dispersed) | [ ] | MEDIA | Sidebar con metrics: "5/12 in Homeostasis, 4/12 At-Risk, 3/12 Crisis" |
| 3.10 | Implementare filtri: visualizzare solo partecipanti in stato specifico (es: mostra solo "Rigid") | [ ] | MEDIA | Multiselect: Clinical Group (NT/ASD/ADHD), Current State (Baseline/Rigid/Dispersed) |
| 3.11 | Creare heatmap sinottica: matrice Partecipante×Sensore colorata per valori attuali | [ ] | MEDIA | Stile "fisheye": click su cella → espande grafico dettagliato di quel partecipante/sensore |

#### **3.B: Simulatori Secondari (1, 2, 3)**

| ID Task | Attività | Stato | Priorità | Note |
|---------|----------|-------|----------|------|
| 3.12 | **Simulator1** (Educational): Aggiungere slide "From Theory to Practice" che collega equazioni a RQ1/RQ2 | [ ] | MEDIA | Dopo spiegazione matematica, mostrare applicazione concreta |
| 3.13 | **Simulator2** (Philosophical): Espandere sezione "Pragmatic Model" con esempi da RQ1/RQ2 | [ ] | MEDIA | "Rigid state isn't autism - it's what we all experience under stress (see RQ1)" |
| 3.14 | **Simulator3** (Interactive): Aggiungere preset "RQ1 Scenarios" e "RQ2 Scenarios" | [ ] | MEDIA | 6 preset buttons: ASD+Human, ASD+LLM, ADHD+LLM, etc. |
| 3.15 | Sincronizzare terminologia: verificare che tutti e 4 i simulatori usino stessi nomi per parametri | [ ] | ALTA | Standardize: "Depth (Resilience)", "Noise (Allostatic Load)", "Width (Flexibility)" |

---

### **🧪 Fase 4: Testing & Validazione**

**Stima Sforzo:** 3-4 ore

| ID Task | Attività | Stato | Priorità | Note |
|---------|----------|-------|----------|------|
| 4.1 | **Test navigazione index.html**: verificare che tutte le sezioni siano accessibili nell'ordine corretto | [ ] | CRITICA | Testare su Chrome, Firefox, Safari |
| 4.2 | **Test responsiveness**: verificare layout su mobile/tablet per nuova struttura a 3 sub-tab | [ ] | ALTA | Particolare attenzione a sub-nav con 3 elementi |
| 4.3 | **Test widget Waddington**: verificare che preset funzionino e grafici si aggiornino correttamente | [ ] | ALTA | Testare tutti i 3 preset + manipolazione manuale sliders |
| 4.4 | **Test cross-references**: verificare che link interni "vedi RQ1/RQ2" portino alla sezione corretta | [ ] | MEDIA | Click su ogni link e verificare scroll/navigazione |
| 4.5 | **Test simulatori Python**: verificare che tutti e 4 i file .py si lancino senza errori | [ ] | CRITICA | `streamlit run PNEI_Waddington_SimulatorX.py` per X=1,2,3,main |
| 4.6 | **Test coerenza contenuti**: verificare che spiegazioni PNEI siano consistenti tra web e Python | [ ] | ALTA | Leggere side-by-side e verificare terminologia |
| 4.7 | **Peer review**: far testare navigazione e comprensibilità a collega/supervisore | [ ] | MEDIA | Raccogliere feedback su chiarezza del flusso logico |
| 4.8 | **Test performance**: verificare tempi di caricamento con nuovo widget 3D in più sezioni | [ ] | BASSA | Plotly può essere pesante - ottimizzare se necessario |

---

### **📚 Fase 5: Documentazione & Finalizzazione**

**Stima Sforzo:** 2-3 ore

| ID Task | Attività | Stato | Priorità | File Coinvolti |
|---------|----------|-------|----------|----------------|
| 5.1 | Aggiornare README.md con nuova struttura di navigazione | [ ] | ALTA | README.md - sezione "Features" |
| 5.2 | Aggiornare SIMULATOR_VERSIONS.md: aggiungere note su integrazione RQ1/RQ2 | [ ] | ALTA | SIMULATOR_VERSIONS.md |
| 5.3 | Aggiornare QUICK_REFERENCE.md con nuovo flusso: PNEI Model → Hypotheses → Results | [ ] | ALTA | QUICK_REFERENCE.md |
| 5.4 | Creare nuovo documento: PNEI_MODEL_INTEGRATION_GUIDE.md | [ ] | MEDIA | Spiega come il modello permea tutta la presentazione |
| 5.5 | Aggiornare HTML_UPDATE_SUMMARY.md con cambiamenti strutturali | [ ] | MEDIA | Documentare spostamento sezione 5→1c |
| 5.6 | Creare diagramma di flusso visuale: "From Theory to Conclusions" per appendice presentazione | [ ] | BASSA | Tool: draw.io o Mermaid diagram in Markdown |
| 5.7 | Aggiornare COMMIT_MESSAGE.md con nuovo messaggio per questa ristrutturazione | [ ] | MEDIA | COMMIT_MESSAGE.md |
| 5.8 | Scrivere changelog dettagliato in CHANGELOG.md (creare se non esiste) | [ ] | MEDIA | Formato: [Version 3.0] - YYYY-MM-DD |

---

## **⚠️ Rischi & Blocchi**

* [ ] **Rischio 1:** Spostamento sezione PNEI potrebbe rompere riferimenti JavaScript esistenti (es: ID elementi, event listeners).  
  * **Mitigazione:** Testare incrementalmente, mantenere ID coerenti durante refactor.

* [ ] **Rischio 2:** Aggiunta di widget Waddington multipli in index.html potrebbe rallentare rendering Plotly.  
  * **Mitigazione:** Usare versione "mini" del widget (risoluzione ridotta), lazy loading per widget fuori viewport.

* [ ] **Rischio 3:** Coerenza terminologica tra 4 simulatori Python + 1 HTML potrebbe essere difficile da mantenere.  
  * **Mitigazione:** Creare glossario condiviso (TERMINOLOGY.md), script di verifica automatica (grep per termini chiave).

* [ ] **Rischio 4:** Espansione contenuti potrebbe rendere sezione "1. Exp. Setting" troppo lunga e faticosa da navigare.  
  * **Mitigazione:** Usare collapsible sections (Streamlit expanders, HTML details/summary), design minimalista.

* [ ] **Rischio 5:** Utente abituato alla vecchia struttura potrebbe confondersi con PNEI come sezione 1c invece di 5.  
  * **Mitigazione:** Aggiungere banner temporaneo "New Structure!" nell'header, aggiornare tutti i materiali di supporto.

* [ ] **Rischio 6:** Visualizzazione multi-partecipante in tempo reale potrebbe causare problemi di performance con molti partecipanti (>20).  
  * **Mitigazione:** Implementare paginazione (mostrare 12 alla volta), ridurre refresh rate (5s invece di 2s), usare grafici 2D semplificati per overview invece di 3D completi.

* [ ] **Rischio 7:** In assenza di dati empirici reali, la modalità "All Participants" risulterà placeholder/mock, potenzialmente confondendo utenti.  
  * **Mitigazione:** Chiaramente etichettare come "Demo Mode" quando usa dati simulati; implementare generatore di dati sintetici realistici (con variabilità inter-individuale) per presentazioni.

---

## **🔗 Riferimenti & Risorse**

* **Specifiche Funzionali:** UPDATE_SUMMARY.md, HTML_UPDATE_SUMMARY.md  
* **Documentazione Modello PNEI:** SIMULATOR_VERSIONS.md, QUICK_REFERENCE.md  
* **File Principali da Modificare:**
  * `index.html` (core web presentation)
  * `PNEI_Waddington_Simulator.py` (main Python simulator)
  * `PNEI_Waddington_Simulator1.py, 2.py, 3.py` (secondary simulators)
  * `README.md`, `SIMULATOR_VERSIONS.md`, `QUICK_REFERENCE.md` (documentation)
* **Librerie Critiche:**
  * Plotly.js 2.27.0 (per grafici 3D Waddington)
  * Chart.js (per grafici standard in index.html)
  * Streamlit (per simulatori Python)
* **Branch Git:** feature/pnei-restructure (da creare in task 1.5)
* **Milestone Target:** Completamento entro [DATA DIFESA TESI] - lasciare 1 settimana di buffer per revisioni

---

## **📊 Metriche di Successo**

Al completamento di tutte le task, il progetto deve soddisfare:

1. ✅ **Navigazione Logica**: Utente comprende che PNEI Model è fondamento teorico (posizione 1c)
2. ✅ **Cross-Referencing**: Ogni ipotesi in RQ1/RQ2 cita esplicitamente parametri PNEI
3. ✅ **Coerenza Visiva**: Widget Waddington presente in almeno 4 sezioni (1c, 2a, 3a, 4)
4. ✅ **Testabilità**: Tabelle "Predictions" contengono valori quantitativi derivati dal modello
5. ✅ **Documentazione Completa**: Ogni file .md aggiornato riflette nuova struttura
6. ✅ **Zero Regression**: Tutte le funzionalità esistenti (grafici, interattività) funzionano post-refactor
7. ✅ **Peer Validation**: Almeno 1 revisore esterno conferma chiarezza del flusso logico

---

## **🗓️ Timeline Proposto**

| Fase | Durata Stimata | Data Inizio | Data Fine | Note |
|------|----------------|-------------|-----------|------|
| Fase 1 (Analisi) | 2 ore | [GG/MM] | [GG/MM] | Prerequisito per tutto il resto |
| Fase 2 (index.html Core) | 8 ore | [GG/MM] | [GG/MM] | Lavoro più critico e complesso |
| Fase 3 (Python Simulators) | 9 ore | [GG/MM] | [GG/MM] | Include visualizzazione multi-partecipante, può sovrapporsi parzialmente a Fase 2 |
| Fase 4 (Testing) | 4 ore | [GG/MM] | [GG/MM] | Inizio solo dopo completamento Fase 2 |
| Fase 5 (Documentazione) | 3 ore | [GG/MM] | [GG/MM] | Parallelo a Fase 4, finalizzato dopo test |
| **TOTALE** | **26 ore** | | | ~3.5 giorni lavorativi full-time o 1 settimana part-time |

---

## **🎓 Note per la Difesa**

Una volta completata questa ristrutturazione, nella presentazione potrai:

1. **Aprire con il Modello**: "Ecco il nostro framework teorico PNEI-Waddington" (1c)
2. **Derivare Ipotesi**: "Dal modello deduciamo che... (mostra parametri) ...quindi testiamo in RQ1/RQ2"
3. **Mostrare Coerenza**: "Ogni predizione fisiologica deriva matematicamente dal modello"
4. **Chiudere con Validazione**: "I risultati confermano/sfidano le predizioni del modello (Conclusions)"

Questo flusso narrativo è **molto più robusto scientificamente** rispetto a "ecco i risultati... ah, tra l'altro abbiamo un modello (sezione 5)".

---

**Status Tracking:** Aggiornare questo documento ad ogni task completata. Usare `git commit` frequentemente con messaggi descrittivi (es: "feat: moved PNEI section to 1c in index.html").

**Prossimo Step:** Iniziare da Task 1.1 (Analisi dipendenze sezione 5-pnei).
