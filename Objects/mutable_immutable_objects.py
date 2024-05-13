# 가변 객체 전달
def modify_list(lst):
    lst.append(4)  # 기존 리스트 객체 변경

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # 출력: [1, 2, 3, 4]

# 불변 객체 전달
def modify_number(x):
    x += 10  # x는 새로운 객체를 참조하게 됨

num = 5
modify_number(num)
print(num)  # 출력: 5


