class WateringStrategy():

    def execute(self,amount: float)-> float:
        raise NotImplementedError 
    
class WateringStrategySaveUp(WateringStrategy):

    def execute(self,amount: float)-> float:
        print("Watering Strategy Save up used: only watering 80%")
        return round(amount * 0.823434,2)
    
class WateringStrategyNormal(WateringStrategy):

    def execute(self,amount: float)-> float:
        print("Watering Strategy normal used: watering 100%")
        return amount
