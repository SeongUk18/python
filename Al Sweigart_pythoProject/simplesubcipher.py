import random

def randomString():
    stringAZ=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    random.shuffle(stringAZ)
    stringAZ="".join(stringAZ)
    print("랜덤키는 : ",stringAZ)
    return stringAZ

def changeString(string,password):
    stringAZ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    word=""
    for i in string:
        if(i==" "):
            word+=" "
        else:
            for j in range(len(stringAZ)):
                if(i==stringAZ[j]):
                    word+=password[j]
    return word

def changeKey(string,password):
    stringAZ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    word=""
    for i in string:
        if(i==" "):
            word+=" "
        else:
            for j in range(len(password)):
                if(i==password[j]):
                    word+=stringAZ[j]
    return word

menu =input("암호화를 하려면 e를 복호화를 하려면 d를 입력하세요")
password=input("key를 입력해주세요 random작성시 랜덤으로 생성")
string = input("암호화할 문자열을 입력해주세요")

if(menu=="e"):
    if(password=="random"):
        password=randomString()
    print(changeString(string,password))
elif(menu=="d"):
    print(changeKey(string,password))
