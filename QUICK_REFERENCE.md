# Quick Reference Guide - PNEI Waddington Simulator

## 🎯 One-Page Overview

### What Is This?
A **comprehensive PNEI model** using Waddington's landscape to visualize human states through multi-modal physiological sensors.

### Core Philosophy
**Transitory States, Not Fixed Categories**
- Clinical groups = Accessible topological states, not pathologies
- Everyone can reach "ASD-like" (stress) or "ADHD-like" (exhaustion) states
- Pragmatic, measurement-driven, anti-stigma approach

---

## 📊 The 5 PNEI Sensors

| Sensor | What It Measures | System | Maps To |
|--------|------------------|--------|---------|
| **HRV** | Vagal tone, resilience | Autonomic (Parasympathetic) | **Depth** (valley depth) |
| **GSR** | Sympathetic stress | Autonomic (Sympathetic) | **Noise** (perturbations) |
| **fNIRS (Amygdala)** | Emotional reactivity | Limbic | **Noise** (emotional friction) |
| **fNIRS (rTPJ)** | Social cognition | Social Brain | **Noise** (social load) |
| **fNIRS (DLPFC)** | Executive control | Executive Network | **Depth** (cognitive scaffolding) |

---

## 🧪 The 9 Experimental Scenarios

### Matrix: 3 Populations × 3 Environments

|  | **G3: Book** | **G1: Human Tutor** | **G4: LLM** |
|---|---|---|---|
| **Neurotypical** | Baseline | Social scaffolding ✅ | Logical depuration |
| **ASD-like** | Baseline | Social friction 🚨 | Social bypass ✅ |
| **ADHD-like** | Baseline | External regulation ✅ | Executive burnout ⚠️ |

### Key Predictions

**ASD + Human:** 🚨 High amygdala, spiking GSR, collapsing HRV  
**ASD + LLM:** ✅ Low amygdala, stable HRV, freed DLPFC resources  
**ADHD + LLM:** ⚠️ Rising amygdala, fading DLPFC, dropping HRV  

---

## 🔬 The Mathematical Model

$$\frac{dx}{dt} = -\nabla U(x) + \xi(t)$$

- **$U(x)$** = Landscape shape (genetics, learning history)
- **$-\nabla U(x)$** = Homeostatic pull (return to equilibrium)
- **$\xi(t)$** = Stochastic noise (stress, environment)

**Landscape Parameters:**
- **Depth ($k$)** = Resilience (HRV proxy)
- **Width ($\sigma$)** = Flexibility vs. Rigidity
- **Noise ($\zeta$)** = Allostatic load (GSR/Amygdala)

---

## 📁 Which File to Use?

### 🎓 Research Defense / Thesis
→ **PNEI_Waddington_Simulator.py**
- Complete experimental design
- All 5 sensors, 9 scenarios
- Scientific justification included

### 🎤 Conference Presentation
→ **PNEI_Waddington_Simulator3.py**
- Quick preset buttons
- Live demo ready
- Visual feedback

### 👨‍🏫 Teaching Class
→ **PNEI_Waddington_Simulator1.py**
- Mathematical focus
- Educational annotations

### 🧠 Public Engagement
→ **PNEI_Waddington_Simulator2.py**
- Anti-stigma messaging
- Accessible language

---

## 🚀 Quick Start

```bash
# Install
pip install streamlit numpy plotly pandas

# Run main version
streamlit run PNEI_Waddington_Simulator.py
```

Opens at: `http://localhost:8501`

---

## 💡 Key Talking Points

### 1. Why Study Clinical Groups?
"Clinical groups occupy the **asymptotic boundaries** of the state space. They reveal non-linear dynamics invisible at equilibrium. Not 'broken' but **boundary explorers** showing limits all humans can reach under stress."

### 2. Transitory States
"Under bereavement, inflammation, or sleep deprivation, any 'normal' brain can transition to rigid (ASD-like) or labile (ADHD-like) topologies. **Same machinery, different conditions.**"

### 3. Multi-Modal Validation
"Not just brain imaging. We validate through **5 concurrent physiological measures** spanning central, autonomic, limbic, social, and executive systems."

### 4. A Posteriori Model
"Built from measurements, not assumptions. Describes humans **as they are** under measurable conditions, not as idealized diagnostic categories."

---

## 📊 Expected Sensor Signatures (Quick Reference)

### Baseline (All Populations + Book)
- Amygdala: Low
- rTPJ: Low
- DLPFC: Moderate
- HRV: Stable
- GSR: Low

### Social Friction (ASD + Human)
- Amygdala: 🚨 HIGH ALERT (Red)
- rTPJ: 🚨 SPIKE
- DLPFC: Low (resource steal)
- HRV: 📉 Collapsing
- GSR: 📈 Spiking

### Social Bypass (ASD + LLM)
- Amygdala: ✅ Low/Baseline
- rTPJ: ✅ Low (energy saved)
- DLPFC: 📈 High (resources freed)
- HRV: Stable
- GSR: Low

### Executive Burnout (ADHD + LLM)
- Amygdala: Rising (frustration)
- rTPJ: Phantom activation
- DLPFC: 📉 Fading (fatigue)
- HRV: 📉 Dropping fast
- GSR: High (sustained effort)

---

## 🔍 Troubleshooting

**No graphs showing?**
→ Check Python version (use 3.11 or 3.12)

**PyArrow errors?**
→ `pip install --only-binary :all: pyarrow`

**Streamlit won't start?**
→ Activate virtual environment first

---

## 📚 Full Documentation

- **SIMULATOR_VERSIONS.md** - Detailed version comparison
- **UPDATE_SUMMARY.md** - Complete change log
- **README.md** - Full project documentation
- **INTEGRATION_GUIDE.md** - Technical integration

---

## ✅ Pre-Presentation Checklist

- [ ] Review the 5 sensor mappings
- [ ] Understand 9 experimental scenarios
- [ ] Practice explaining transitory states philosophy
- [ ] Memorize key talking points (above)
- [ ] Test the simulator (run locally once)
- [ ] Prepare answers to expected questions
- [ ] Have examples ready (stress→ASD-like, fatigue→ADHD-like)

---

## 🎯 Defense Day Essentials

**If asked:** "Why not just diagnose ASD/ADHD?"
**Answer:** "We're not diagnosing. We're mapping **topological states** that anyone can enter. Clinical groups show us the **mathematical limits** of human variability under stress. This informs interventions for **everyone**."

**If asked:** "How do you validate this?"
**Answer:** "Multi-modal concurrent measurement. If we predict high amygdala + low HRV for Scenario X, we **measure it** with fNIRS and ECG. The operationalization table provides exact protocol."

**If asked:** "What's new here?"
**Answer:** "First **comprehensive bridge** between Waddington's abstract dynamical systems and **concrete PNEI sensors**. Enables empirical validation of theoretical concepts through 5 simultaneous physiological measures."

---

*Print this page for quick reference during presentations!*

**Version:** 1.0  
**Updated:** November 19, 2025  
**Status:** ✅ Ready for research defense
