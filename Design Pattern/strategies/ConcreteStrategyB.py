from .strategy_interface import StrategyInterface

class ConcreteStrategyB(StrategyInterface):
    def execute(self):
        print("Executing ConcreteStrategyB")
