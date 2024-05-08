class StrategyInterface:
    def execute(self):
        raise NotImplementedError("Execute method not implemented.")

class ConcreteStrategyA(StrategyInterface):
    def execute(self):
        print("Executing strategy A")

class ConcreteStrategyB(StrategyInterface):
    def execute(self):
        print("Executing strategy B")

class StrategyContext:
    def __init__(self, strategy_name):
        strategy_class = globals().get(strategy_name)
        if strategy_class:
            self.strategy = strategy_class()
        else:
            raise ValueError(f"Strategy {strategy_name} not found")

    def execute_strategy(self):
        self.strategy.execute()

# 클라이언트 코드
if __name__ == "__main__":
    strategy_context = StrategyContext('ConcreteStrategyA')
    strategy_context.execute_strategy()

    strategy_context = StrategyContext('ConcreteStrategyB')
    strategy_context.execute_strategy()