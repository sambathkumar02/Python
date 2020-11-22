from abc import ABC,abstractmethod

class abstract(ABC):
    @abstractmethod
    def show(self):
        pass

class simple(abstract):
    def show(self):
        print('hi this is sambath..')

s=simple()
s.show()