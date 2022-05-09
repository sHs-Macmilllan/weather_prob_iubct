import random
n = int(input("Enter the number of the cities : "))
hot = []
mild=[]
cool=[]
freezing=[]
x=0
list= []
while len(list)!=n:
    list.append(random.uniform(-15,45))
    x=x+1
print(list)
print()
h_counter  =0
m_counter =0
c_counter  =0
f_counter   =0
m=0
while m!=n:
    if  list[m]>=28 and list[m]<=45:
        hot.append(list[m])
        h_counter=h_counter+1
    elif  list[m]>=15 and list[m]<=27.9:
        mild.append(list[m])
        m_counter=m_counter+1
    elif  list[m]>=4 and list[m]<=14.9:
        cool.append(list[m])
        c_counter=c_counter+1
    elif  list[m]>=-15 and list[m]<=3.9:
        freezing.append(list[m])
        f_counter=f_counter+1
    m=m+1
        
print("Temp Category""                        ""Count""                                                                 ""List of temp in this category")
print("______________________________________________________________________________________________________________________________________________________________________________")
print()
print ("Hot",f"                                         {h_counter}                                                                      {hot}")
print ("Mild",f"                                        {m_counter}                                                                      {mild}")
print ("Cool",f"                                        {c_counter}                                                                      {cool}")