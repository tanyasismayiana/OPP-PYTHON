# class Student:
#     name="Tanyasis"
#     age= 21
#     country="Kenya"
#     school="Akirachix"
class Student:
    school="Akirachix"
    def __init__(self,name ,age,county,firstname,lastname):
        self.name=name
        self.age=age
        self.country=county
        self.firstname= firstname
        self.lastname=lastname
    def greet(self):
        return f"Hello{self.name} from {self.country}.Welcome to {self.school}"    


        
    def full_name(self):
        return f"your full name is {self.firstname} {self.lastname}"
        

    def initials(self):
        return f"your initials is {self.firstname[0]}.{self.lastname[0]}"




     

        
        


