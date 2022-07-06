ordDistance=26

menu =input("암호화를 하려면 e를 복호화를 하려면 d를 입력하세요")
key= input("Key 값을 입력해주세요")
string = input("암호화할 문자열을 입력해주세요")


def vigenere(key):
    AZ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for index in range(len(AZ)):
        if(AZ[index]==key):
            return index
def checkIndex(string,index):
    index=index+1
    if(index==len(string)):
        index=index-len(string)

    return index

def encoding(string,key):
    secret=""
    stringIndex=0
    keyIndex=0
    while True:
        if(string[stringIndex]==" "):
            secret+=" "
            keyIndex=checkIndex(key,keyIndex)
            stringIndex=stringIndex+1
            
        else:
            ch=ord(string[stringIndex])+vigenere(key[keyIndex])
            if(ch>ord("Z")):
                ch=ch-ordDistance
                secret+=chr(ch)
                keyIndex=checkIndex(key,keyIndex)
                stringIndex=stringIndex+1
            else:
                secret+=chr(ch)
                keyIndex=checkIndex(key,keyIndex)
                stringIndex=stringIndex+1
            if(stringIndex==len(string)):
                break
    return secret

def decoding(string,key):
    secret=""
    stringIndex=0
    keyIndex=0
    while True:
        if(string[stringIndex]==" "):
            secret+=" "
            keyIndex=checkIndex(key,keyIndex)
            stringIndex=stringIndex+1
        else:
            ch=ord(string[stringIndex])-vigenere(key[keyIndex])
            if(ch<ord("A")):
                ch=ch+ordDistance
                secret+=chr(ch)
                keyIndex=checkIndex(key,keyIndex)
                stringIndex=stringIndex+1
            else:
                secret+=chr(ch)
                keyIndex=checkIndex(key,keyIndex)
                stringIndex=stringIndex+1
            if(stringIndex==len(string)):
                break
    return secret

if(menu=="e"):
    print(encoding(string,key))
elif(menu=="d"):
    print(decoding(string,key))

