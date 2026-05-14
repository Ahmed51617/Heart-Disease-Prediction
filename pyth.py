from abc import ABCMeta,abstractmethod
class vehicle(metaclass=ABCMeta):
    count_v=0
    def __init__(self,model,distance,fuel_cost):
        self.model=model
        self.distance=distance
        self.__fuel_cost=fuel_cost
        vehicle.count_v+=1
    def get_cost(self):
        return self.__fuel_cost
    def set(self,new_fuel_cost):
        self.__fuel_cost=new_fuel_cost
    
       
    @staticmethod 
    def show_count() :
        print(f"Number of vehicle is : {vehicle.count_v}\n")
    
    @abstractmethod
    def calc_fuel_cost(self):
        pass
    def v_info(self) :
        pass
    

class van(vehicle):
    def __init__(self, model,distance,fuel_cost):
        super().__init__(model,distance,fuel_cost)
    def calc_fuel_cost(self):
        return (self.distance*self.get_cost()+100)
    def v_info(self) :
        print(f"The model : {self.model}\nThe distance is : {self.distance}\nthe fuel cost :{self.calc_fuel_cost()}\n")   

class car(vehicle):
    def __init__(self,model,distance,fuel_cost):
        super().__init__(model,distance,fuel_cost)
    def calc_fuel_cost(self):
        return (self.distance*self.get_cost())
    def v_info(self) :
        print(f"The model : {self.model}\nThe distance is : {self.distance}\nthe fuel cost :{self.calc_fuel_cost()}\n")   
vehicle.show_count()    
C=car("BMW",1000,50)
C.v_info()
v=van("toyta",2023,342)
v.v_info()
vehicle.show_count()
                

