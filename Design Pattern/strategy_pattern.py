from abc import ABC, abstractmethod
from typing import List

# Strategy 인터페이스
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, dataset: List[int]) -> List[int]:
        pass

# ConcreteStrategy 1: 퀵 정렬
class QuickSort(SortStrategy):
    def sort(self, dataset: List[int]) -> List[int]:
        if len(dataset) <= 1:
            return dataset
        pivot = dataset[len(dataset) // 2]
        left = [x for x in dataset if x < pivot]
        middle = [x for x in dataset if x == pivot]
        right = [x for x in dataset if x > pivot]
        return self.sort(left) + middle + self.sort(right)

# ConcreteStrategy 2: 버블 정렬
class BubbleSort(SortStrategy):
    def sort(self, dataset: List[int]) -> List[int]:
        n = len(dataset)
        for i in range(n):
            for j in range(0, n-i-1):
                if dataset[j] > dataset[j+1]:
                    dataset[j], dataset[j+1] = dataset[j+1], dataset[j]
        return dataset

# Context
class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self.strategy = strategy

    def sort(self, dataset: List[int]) -> List[int]:
        return self.strategy.sort(dataset)

# 클라이언트 코드
dataset = [3, 5, 2, 9, 1]
sorter = Sorter(QuickSort())
print("Quick Sort:", sorter.sort(dataset))

sorter.set_strategy(BubbleSort())
print("Bubble Sort:", sorter.sort(dataset))