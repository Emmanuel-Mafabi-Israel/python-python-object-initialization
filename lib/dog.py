# GLORY BE TO GOD,
# PYTHON PROGRAMMING - PYTHON - INSTANCE METHODS
# BY ISRAEL MAFABI EMMANUEL

class Dog:
    # class constructor
    def __init__(self, name:str, breed:str = "Mutt"):
        self.name  = name
        self.breed = breed
    
    def sit(self):
        print("The dog is sitting.")

    def bark(self):
        print("Woof!")