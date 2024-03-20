# class Pet:
#     def __init__(self, name):
#         self.name = name
#         self.age = 1
#         self.color = 'Black'
#
# class PetC(Pet):
#     pass
# def dis(self):
#     print(self.name, self.age, self.color)
#
# PetC = type('PetC', (Pet,), {'dis': dis})
#
# my_pet = PetC('Myrka')
# my_pet.dis()
# my_pet.age = 10
# my_pet.dis()
# my_pet.color = 'White'
# my_pet.dis()

def dis(self):
    for i in self.__dict__:
        print(i, self.__dict__[i])
Pet = type('Pet', (), {'dis': dis})
aaa = Pet()
aaa.name = 'bbb'
aaa.dis()
