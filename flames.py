flames= 'flames'
def altering_fun(word,total_number,remo_letter):#to change the order of the letters
    rem_letter = remo_letter
    i=0;j=0;fin_value_fin=['','','','',''];
    while(rem_letter<total_number):
        fin_value_fin[i] = word[rem_letter];
        rem_letter = rem_letter+1 ;i = i+1
    #print(i)
    while(j<remo_letter):
        fin_value_fin[i]=word[j]
        j = j+1;i=i+1
    return ''.join(fin_value_fin)
def first_v(a_fin_value,a):
    a1 = a%6
    while 1:
            if (a1==0):
                a1=6;continue #if value is 0, removing value will be last one i.e 6
            elif(a1==1):
                f1 = a_fin_value[1:6] #if value is 1,
                return f1
            elif(a1==6):
                f1 = a_fin_value[:-1]
                return f1
            else:
                f1 = a_fin_value[0:(a1-1)]+a_fin_value[a1:6] 
                f1 = altering_fun(f1,5,(a1-1))
                return f1
def second_val(a_sec_value,a):
    a1 = a%5;#print(a1)
    while 1:
            if (a1==0):
                f1 = a_sec_value[0:4];
                return f1
            elif(a1==1):
                f1 = a_sec_value[1:5]
                return f1
            else:
                f1 = a_sec_value[0:(a1-1)]
                f2 = a_sec_value[(a1):5]
                f3 = f1 + f2;
                f3 = altering_fun(f3,4,(a1-1))
                return (f3)
def third_val(a_third_val,a):
    a1 = a%4;#print (a1)
    while 1:
            if (a1==0):
                f1 = a_third_val[0:3]
                return f1
            elif(a1==1):
                f1 = a_third_val[1:4]
                return f1
            else:
                f1 = a_third_val[0:(a1-1)]
                f2 = a_third_val[(a1):4]
                f3 = f1+f2
                f3 = altering_fun(f3,3,(a1-1))
                return (f3)
def four_val(a_four_val,a):
    a1 = a%3;#print (a1)
    while 1:
            if (a1==0): 
                f1 = a_four_val[0:2]
                return f1
            elif(a1==1):
                f1 = a_four_val[1:3]
                return f1
            else:
                f1 = a_four_val[0:(a1-1)]
                f2 = a_four_val[(a1):3]
                f3 = f1+f2
                f3 = altering_fun(f3,2,(a1-1))
                return f3
def five_val(a_five_val,a):
    a1 = a%2;#print (a1)
    if (a1%2==0):
        return(a_five_val[0])
    else:
        return(a_five_val[1])
first_name= raw_input("enter the first name")
second_name = raw_input("enter the second name");
first_name=''.join(first_name.split())
second_name=''.join(second_name.split())
if(first_name.isalpha() == True and second_name.isalpha() == True):
    pass
else:
    exit("sorry!! the name you entered has some other characters other than just letters" + "\ntry again")
tot = len(first_name+second_name);count = 0 #
for x in first_name:
    if x in second_name:
        count+=2;
global fin_value
fin_value = tot-count
a = fin_value
#print (fin_value)
f1 = first_v(flames,a);#print (f1)
f2 = second_val(f1,a);#print (f2)
f3 = third_val (f2,a);#print (f3)
f4 = four_val (f3,a);#print (f4)
f5 = five_val(f4,a);#print (f5)
if(f5 == 'f'):
    print("the relation between " + first_name + " and " + second_name + " is affection. sorry you are friendzoned xP!!");
elif(f5 == 'l' ):
    print ("you are lucky !! the relation you got is LOVE")
elif(f5 == 'a'):
    print("the relation between " + first_name +  " and " + second_name+ " is affection")
elif(f5== 'm'):
    print("have a good life!! you two are gonna get MARRIED soon")
elif(f5 == 'e'):
    print("sorry !!you got ENEMY :o")
elif(f5 == 's'):
    print ("worst friendzoned ever  hahaha!!,you two are SISTERS")
else:
    print ("your bad luck!!you got nothing bro")