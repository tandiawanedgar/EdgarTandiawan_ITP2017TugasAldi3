class room():
    def __init__(self,roomsize):
        self.roomsize = roomsize

class studio(room):
    def __init__(self):
        super(studio,self).__init__(1)
        self.size = 'studio'

class king(room):
    def __init__(self):
        super(king,self).__init__(2)
        self.size = 'king'

class president(room):
    def __init__(self):
        super(president,self).__init__(3)
        self.size = 'president'

class order():
    def __init__(self,hargastudio,hargaking,hargapresident):
        self.roomprice = {
            'studio' : hargastudio,
            'king' : hargaking,
            'president' : hargapresident
        }
        self.kamarstudio = 0
        self.kamarking = 0
        self.kamarpresident = 0

    def jumlahkamar(self):
        print('This is our avaible room :')
        cabe1 = str(input('studio = 300.000 \nking = 600.000 \npresident = 1.200.000 \npick your choice: ')).lower()
        if cabe1 == 'studio':
            self.kamarstudio += 1
            print('Do you want to do anything else?')
            u = str(input('input here: ')).lower()
            if u == 'yes':
                return order.jumlahkamar(self)
            elif u == 'no':
                return order.jumlahuang(self)
            else:
                print('only input yes or no')
                return order.jumlahkamar(self)
        elif cabe1 == 'king':
            self.kamarking += 1
            print('Do you want to do anything else?')
            u = str(input('input here: ')).lower()
            if u == 'yes':
                return order.jumlahkamar(self)
            elif u == 'no':
                return order.jumlahuang(self)
            else:
                print('only input yes or no')
                return order.jumlahkamar(self)
        elif cabe1 == 'president':
            self.kamarpresident += 1
            print('Do you want to do anything else?')
            u = str(input('input here: ')).lower()
            if u == 'yes':
                return order.jumlahkamar(self)
            elif u == 'no':
                return order.jumlahuang(self)
            else:
                print('only input yes or no')
                return order.jumlahkamar(self)
        elif cabe1 != 'studio' or cabe1 != 'king' or cabe1 != 'president':
            print('no room exist')
            return order.jumlahkamar(self)

    def jumlahuang(self):
        sabrina =self.kamarstudio*300000 + self.kamarking*600000 + self.kamarpresident*1200000
        print(sabrina)

ord = order(30000,60000,1200000)
ord.jumlahkamar()
