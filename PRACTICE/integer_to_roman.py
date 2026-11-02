'''num=int(input("Enter a number betwenn 1-3999 :"))
dic={1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}

roman=""
for i in range(3,-1,-1):
    quo=num//10**i
    rem=num%10**i
    temp=quo*(10**i)

    if quo==2 or quo==3 :
        roman+=dic.get(10**i)*quo
    elif quo==6 or quo==7 or quo==8 :
        roman=roman+dic.get(5*10**i)+(dic.get(10**i))*(quo-5)
    else:
        roman+=dic.get(temp)

    num=rem

print(f"It\'s Roman equivalent is {roman}")'''

dic={1:"I",2:"II",3:"III", 4:"IV", 5:"V",6:"VI",7:"VII",8:"VIII" ,9:"IX", 10:"X",20:"XX",30:"XXX", 40:"XL", 50:"L",60:"LX",70:"LXX",80:"LXXX", 90:"XC", 100:"C",200:"CC",300:"CCC", 400:"CD", 500:"D",600:"DC",700:"DCC",800:"DCCC", 900:"CM", 1000:"M",2000:"MM",3000:"MMM"}
num=3749
num=str(num)
roman=""
n=len(num)

for i in num:
    num_c=int(i)*10**(n-1)
    roman+=dic.get(num_c)
    n-=1
print(roman)