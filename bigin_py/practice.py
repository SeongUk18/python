string =" 1,2 , 3,4,5"
string_list= string.split(',')
i=0
l=0
string_list2=[]
string_list3=[]
while i<len(string_list):
    string_list2.append(string_list[i].strip())
    i = i+1
print(string_list2)

for k in range(len(string_list)):
    string_list3.append(string_list[k].strip())
    
print(string_list3)