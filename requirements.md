Brake Warning Light – Requirements Document

1. Problem Summary
The driver has no direct way of knowing when brake fluid is critically low.
If the fluid goes below a safe level, it can affect braking performance and safety.
The system should automatically warn the driver through a warning light.

2. Scope
In Scope:
- Monitoring brake fluid level with a sensor
- Comparing the fluid level against a threshold (20%)
- Switching the brake warning light ON or OFF based on the reading

Out of Scope:
- Integration with ABS or other ECU systems
- Predictive maintenance or leak detection
- Detailed diagnostics beyond ON/OFF light indication

3. Objectives
- Alert the driver whenever brake fluid is less than 20%
- Prevent false alarms when fluid is within the safe range
- Make sure the light reacts quickly to sensor value changes

4. Functional Requirements
FR-01: System shall read the brake fluid level from the sensor
FR-02: System shall compare the fluid level with the threshold of 20%
FR-03: System shall turn ON the warning light when the fluid level is less than 20%
FR-04: System shall keep the warning light OFF when the fluid level is 20% or higher

5. Non-Functional Requirements
NFR-01: Light status should update within 1 second of sensor change
NFR-02: System should work in the temperature range -20°C to +70°C
NFR-03: Accuracy of the fluid sensor readings should be within ±2%

6. Constraints
- Implementation will be done on an embedded ECU (C language)
- Must follow automotive functional safety standards
- Limited by the vehicle’s existing power supply and wiring

7. Assumptions
- Brake fluid sensor provides data in percentage
- Only one brake fluid level sensor exists
- Power supply is stable when ignition is ON

8. Acceptance Criteria
- Warning light turns ON when fluid level is 19% or lower
- Warning light stays OFF when fluid level is 20% or higher
- Status change happens in under 1 second
- System performs correctly in environmental testing conditions
