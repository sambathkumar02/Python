class people:
    def __init__(self,name):
        self.name=name

    def __add__(self,other):
        print(self.name,'loves',other.name)

    def __sub__(self,other):
        print(self.name,'breakups',other.name)
boy=people('sambath')
girl=people('roshini')
boy+girl


