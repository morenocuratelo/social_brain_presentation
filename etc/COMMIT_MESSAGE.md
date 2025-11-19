# Suggested Commit Message

## Title
```
feat: Restore comprehensive PNEI multi-modal framework
```

## Full Message
```
feat: Restore comprehensive PNEI multi-modal framework

WHAT CHANGED:
- Restored full PNEI sensor suite: HRV, GSR, fNIRS (Amygdala/rTPJ/DLPFC)
- Updated all 9 experimental scenarios with complete physiological predictions
- Enhanced dashboard: 5 comprehensive metrics (was 2)
- Restored operationalization table: 5 mappings (was 2)
- Added scientific justification for clinical groups as boundary explorers
- Integrated transitory states philosophy throughout

WHY:
Previous commit (513c55e) narrowed focus to fNIRS-only, losing:
- Autonomic measures (HRV = vagal tone/resilience)
- Peripheral stress indicators (GSR = sympathetic arousal)
- Limbic activation (Amygdala = emotional reactivity)
- Holistic PNEI validation approach

This restoration aligns with original vision from LLM conversation:
multi-dimensional state space, Waddington landscape, pragmatic a posteriori
model validated through comprehensive physiological sensors.

PHILOSOPHY EMPHASIS:
- Clinical groups = accessible topological states, not pathologies
- Dimensional (not categorical) approach
- Universal mechanisms studied at their limits
- Neuroplasticity: states are transitory, not fixed

NEW DOCUMENTATION:
- SIMULATOR_VERSIONS.md: Complete version comparison guide
- UPDATE_SUMMARY.md: Detailed change log and rationale
- QUICK_REFERENCE.md: One-page presenter's guide
- Enhanced README.md with full PNEI framework

TECHNICAL:
- No errors, all files validated
- Backward compatible with existing code
- Enhanced scientific rigor and completeness
- Ready for research defense/publication

STATE: All files now reflect state-of-the-art PNEI vision ✅
```

## Alternative Short Version
```
feat: Restore comprehensive PNEI framework (HRV, GSR, Amygdala + rTPJ/DLPFC)

Previous commit removed autonomic and limbic measures, narrowing to fNIRS-only.
This restores the complete multi-modal PNEI validation approach:

Restored:
- HRV (vagal tone/resilience) 
- GSR (sympathetic stress)
- fNIRS Amygdala (emotional reactivity)
- Comprehensive operationalization table (5 mappings)
- Scientific justification for clinical groups
- Transitory states philosophy integration

Added:
- SIMULATOR_VERSIONS.md (version comparison)
- UPDATE_SUMMARY.md (complete change log)
- QUICK_REFERENCE.md (presenter guide)

All files now aligned with state-of-the-art PNEI vision.
```

## For Git Commands
```bash
# Stage all changes
git add .

# Commit with detailed message
git commit -m "feat: Restore comprehensive PNEI multi-modal framework

Restored full PNEI sensor suite (HRV, GSR, fNIRS: Amygdala/rTPJ/DLPFC) and
comprehensive operationalization framework. Previous commit narrowed to 
fNIRS-only, losing autonomic and limbic validation measures.

Changes:
- Restored HRV (vagal tone), GSR (stress), Amygdala (emotion)
- Updated all 9 scenarios with complete sensor predictions
- Enhanced dashboard: 5 metrics organized by system
- Operationalization table: 5 complete mappings
- Added scientific justification for clinical groups
- Integrated transitory states philosophy

Documentation:
- SIMULATOR_VERSIONS.md: Complete version guide
- UPDATE_SUMMARY.md: Detailed change analysis
- QUICK_REFERENCE.md: One-page presenter guide
- Enhanced README.md with full framework

Philosophy: Clinical groups as accessible topological states (not pathologies),
dimensional approach, pragmatic a posteriori model validated through 
multi-modal physiological sensors.

Status: All files aligned with state-of-the-art PNEI vision ✅"

# Push to remote
git push origin main
```
