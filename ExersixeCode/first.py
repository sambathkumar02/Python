class car:
    def __init__(self,no,name):
        self.model_number=no
        self.model_name=name
    def display_model(self):
        print(self.model_number,self.model_name)
car1=car(12345,'lamboghini')
car1.display_model()

