class grandfather:
    
    def smile(self):
        print('hahahaha...')
class father():
    def smile(self):
        print('ha..ha..ha..')
        
class son(grandfather,father):
    def __init__(self):
        print('from son init')
    def smile2(self):
        print('haaaaaah...')
        super().smile()



s=son()
s.smile2()

