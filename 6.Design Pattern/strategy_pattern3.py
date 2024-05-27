import importlib
from strategies.ConcreteStrategyA import ConcreteStrategyA
from strategies.ConcreteStrategyB import ConcreteStrategyB
from strategies.strategy_interface import StrategyInterface

class StrategyFactory:
    @staticmethod
    def get_strategy(strategy_name):
        try:
            module = importlib.import_module(f"strategies.{strategy_name}")
            strategy_class = getattr(module, strategy_name)
            return strategy_class()
        except (ImportError, AttributeError) as e:
            print(f"Error loading strategy {strategy_name}: {e}")
            return None

# 클라이언트 코드
strategy = StrategyFactory.get_strategy("ConcreteStrategyA")
if strategy:
    strategy.execute()
