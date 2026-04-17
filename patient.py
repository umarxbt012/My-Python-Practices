class Patient:
    def __init__(self, name,ailment,age):
        self.name=name
        self.age=age
        self.ailment=ailment
        self.admitted=False
    def admitPatient(self):
        self.admitted=True
        print(f"{self.name} has been admitted with an ailment of {self.ailment}")
    def dischargePatient(self):
        self.admitted=False
        print(f"{self.name} has been discharged successfully of the ailment of {self.ailment}. Wishing you good health!!")
    def getDetails(self):
        print("This is the patient's details:")
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Ailment:{self.ailment}")
        print(f"Admitted: {self.admitted}")
        
Patient1=Patient("John Doe","HIV",67)
Patient1.admitPatient()
Patient1.getDetails()
Patient1.dischargePatient()