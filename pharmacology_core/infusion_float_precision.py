# ICU Patient profiles needing precise infusion rate verification
icu_patients = [
    {
        "patient_id": "ICU-001",
        "weight_kg": 72.5,
        "dose_mcg_kg_min": 0.1,
        "concentration_mg_ml": 4.0,
        "target_rate": 0.10875
    },
    {
        "patient_id": "ICU-002",
        "weight_kg": 85.0,
        "dose_mcg_kg_min": 0.15,
        "concentration_mg_ml": 4.0,
        "target_rate": 0.19125
    }
]

def calculate_infusion_rate(weight_kg, dose_mcg_kg_min, concentration_mg_ml) :
    infusion_rate = ((weight_kg * dose_mcg_kg_min) / (concentration_mg_ml * 1000)) * 60
    return infusion_rate

def verify_pump_tolerance(calculated_rate, target_rate, tolerance) :
    return abs(calculated_rate - target_rate) < tolerance

for patient in icu_patients :
    calculated_rate = calculate_infusion_rate(patient["weight_kg"], patient["dose_mcg_kg_min"], patient["concentration_mg_ml"])
    if verify_pump_tolerance(calculated_rate, patient['target_rate'], 1e-5) :
        Check = "PASSED"
    else :
        Check = "FAILED"
    print(f"Patient {patient['patient_id']}: Calculated Rate = {calculated_rate:.4f} | Safety Check: {Check}")
