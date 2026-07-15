# Raw, unstructured HL7 PID segments pulled from a hospital admission feed
raw_hl7_feeds = [
    "PID|1|PT-9942^^^MRN|| SMITH ^  jane  ||19900824|F",
    "PID|2|PT-1053^^^MRN||AL-AMIN^yousef ||19831102|M",
    "PID|3|PT-3301^^^MRN||  O'CONNOR  ^ ryan||19750514|M"
]

def parser_hl7_pid(pid_segment) :
    return pid_segment.strip(' ').replace('^', '|').split('|')

def standardize_demographics(raw_pid_list) :
    data = []
    for pid_raw in raw_pid_list :
        data.append([parser_hl7_pid(pid_raw)[2], parser_hl7_pid(pid_raw)[7].strip(' ').title(), parser_hl7_pid(pid_raw)[8].strip(' ').title()])
    return data

for patient in standardize_demographics(raw_hl7_feeds) :
    print(f"ID: {patient[0]} | Name: {patient[1]}, {patient[2]}")
