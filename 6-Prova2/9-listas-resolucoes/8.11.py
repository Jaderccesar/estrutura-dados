class PatientRecord:

    def __init__(self, patient_id, date, reason, treatment):
        self.patient_id = patient_id
        self.date = date
        self.reason = reason
        self.treatment = treatment
    
    def __hash__(self):
        return hash((self.patient_id, self.date))
    
    def __eq__(self, other):
        return self.patient_id == other.patient_id and self.date == other.date

    def __str__(self):
        return (
            f"Paciente: {self.patient_id} | "
            f"Data: {self.date} | "
            f"Motivo: {self.reason} | "
            f"Tratamento: {self.treatment}"
        )
    
# p1 = PatientRecord(
#     101,
#     "20/05/2026",
#     "Dor de cabeça",
#     "Paracetamol"
# )

# p2 = PatientRecord(
#     102,
#     "21/05/2026",
#     "Gripe",
#     "Repouso e Hidratação"
# )

# print(p1)
# print(p2)

# print("Hash p1:", hash(p1))
# print("Hash p2:", hash(p2))

class PatientDataBase:

    def __init__(self):
        self.records = {}

    def add_record(self, record):
        key = (record.patient_id, record.date)
        self.records[key] = record

    def get_reason(self, patient_id, date):
        key = (patient_id, date)

        if key in self.records:
            return self.records[key].reason
        
        return "Registro não encontrado"
    
    def get_treatment(self, patient_id, date):
        key = (patient_id, date)

        if key in self.records:
            return self.records[key].treatment
        
        return "Registro não encotrado"
    
    def show_records(self):
        for record in self.records.values():
            print(record)

db = PatientDataBase()

p1 = PatientRecord(
    101,
    "20/05/2026",
    "Dor de cabeça",
    "Paracetamol"
)

p2 = PatientRecord(
    102,
    "21/05/2026",
    "Gripe",
    "Repouso e hidratação"
)

p3 = PatientRecord(
    101,
    "25/05/2026",
    "Febre",
    "Ibuprofeno"
)

db.add_record(p1)
db.add_record(p2)
db.add_record(p3)

print("=== REGISTROS ===")
db.show_records()

print("\n=== CONSULTAS ===")

print(
    db.get_reason(101, "20/05/2026")
)

print(
    db.get_treatment(101, "25/05/2026")
)