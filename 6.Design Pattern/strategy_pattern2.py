from typing import List, Callable

# 정렬 전략을 함수로 정의
def quick_sort(dataset: List[int]) -> List[int]:
    if len(dataset) <= 1:
        return dataset
    pivot = dataset[len(dataset) // 2]
    left = [x for x in dataset if x < pivot]
    middle = [x for x in dataset if x == pivot]
    right = [x for x in dataset if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def bubble_sort(dataset: List[int]) -> List[int]:
    n = len(dataset)
    for i in range(n):
        for j in range(0, n-i-1):
            if dataset[j] > dataset[j+1]:
                dataset[j], dataset[j+1] = dataset[j+1], dataset[j]
    return dataset

# 정렬 함수를 인자로 받는 고차 함수
def sort_dataset(dataset: List[int], strategy: Callable[[List[int]], List[int]]) -> List[int]:
    return strategy(dataset)

# 클라이언트 코드
dataset = [3, 5, 2, 9, 1]
sorted_data = sort_dataset(dataset, quick_sort)
print("Quick Sort:", sorted_data)

sorted_data = sort_dataset(dataset, bubble_sort)
print("Bubble Sort:", sorted_data)