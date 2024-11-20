# Patient Record Management System
# Spencer Kunz

# so I guess this is where we manage all those patient records huh
# wonder how that works

# I spose we're gonna start by making a BST
# Then we'll need some methods for populating it
# 

from binary_search_tree import BinarySearchTree, Node
from patient_record_mgmt import PatientRecord



class PatientRecord:
    def __init__(self, patient_id, name, age, diagnosis, blood_pressure,
                           pulse, body_temperature):
        
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.blood_pressure = blood_pressure
        self.pulse = pulse
        self.body_temperature = body_temperature

    # optional, a method for returning the patient record in a neat format
    def print_patient_record(self):

        print("Patient ID:       ", self.patient_id)
        print("Name:             ", self.name)
        print("Age:              ", self.age)
        print("Diagnosis:        ", self.diagnosis)
        print("Blood Pressure:   ", self.blood_pressure)
        print("Pulse:            ", self.pulse)
        print("Body Temperature: ", self.body_temperature)





class PatientRecordManagementSystem:

    def __init__(self):
        self.bst = BinarySearchTree()


    def add_patient_record(self, patient_id, name, age, diagnosis, blood_pressure,
                           pulse, body_temperature):
        
        new_patient_record = PatientRecord(patient_id, name, age, diagnosis,
                                           blood_pressure,pulse, body_temperature)
        
        # make a node with key=Patient_ID and value=new_patient_record
        new_node = Node(patient_id,new_patient_record)
        # insert the new node
        self.bst.insert(new_node)

        pass


    def search_patient_record(self, patient_id):
        return self.bst.search(patient_id)
    

    def delete_patient_record(self, patient_id):
        self.bst.remove(patient_id)


    def display_all_records(self):

        pass


    def build_tree_from_csv(self, file_path):

        pass


    def vizualize_tree(self):

        pass


    def _add_nodes(self):

        pass