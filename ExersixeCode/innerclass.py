class mobile:
    def __init__(self,company,modelno):
        self.company=company
        self.modelno=modelno
        name=input('enter the os name:')
        version=input('enter the version:')
        self.osys=self.os(name,version)

    class os:
        def __init__(self,name,version):
            self.name=name
            self.version=version
    def show(self):
        print(self.company,self.modelno,self.osys.name,self.osys.version)

p1=mobile('apple','x12')
p1.show()



        