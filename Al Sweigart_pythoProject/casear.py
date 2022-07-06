#암호화 or 복호화 입력 받기
menu =input("암호화를 하려면 e를 복호화를 하려면 d를 입력하세요")

symbol="ABCD"
ordDistance=26

#카이사르 암호 거리 입력 받기
distance= int(input("거리를 입력해주세요"))
#문자열 입력 받기
string = input("암호화할 문자열을 입력해주세요")
#아스키 코드 변환
def caesar(string,distance):
    secret=""
    for i in string:
        if(i==" "):
            secret+=" "
        else:
            ch=ord(i)+distance
            if(ch>ord("Z")):
                ch=ch-(ord("Z")-ord("A"))
                secret+=chr(ch)
            else:
                secret+=chr(ch)
    print(secret)

def decaesar(string,distance):
    secret=""
    for i in string:
        if(i==" "):
            secret+=" "
        else:
            ch=ord(i)-distance
            if(ch<65):
                ch=ch+26
                secret+=chr(ch)
            else:
                secret+=chr(ch)
    print(secret)

if(menu=="e"):
    caesar(string,distance)
elif(menu=="d"):
    decaesar(string,distance)

