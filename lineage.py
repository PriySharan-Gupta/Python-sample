class Family:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def welcome_family(self):
        print(f"Dear {self.name}, welcome to Gupta Family")
                
fam = Family("PDG",5,"Male")
print(fam.name)
print(fam.age)
print(fam.gender)
fam.welcome_family()

class Child(Family):
    def __init__(self,name,age,gender,lineage):
        super().__init__(name,age,gender)
        self.lineage=lineage
    def intro_child(self):
        print(f"Dear {self.name}, welcome to Gupta Lineage Family")
        print(f"Dear {self.name}, you are in {self.lineage} s Family")
chld = Child("Vivek",39, "Male","PrabhuDayal")  
chld.welcome_family()   
chld.intro_child() 

class GrandChildren(Child):
    def __init__(self,name,age,gender,lineage,gotra):
        super().__init__(name,age,gender,lineage)
        self.gotra = gotra
    def intro_grand_children(self):
        print(f"Dear {self.name}, welcome to Gupta Lineage+1 Family") 
        print(f"Dear {self.name}, welcome to {self.gotra}")  
grandchldren = GrandChildren("Viththal",5,"Male", "Vivek","Bhaisanwar Family")  
grandchldren.welcome_family()   
grandchldren.intro_child() 
grandchldren.intro_grand_children()
