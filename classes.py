class MyClass:
    def __init__ (this, name, age):
        this.name = name
        this.age = age
        
    def __str__(this):
        return f"{this.name}({this.age})"
    
    def printMyClass(this):
        print(f"here is the value of x in MyClass {this.name}")
    
newClass = MyClass("Mahmoud", 21)

newClass.printMyClass()

del newClass.name