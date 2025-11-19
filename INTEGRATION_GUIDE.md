# Guida all'Integrazione del Widget Waddington

## ✅ Completato

Il simulatore Waddington è stato **completamente integrato** nell'index.html come sezione interattiva.

## 📂 File Aggiornati

### 1. **index.html**
- ✅ Aggiunta libreria Plotly.js per visualizzazioni 3D
- ✅ Nuovi stili CSS per controlli del widget
- ✅ Nuova sezione "5. PNEI Model" nel deck
- ✅ Funzioni JavaScript integrate:
  - `renderWaddingtonWidget()` - Renderizza l'interfaccia
  - `simulateWaddington()` - Esegue la simulazione fisica
  - `loadWaddingtonPreset()` - Carica preset (Baseline/Rigid/Dispersed)
  - `updateWaddington()` - Aggiorna in tempo reale

### 2. **PNEI_Waddington_Simulation.py** (Streamlit)
- ✅ Aggiornato con filosofia "stati transitori"
- ✅ Preset rinominati con interpretazione universale
- ✅ Metriche di carico allostatico

### 3. **waddington_widget.html** (Standalone)
- ✅ Widget HTML standalone (opzionale, per testing isolato)

## 🚀 Come Usare

### Opzione 1: Versione Integrata (Presentazione)

1. **Apri index.html nel browser**:
   ```
   Doppio click su: index.html
   O usa Live Server in VS Code
   ```

2. **Naviga alla sezione PNEI**:
   - Clicca su "5. PNEI Model" nella barra di navigazione superiore
   - Vedrai il simulatore interattivo nel pannello destro

3. **Interagisci con il modello**:
   - **Preset**: Clicca su 🟢 Baseline, 🔵 Rigid, o 🟡 Dispersed
   - **Sliders**: Regola manualmente Depth, Width, Noise, Steps
   - **Visualizzazione**: Ruota il plot 3D con il mouse
   - **Metriche**: Osserva Allostatic Load e State in tempo reale

### Opzione 2: Streamlit (Per Analisi Dettagliata)

```bash
streamlit run PNEI_Waddington_Simulation.py
```

- Più controlli e spiegazioni dettagliate
- Grafici 2D aggiuntivi
- Interpretazioni cliniche estese

### Opzione 3: Widget Standalone

```
Apri: waddington_widget.html
```

- Versione completa del widget in pagina dedicata
- Utile per embedding in altre pagine o per testing

## 🎯 Caratteristiche dell'Integrazione

### Interfaccia Unificata
- **Seamless**: Il widget si integra perfettamente con il design della presentazione
- **Responsive**: Funziona su desktop e tablet
- **Consistent**: Usa gli stessi colori e stili del resto della presentazione

### Interattività Real-Time
- **Preset istantanei**: 3 configurazioni pre-definite
- **Sliders fluidi**: Aggiornamento continuo della simulazione
- **Visualizzazione 3D**: Rotazione e zoom con Plotly

### Metriche Dinamiche
- **Allostatic Load**: Calcolo automatico della dispersione media
- **State Classification**: Identifica automaticamente Baseline/Rigid/Dispersed

## 📊 Parametri del Modello

| Parametro | Range | Significato |
|-----------|-------|-------------|
| **Depth** | 0.1 - 5.0 | Resilienza - Forza di ritorno all'equilibrio |
| **Width** | 0.5 - 4.0 | Flessibilità - Ampiezza della valle |
| **Noise** | 0.0 - 2.0 | Stress ambientale - Intensità perturbazioni |
| **Steps** | 100 - 600 | Durata simulazione - Tempo di osservazione |

## 🔧 Personalizzazione Avanzata

### Modificare i Preset

In `index.html`, trova la funzione `loadWaddingtonPreset()`:

```javascript
function loadWaddingtonPreset(type) {
    switch(type) {
        case 'baseline':
            waddingtonParams = { depth: 1.5, width: 1.5, noise: 0.5, steps: 300 };
            break;
        case 'rigid':
            waddingtonParams = { depth: 4.0, width: 0.8, noise: 0.4, steps: 300 };
            break;
        // Aggiungi nuovi preset qui
    }
}
```

### Cambiare i Colori del Plot

Nella funzione `simulateWaddington()`:

```javascript
const trajectoryTrace = {
    // ...
    line: { color: '#ef4444', width: 3 },  // Rosso
    marker: { size: 2.5, color: '#dc2626' }
};
```

### Aggiungere Metriche Personalizzate

Dopo il calcolo di `avgLoad`:

```javascript
// Esempio: Calcola varianza
const variance = distances.reduce((sum, d) => sum + (d - avgLoad)**2, 0) / distances.length;
```

## 🐛 Troubleshooting

### Il widget non appare
1. Verifica che la sezione "5. PNEI Model" sia selezionata
2. Controlla la console del browser (F12) per errori JavaScript
3. Assicurati che Plotly.js sia caricato (verifica connessione internet)

### La simulazione è lenta
1. Riduci il numero di Steps (slider in basso a destra)
2. Riduci gridSize in `simulateWaddington()` (attualmente 30)

### I preset non funzionano
1. Assicurati di aver salvato le modifiche all'index.html
2. Ricarica la pagina con Ctrl+F5 (hard refresh)

## 🎓 Uso Didattico

### Durante la Presentazione

1. **Introduci il concetto** (slide testuale a sinistra)
2. **Mostra Baseline** → "Ecco come appare uno stato ottimale"
3. **Passa a Rigid** → "Osserva come la valle si stringe (ipervigilanza)"
4. **Passa a Dispersed** → "Nota la traiettoria caotica (sovraccarico)"
5. **Regola manualmente** → "Aumentiamo il Noise per simulare stress acuto"

### Esperimento Live

Chiedi al pubblico di chiamare parametri e mostra gli effetti in diretta:
- "Che succede se aumentiamo Width a 3.5 ma manteniamo Depth alto?"
- "Se riduciamo il Noise a zero, la traiettoria converge?"

## 📝 Note Tecniche

### Algoritmo di Simulazione
- **Metodo**: Euler-Maruyama (discretizzazione stocastica)
- **Step size**: dt = 0.05
- **Funzione potenziale**: U(x,y) = -depth × exp(-r²/2σ²) + 0.05×(x⁴+y⁴)

### Performance
- **Complessità**: O(gridSize² + steps)
- **Rendering**: Gestito da Plotly (WebGL accelerato)
- **Refresh**: ~100-300ms per simulazione completa

### Browser Supportati
- ✅ Chrome/Edge (Chromium) - Raccomandato
- ✅ Firefox
- ✅ Safari (macOS/iOS)
- ⚠️ IE11 - Non supportato

## 🚀 Prossimi Sviluppi

- [ ] Aggiungere animazione temporale (play/pause)
- [ ] Export dei dati come CSV
- [ ] Integrazione con dati fNIRS/HRV reali
- [ ] Modalità comparativa (2 simulazioni side-by-side)
- [ ] Preset custom salvabili in localStorage

## 📧 Supporto

Per problemi o domande, contatta il team di sviluppo o apri un issue nel repository.

---

**Versione**: 1.0 (Integrazione completa)  
**Data**: 19 Novembre 2025  
**Compatibilità**: Modern browsers (ES6+)
