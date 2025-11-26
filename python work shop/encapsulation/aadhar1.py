class Adhar:
    def __init__(self,Name,Adhar_no,age,dob,finger_print,retina):
        self.Name=Name
        self.Adhar_no=Adhar_no
        self.dob=dob
        self.age=age
        self._finger_print=finger_print
        self.__retina=retina

    def display_userData(self):
        print("------------------------------")
        print("\n---- Adhar Details ----")
        print("------------------------------")
        print(f"Name           : {self.Name}")
        print(f"Adhar_no       : {self.Adhar_no}")
        print(f"age            : {self.age}")
        print(f"dob            : {self.dob}")
        print(f"finger_print   : {self._finger_print}")
        print(f"retina         : {self.__retina}")
        print("------------------------------")

var=Adhar("pooja",545481545454165,22,"16-04-2003","fdaegdfdaeedgjyadgdf","kcgyfshghfhsgf")
var.display_userData()