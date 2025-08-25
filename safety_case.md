Functional Safety – Brake Fluid Warning System

1. Safety Goal
Ensure that the driver is warned if the brake fluid level drops below 20%, 
to maintain braking performance and to ensure that vehicle is controlled.

ASIL Target: ASIL B (medium severity, controllable by average driver)

2. Hazard Analysis
| Hazard ID | Hazard Description                   | Severity | Exposure | Controllability | ASIL  |
|-----------|--------------------------------------|----------|----------|-----------------|-------|
| H1        | Brake fluid low, no warning given    | High     | Medium   | Medium          | B     |
| H2        | False warning when fluid is normal   | Medium   | Medium   | High            | QM    |

3. Safety Requirements
 The system should turn ON brake warning light when fluid < 20%.
 The system should keep brake warning light OFF when fluid ≥ 20%.
 The system must perform self-check on every engine startup.

4. Safety Mechanisms
- Threshold check (20%).
- Unit test coverage to verify logic.
- Logging abnormal behavior (`test_log.txt`).

5. FMEA (Failure Modes & Effects Analysis)
Failure Mode |	Effect |  Detection |  Mitigation 
Sensor stuck at high value |  Warning not triggered |  Testcoverage, watchdog |  Redundantsensor
Sensor stuck at low value |	False warning |	Test coverage |	Cross-check (future)
Codelogicerror |	Warning not triggered |	Unit test, coverage |  Peerreview, CIpipeline