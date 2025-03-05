
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printInfo(self):
        print(self.name, self.age)

if __name__ == "__main__":
    from animal.wild import Ant
    a = Ant("동학개미", 1000000)
    a.printInfo()