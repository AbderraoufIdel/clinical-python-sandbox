# Electronic Health Record (EHR) snapshot of incoming emergency patients

emergency_patients = [
    {
        "patient_id": "P-101",
        "temp_c": 38.9,   # High (>38.0)
        "hr": 95,         # High (>90)
        "rr": 24,         # High (>20)
        "wbc": 11.0       # Normal (between 4.0 and 12.0)
    },
    {
        "patient_id": "P-102",
        "temp_c": 36.8,   # Normal
        "hr": 72,         # Normal
        "rr": 16,         # Normal
        "wbc": 6.5        # Normal
    },
    {
        "patient_id": "P-103",
        "temp_c": 39.1,   # High (>38.0)
        "hr": 85,         # Normal
        "rr": 18,         # Normal
        "wbc": 14.2       # High (>12.0)
    }
]

def evaluate_sirs_criteria(temp_c, hr, rr, wbc) :

    return [temp_c < 36 or temp_c > 38, hr > 90, rr > 20, wbc > 12 * 10e9 or wbc < 4 * 10e9]

# for patient in emergency_patients:
#     print(list(patient.values())[1:5])
#
def screen_patient_sepsis(vitals_list) :
    return sum(evaluate_sirs_criteria(*vitals_list)) >= 2

for patient in emergency_patients :
    result = "POSTIVE (Trigger Alert)" if screen_patient_sepsis(list(patient.values())[1:5]) else "NEGATIVE (Routine Monitor)"
    print(f"{patient['patient_id']}: SIRS Score = {sum(evaluate_sirs_criteria(*list(patient.values())[1:5]))} | Sepsis Screen: {result}")
