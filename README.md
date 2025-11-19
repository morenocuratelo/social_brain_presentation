# PNEI Waddington Simulator

**A Pragmatic, Multi-Modal Model of Human Psycho-Neuro-Endocrine-Immunological States**

Interactive visualization and experimental design tool using **Waddington's Epigenetic Landscape** to model human states through comprehensive physiological measures.

## 🎯 Philosophy: Transitory States, Not Fixed Categories

**This is NOT a diagnostic tool. This is NOT about classifying "normal" vs "pathological".**

### The A Posteriori Paradigm

We build a **pragmatic model** based on measurable states, not idealistic categories:

- **"Neurotypical"** = Snapshot of optimal conditions (rest, social support, health)
- **"ASD-like State"** = Rigidity pattern accessible to anyone (burnout, hypervigilance, trauma)
- **"ADHD-like State"** = Dispersion pattern accessible to anyone (sleep deprivation, cognitive overload, chronic stress)

### Why Study Clinical Groups?

**Mathematical Reason:** Clinical groups occupy the **asymptotic boundaries** of the state space. The neurotypical population clusters near equilibrium where subtle relationships are invisible. Clinical groups reveal the **non-linear dynamics** that govern all humans.

**Philosophical Reason:** They are not "broken humans" but **explorers of landscape limits**. Under extreme stress, bereavement, or inflammation, any brain can transition to these topological states.

## 🔬 Multi-Modal PNEI Framework

### Comprehensive Physiological Operationalization

| Landscape Parameter | Physiological Measure | System | Interpretation |
|---------------------|----------------------|--------|----------------|
| **Depth** | HRV (RMSSD) | Autonomic (Parasympathetic) | Resilience, vagal tone |
| **Noise** | GSR + fNIRS (Amygdala) | Autonomic (Sympathetic) + Limbic | Stress, emotional reactivity |
| **Width** | Behavioral Rigidity | Executive (DLPFC) | Cognitive flexibility |
| **rTPJ** | fNIRS (Social Brain) | Social Network | Theory of Mind load |
| **DLPFC** | fNIRS (Executive) | Executive Network | Cognitive control |

**Innovation:** Bridges abstract dynamical systems theory with concrete, measurable physiological signals (HRV, GSR, fNIRS).

## Mathematical Model

This simulator visualizes a person's state as a particle in a **Waddington Landscape**, following the Langevin stochastic differential equation:

$$\frac{dx}{dt} = -\nabla U(x) + \xi(t)$$

Where:
- **U(x)**: Potential function (Genetics/Ontogenesis)
- **-∇U(x)**: Deterministic force (tendency to return to homeostasis)
- **ξ(t)**: Stochastic noise (Stress, Environment)

## 📊 Features

### Main Simulator (PNEI_Waddington_Simulator.py) ⭐
**Complete experimental design and validation tool**

- ✅ **Multi-Modal Sensor Dashboard**: HRV, GSR, fNIRS (Amygdala, rTPJ, DLPFC)
- ✅ **Experimental Design Matrix**: 3 Populations × 3 Environments (9 scenarios)
- ✅ **Predicted Physiological Responses**: Shows expected sensor readings for each condition
- ✅ **Waddington Landscape Visualization**: 2D potential well with particle dynamics
- ✅ **State Trajectory Over Time**: Temporal evolution with PNEI-mapped zones
- ✅ **Comprehensive Operationalization Table**: Maps landscape ↔ physiology
- ✅ **Scientific Justification**: Explains why clinical groups inform universal mechanisms

### Alternative Versions

See [SIMULATOR_VERSIONS.md](SIMULATOR_VERSIONS.md) for detailed comparison:
- **Simulator1**: Educational/mathematical focus
- **Simulator2**: Philosophical/conceptual exploration  
- **Simulator3**: Interactive demo with preset buttons

## Requirements

### Python Version

**Recommended**: Python 3.11 or 3.12

**Note**: Python 3.14 may have compatibility issues with PyArrow (required by Streamlit). If you encounter installation errors, please use Python 3.11 or 3.12.

### Dependencies

```txt
streamlit>=1.28.0
numpy>=1.24.0,<2.0.0
plotly>=5.17.0
pandas>=2.0.0
```

## Installation

