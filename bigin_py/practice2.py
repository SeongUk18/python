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


