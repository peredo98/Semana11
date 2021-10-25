from abc import ABCMeta, abstractstaticmethod

class IObservable(metaclass=ABCMeta):
    @abstractstaticmethod
    def attach(self, observer):
        """ Interface Method"""

    @abstractstaticmethod
    def detach(self, observer):
        """ Interface Method"""

    @abstractstaticmethod
    def notify(self):
        """ Interface Method"""

class IObserver(metaclass=ABCMeta):
    @abstractstaticmethod
    def update(self):
        """ Interface Method"""

class District(IObservable):
    visualizators = []

    def __init__(self, name):
        self.name = name
        self.votes = {
            "blue": 0,
            "yellow": 0,
            "green": 0,
            "red": 0
        }

    def attach(self, observer):
        self.visualizators.append(observer)

    def detach(self, observer):
        self.visualizators.remove(observer)
    
    def notify(self):
        for v in self.visualizators:
            v.update()
    
    def print_votes(self):
        print(self.name)
        print(self.votes)
    
    def add_vote(self, party_name):
        self.votes[party_name] += 1
        self.notify()

class Visualizator(IObserver):
    def __init__(self, observable):
        self.observable = observable
    
    def update(self):
        self.observable.print_votes()

class IMap(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_data(self, districts):
        """ Interface Method"""
    
class MapSingleton(IMap):
    __instance = None
    districts = []
    visualizators = []

    @staticmethod
    def get_intance():
        if MapSingleton.__instance == None:
            MapSingleton([])
        return __instance

    def __init__(self, districts):
        if MapSingleton.__instance != None:
            raise Exception("Map cannot be instanciated more than once")
        else:
            for d in districts:
                v = Visualizator(d)
                d.attach(v)
                self.districts.append(d)
                self.visualizators.append(v)
                MapSingleton.__instance = self

    @staticmethod
    def get_data():
        for d in MapSingleton.__instance.districts:
            d.print_votes()

            

# Example
dist1 = District("Distrito 1")
dist2 = District("Distrito 2")
dist3 = District("Distrito 3")

m = MapSingleton([dist1,dist2,dist3])
print("Update")
dist1.add_vote("green")
print("Update")
dist2.add_vote("red")
print("Update")
dist3.add_vote("yellow")
print("Update")
dist3.add_vote("yellow")

print("Map Data")
m.get_data()