### Option 1: Standard Installation (Python 3.11-3.12)

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows PowerShell:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### Option 2: If Using Python 3.14 (with PyArrow issues)

```bash
# Try installing with binary wheels only
pip install --only-binary :all: pyarrow
pip install -r requirements.txt

# Or use the installation helper script
python install_deps.py
```

### Option 3: Use Python 3.12 Specifically

```bash
# Create venv with Python 3.12
py -3.12 -m venv .venv312
.venv312\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

Run the simulator:

```bash
streamlit run PNEI_Waddington_Simulator.py
```

The application will open in your default web browser at `http://localhost:8501`

## State Presets (Transient Configurations)

### Baseline State
- **Valley Depth**: 1.5 (moderate resilience)
- **Valley Width**: 1.5 (balanced flexibility)
- **Noise Level**: 0.5 (standard environmental input)
- **When**: Optimal conditions (rested, supported, healthy)
- **Universal**: This is the "statistical normal" anyone can reach with proper resources

### Rigid State (Hypervigilance)
- **Valley Depth**: 4.0 (strong homeostatic pull, but narrow range)
- **Valley Width**: 0.8 (narrow tolerance window)
- **Noise Level**: 0.4 (reduced processing of external variance)
- **When**: Burnout, PTSD, chronic stress, autistic shutdown
- **Universal**: Anyone can enter this state under prolonged threat or depletion

### Dispersed State (Cognitive Overload)
- **Valley Depth**: 0.5 (weak homeostatic pull)
- **Valley Width**: 3.0 (wide but unstable)
- **Noise Level**: 0.8 (high sensitivity to distraction)
- **When**: Sleep deprivation, ADHD episode, information overload, multitasking
- **Universal**: Common during exams, crises, or chronic task-switching

### Custom
- Manually adjust parameters to explore intermediate states or simulate specific interventions

## Interpretation

### Landscape Parameters (Universal Mechanisms)

1. **Valley Depth (k)**: Resilience / Recovery Speed
   - Deep: Quick return to baseline after stress (good recovery)
   - Shallow: Slow recovery, prolonged dysregulation
   - **Not fixed**: Can change with sleep, social support, inflammation levels

2. **Valley Width (σ)**: Flexibility / Tolerance Window
   - Narrow: Low tolerance for deviation (rigid, but stable if not perturbed)
   - Wide: High tolerance (flexible, but hard to maintain focus)
   - **Not fixed**: Modulated by fatigue, sensory load, emotional regulation

3. **Particle Position (x, y)**: Current Physiological State
   - Real-time intersection of cortisol, inflammatory cytokines, HRV, and mood
   - **Dynamic**: Changes minute-to-minute based on stressors and resources

### Pragmatic Metrics (For All Humans)

- **Large Oscillations**: High allostatic load (common during crises, exams, grief)
- **Flat Convergence**: Locked state (depression, chronic fatigue, or deep rest)
- **Return to Center**: Successful homeostatic regulation

**Allostatic Load (Dispersion)**:
- `< 1.0`: Homeostasis - System resilient ✅
- `1.0 - 2.0`: Elevated load - Preventive intervention window ⚠️
- `> 2.0`: Critical dysregulation - Immediate support needed 🚨

### Clinical Insight

These patterns are **not diagnostic labels** but **state descriptors** that inform intervention:
- Rigid state → Reduce social/sensory load, provide predictability
- Dispersed state → Reduce task-switching, provide external structure
- Baseline state → Maintain resources, challenge growth

## Troubleshooting

### PyArrow Installation Errors

If you see errors about PyArrow failing to build:

1. **Use Python 3.11 or 3.12** (most reliable)
2. Try installing PyArrow separately:
   ```bash
   pip install --only-binary :all: pyarrow
   ```
3. Use the provided `install_deps.py` helper script
4. Install via Conda if available:
   ```bash
   conda install -c conda-forge pyarrow
   ```

### CMake Errors

The CMake errors indicate PyArrow is trying to build from source. Solutions:
- Ensure you're using Python 3.11 or 3.12
- Update pip: `pip install --upgrade pip setuptools wheel`
- Force binary installation: `pip install --only-binary :all: -r requirements.txt`

## License

Educational use for neuroscience and PNEI research.

## Author

Created for The Social Brain course - University of Turin
