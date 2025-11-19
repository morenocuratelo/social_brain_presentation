# PNEI Waddington Simulator Versions - Complete Documentation

## Project Philosophy

This project implements a **pragmatic, a posteriori model** of human psycho-neuro-endocrine-immunological (PNEI) states using **Waddington's Epigenetic Landscape** metaphor.

### Core Paradigm: Transitory States, Not Fixed Categories

**Key Insight:** Clinical groups (ASD, ADHD) represent **accessible topological states** that anyone can reach under specific conditions, not fundamentally different categories of humans.

- **"Neurotypical"** = Snapshot of optimal conditions (rest, social support, health)
- **"ASD-like"** = State of rigidity (burnout, hypervigilance, trauma) 
- **"ADHD-like"** = State of dispersion (sleep deprivation, cognitive overload, chronic stress)

### Scientific Foundation

The model is based on the **Langevin overdamped stochastic differential equation**:

$$\frac{dx}{dt} = -\nabla U(x) + \xi(t)$$

Where:
- **$U(x)$** = Potential landscape (genetics, developmental history)
- **$-\nabla U(x)$** = Deterministic force toward homeostasis
- **$\xi(t)$** = Stochastic noise (environmental stress, sensory input)

## PNEI Operationalization Framework

### Multi-Dimensional Mapping

| Waddington Parameter | Physiological Measure | System | Interpretation |
|---------------------|----------------------|--------|----------------|
| **Depth ($k$)** | HRV (RMSSD) | Autonomic (Parasympathetic) | Resilience, vagal tone, ability to return to baseline |
| **Noise ($\xi$)** | GSR + fNIRS (Amygdala) | Autonomic (Sympathetic) + Limbic | Stress, emotional reactivity, unprocessed environmental friction |
| **Width ($\sigma$)** | Behavioral Rigidity | Executive (DLPFC) | Cognitive flexibility vs. channelization |
| **rTPJ Activation** | fNIRS (Social Brain) | Social Network | Theory of Mind, social cognition load |
| **DLPFC Activation** | fNIRS (Executive) | Executive Network | Cognitive control, scaffolding support |

---

## Simulator Versions

### **PNEI_Waddington_Simulator.py** ⭐ MAIN VERSION
**Purpose:** Complete experimental design tool for research validation

**Features:**
- ✅ Full PNEI multi-modal sensor suite (HRV, GSR, fNIRS: Amygdala/rTPJ/DLPFC)
- ✅ Experimental design matrix: 3 Populations × 3 Environments
- ✅ Predicted physiological responses for each scenario
- ✅ Comprehensive operationalization table
- ✅ Scientific justification for including clinical groups

**Use Case:** 
- Academic presentations
- Grant proposals
- Experimental design validation
- Demonstrating PNEI framework completeness

**Target Audience:** Research committees, scientific conferences, PNEI specialists

---

### **PNEI_Waddington_Simulator1.py**
**Purpose:** Educational tool focused on mathematical foundations

**Features:**
- ✅ Clean mathematical presentation of Langevin equation
- ✅ Clinical profile presets (Neurotypical, ASD, ADHD)
- ✅ Interactive sliders for landscape parameters
- ✅ Focus on understanding differential equations

**Use Case:**
- Teaching computational psychiatry
- Mathematics/physics students
- Understanding dynamical systems

**Target Audience:** Students, educators, computational neuroscience courses

---

### **PNEI_Waddington_Simulator2.py**
**Purpose:** Philosophical and conceptual exploration

**Features:**
- ✅ Strong emphasis on "pragmatic, not idealistic" model
- ✅ Transitory states paradigm explanation
- ✅ Renamed from diagnoses to "system states"
- ✅ Includes "Critical Transition" state
- ✅ Dimensional vs categorical approach

**Use Case:**
- Philosophical discussions
- Anti-stigma presentations
- Explaining dimensional psychopathology
- Neurodiversity advocacy

**Target Audience:** Psychologists, psychiatrists, mental health advocates, general public

---

### **PNEI_Waddington_Simulator3.py**
**Purpose:** Interactive demonstration with preset buttons

**Features:**
- ✅ Quick-access preset buttons (Baseline, Rigidity, Dispersion)
- ✅ Italian language interface
- ✅ Transitory states philosophy
- ✅ Real-time parameter manipulation
- ✅ Toast notifications for state changes

