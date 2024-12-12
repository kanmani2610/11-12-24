class student:
    id="she's a beauty"
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def display(self):
        print("Name=",self.__name)
        print("age=",self.__age)
name=input()
age=int(input())
s=student(name,age)
s.display()
print(s.id)