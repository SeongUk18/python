import inspect
import sys

class StrategyInterface:
    def execute(self):
        raise NotImplementedError("Execute method must be implemented by the subclass.")

class ConcreteStrategyA(StrategyInterface):
    def execute(self):
        print("Executing Concrete Strategy A")

class ConcreteStrategyB(StrategyInterface):
    def execute(self):
        print("Executing Concrete Strategy B")

def is_strategy(cls):
    return inspect.isclass(cls) and issubclass(cls, StrategyInterface) and cls is not StrategyInterface

def find_strategies():
    strategies = []
    # inspect.getmembers 함수를 이용하여 현재 모듈의 멤버들을 검사
    for name, obj in inspect.getmembers(sys.modules[__name__], is_strategy):
        strategies.append(obj)
    return strategies

# 클라이언트 코드
strategies = find_strategies()
for strategy_class in strategies:
    strategy = strategy_class()
    strategy.execute()