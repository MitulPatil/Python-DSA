class test:
    x=5     # class variable
    def __init__(self): # def __init__(object by which it is called)
        pass
    def __init__(self,a,b):   
        self.a=a    # instance variable
        self.b=b    # instance variable

t1=test(4,5)
t2=test(1,2)

print(t1.a,t1.b)
print(t2.a,t2.b)


class Test:
    x=5
    def __init__(self,a,b):   
        self.a=a    
        self.b=b    
    def show(self):
        print(self.a,self.b) 

    @staticmethod    
    def f2():
        print("hello") 

    @classmethod
    def f3(cls):
        print(cls.x)

t1=Test(3,4)
t2=Test(5,6)
t1.f2()
Test.f2()
t2.show()
t1.f3()
Test.f3()

class Employee:
    def __init__(self,empid=None,name=None,salary=None):
        self.empid=empid
        self.name=name
        self.salary=salary
    def setEmpid(self,empid):
        self.empid=empid    
    def setname(self,name):
        self.name=name    
    def setsalary(self,salary):
        self.salary=salary 
    def getEmpid(self):
        return self.empid       
    def getname(self):
        return self.name      
    def getsalary(self):
        return self.salary

t1 = Employee(1,'om',5000)
t2= Employee()
t2.setEmpid(2)
t2.setname('mitul')
t2.setsalary('100000')           

print(t1.getEmpid(),t1.getname(),t1.getsalary())        
print(t2.getEmpid(),t2.getname(),t2.getsalary())        
