import random 
station = "사당"

print("%s 행 열차가 들어오고 있습니다." %station)

date =random.randrange(4,29)

print("오프라인 모임 날짜는 %d 일로 선정되었습니다." %date)

siteName = "http://naver.com"
siteName2 = siteName[7:]
passwordSite=siteName2[:-4]

password = passwordSite[0:4]+str(len(passwordSite))+str(passwordSite.count("e"))+"!"
print(password)

comment = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random.shuffle(comment)
random.shuffle(comment)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : %d" %comment[0])
print("치킨 당첨자 : "+ str(comment[1:4]))
print("-- 축하합니다 --")


spendTime = [ random.randint(5,50) for i in range(1,51) ]
count = 0
for i in spendTime:
    if i<15:
        count = count +1
print("총 탑승 승객: {}".format(count))


def std_weight(height, gender):
    if gender=="여":
        return float(height*height*21)
    elif gender=="남":
        return float(height*height*22)
height = 175
gender = "남"
BMI = round(std_weight(height/100,gender),2)
print("키 {} 남자의 표준 체중은 {}kg 입니다.".format(height,BMI))

class House:
    def __init__(self, location, house_type, deal_type, price, completion_year) :
        self.location= location
        self.house_type= house_type
        self.deal_type= deal_type
        self.price=price
        self.completion_year=completion_year

    def show_detail(self):
        print("{4}년에 지어진 {0}에 위치한 {1}, {2}{3}".format(self.location, self.house_type, self.deal_type,self.price, self.completion_year))

building=[]
building1= House("강남","아파트","매매","10억",2010)
building2= House("마포","오피스텔","전세","5억",2007)
building3= House("송파","빌라","월세","500/50",2000)

building.append(building1)
building.append(building2)
building.append(building3)

for i in building:
    i.show_detail()


class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg=msg

    def __str__(self) :
        return self.msg

chicken = 10
waiting = 1
loop= 1

while(True):
   try:
       print("[남은 치킨: {0}]".format(chicken))
       order= int(input("치킨 몇마리 주문 하시겠습니까?:"))
       if order<1 :
           raise ValueError
       if order> chicken:
           print("재료가 부족합니다.")
           raise SoldOutError("재료가 소진되어 더 이상 주문을 받지 않습니다.")
       else:
            print("[대기번호{0}] {1} 마리 주문이 완료되었습니다.".format(waiting,order)) 
            waiting+=1
            chicken-=order
   except ValueError:
    print("잘못된 값을 입력하였습니다.")
   except SoldOutError:
    break
        