**Use Case:**
- Live demonstrations
- Conference presentations
- Interactive workshops
- Quick concept illustration

**Target Audience:** Conference attendees, workshop participants, Italian-speaking audiences

---

## Recommendation: Which Version to Use?

### For Your Thesis/Research Defense:
→ **PNEI_Waddington_Simulator.py** (MAIN)
- Shows complete PNEI framework
- Demonstrates experimental rigor
- Maps all physiological measures
- Justifies clinical group inclusion

### For Teaching a Class:
→ **PNEI_Waddington_Simulator1.py**
- Clear mathematical foundation
- Step-by-step parameter explanation
- Educational focus

### For Public Engagement:
→ **PNEI_Waddington_Simulator2.py**
- Accessible language
- Anti-stigma messaging
- Philosophical depth

### For Live Demos:
→ **PNEI_Waddington_Simulator3.py**
- Quick preset switching
- Interactive and engaging
- Visual feedback

---

## Recent Changes (Nov 19, 2025)

### Commit History Analysis

**Commit 37f9854:** Created comprehensive PNEI operationalization
- Added HRV, GSR, fNIRS (Amygdala, DLPFC)
- Created sensor prediction dashboard
- Mapped landscape → physiology

**Commit 513c55e:** Specialized to fNIRS regions (INCOMPLETE)
- ⚠️ **REMOVED** HRV and GSR measures
- ⚠️ **REMOVED** Amygdala activation
- ✅ Added rTPJ vs DLPFC distinction
- ❌ Lost multi-modal PNEI validation

**Current Update:** RESTORED comprehensive PNEI framework
- ✅ Brought back HRV (Vagal Tone)
- ✅ Brought back GSR (Stress)
- ✅ Brought back Amygdala (Emotion)
- ✅ Kept rTPJ and DLPFC specificity
- ✅ Updated philosophy to emphasize transitory states
- ✅ Added comprehensive operationalization table
- ✅ Added justification for clinical groups as "boundary explorers"

---

## Key Insights for Your Research

### Why Study Clinical Groups?

**Mathematical Answer:**
Clinical groups occupy the **asymptotic limits** of the state space. The neurotypical population clusters near the central attractor (homeostasis), where non-linear relationships are too subtle to detect ("noise floor"). Clinical groups "stretch" the model to reveal correlations (e.g., inflammation → mood) that are invisible in equilibrium.

**Philosophical Answer:**
Clinical groups are not "broken humans" but **explorers of the landscape boundaries**. They show us where the valleys end and mountains begin. Under extreme stress, bereavement, or inflammation, any "statistically normal" brain can transition to these topologies.

### The A Posteriori Model

Unlike traditional nosology (DSM categories based on expert consensus), this is an **empirical, measurement-driven** model:

1. **Observe** the system under various conditions
2. **Measure** multiple physiological dimensions
3. **Map** the state space based on actual data
4. **Define** states by their topological properties, not subjective labels

This is pragmatic science: describing humans as they **are** under measurable conditions, not as idealized categories.

---

## Technical Notes

### Running the Simulators

```bash
# Install dependencies
pip install streamlit numpy plotly pandas

# Run any version
streamlit run PNEI_Waddington_Simulator.py
streamlit run PNEI_Waddington_Simulator1.py
streamlit run PNEI_Waddington_Simulator2.py
streamlit run PNEI_Waddington_Simulator3.py
```

### Dependencies
- `streamlit`: Interactive web app framework
- `numpy`: Numerical computation
- `plotly`: Interactive visualizations
- `pandas`: Data handling

### Potential Enhancement

Future versions could add:
- Real-time sensor data integration
- Machine learning classification
- Population statistics overlay
- Longitudinal trajectory tracking
- Multi-agent simulation (social dynamics)

---

## Citation

If using this model in academic work, cite:

> "A Pragmatic PNEI Model of Human States: Waddington Landscape Operationalization Through Multi-Modal Physiological Measures. Based on Langevin dynamics and dimensional psychopathology framework."

---

## Contact & Contribution

This is a living model. Feedback and contributions welcome.

**Philosophy:** Science should be pragmatic, measurable, and anti-stigma. This model treats all humans as possessing the same biological machinery, experiencing different topological configurations under varying conditions.

---

*Last Updated: November 19, 2025*
*Version: 2.0 (Comprehensive PNEI Restoration)*
