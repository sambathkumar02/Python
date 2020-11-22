class hackers:
    broadcast_message='hello every one'
    def __init__(self,ip,mac):
        self.ip=ip
        self.mac=mac
        self.sucess()

    def contact(self):
        print('contacting....')
        print('Resolving ip ...',self.ip)
        print('conneting to mac ...',self.mac)

    @classmethod    
    def broadcast(cls):
        print('broadcasting msg to every one......')
        
    @staticmethod
    def sucess():
        print('hackers info stored')

h1=hackers('192.168.43.101','23:45:df:ed:34:56')
h1.contact()
hackers.broadcast()
