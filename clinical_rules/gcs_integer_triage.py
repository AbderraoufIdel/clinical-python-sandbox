# Raw Random Data
raw_trauma_cases = [
    {"patient_id": 701, "eye": 3, "verbal": 4, "motor": 5},   # Moderate injury
    {"patient_id": 702, "eye": 1, "verbal": 2, "motor": 3},   # Severe injury (GCS = 6)
    {"patient_id": 703, "eye": 4, "verbal": 5, "motor": 6},   # Fully conscious
]

def validate_scores(eye, verbal, motor) :
    if eye in range(1, 5) and verbal in range(1, 6) and motor in range(1, 7) :
        return True

def assess_airway_risk(patient_cases) :
    results = []

    for case in patient_cases :
        if not validate_scores(case["eye"], case["verbal"], case["motor"]) :
            results.append(f"Patient {case['patient_id']} | Invalid scores")
        elif sum([case["eye"], case["verbal"], case["motor"]]) <= 8 :
            results.append(f"Patient {case['patient_id']} : GCS = {sum([case['eye'], case['verbal'], case['motor']])} | Status: CRITICAL ALERT - Prepare for immediate intubation!")
        else :
            results.append(f"Patient {case['patient_id']} : GCS score is {sum([case['eye'], case['verbal'], case['motor']])} | Status: Monitor closely.")
    return results

print(assess_airway_risk(raw_trauma_cases))
