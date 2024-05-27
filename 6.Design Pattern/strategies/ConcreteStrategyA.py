from .strategy_interface import StrategyInterface

class ConcreteStrategyA(StrategyInterface):
    def execute(self):
        print("Executing ConcreteStrategyA")
