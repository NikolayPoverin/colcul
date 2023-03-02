Pin = int (input("Если год вескасный введите 1 если нет введите 2: "))


sum = 0
sum1 = 0
kol1 = 0
kol2 = 0
kol3 = 0
kol4 = 0
kol5 = 0
kol6 = 0
kol7 = 0
kol8 = 0
kol9 = 0
kol10 = 0
kol11 = 0
kol12 = 0


if(Pin == 1):
    print ("год весакосный")
    for i in range(1,32):
        kol1 += int(i/10) + int(i%10)
    print ("Январь" )
    print (kol1)

    for i in range(1,30):
        kol2 += int(i/10) + int(i%10)
    print ("февраль")
    print (kol2)

    for i in range(1,32):
        kol3 += int(i/10) + int(i%10)
    print ("Март") 
    print (kol3) 

    for i in range(1,31):
        kol4 += int(i/10) + int(i%10)
    print ("Апрель")
    print (kol4)

    for i in range(1,32):
        kol5 += int(i/10) + int(i%10)
    print ("Май")
    print (kol5)

    for i in range(1,31):
        kol6 += int(i/10) + int(i%10)
    print ("Июнь")
    print (kol6)

    for i in range(1,32):
        kol7 += int(i/10) + int(i%10)
    print ("Июль")
    print (kol7)

    for i in range(1,32):
        kol8 += int(i/10) + int(i%10)
    print ("Август")
    print (kol8)

    for i in range(1,31):
        kol9 += int(i/10) + int(i%10)
    print ("Сентабрь")
    print (kol9)

    for i in range(1,32):
        kol10 += int(i/10) + int(i%10)
    print ("Октябрь")
    print (kol10)

    for i in range(1,31):
        kol11 += int(i/10) + int(i%10)
    print ("Ноябрь")
    print (kol11)

    for i in range(1,32):
        kol12 += int(i/10) + int(i%10)
    print ("Декабрь")
    print (kol12)

    print ("В году ")
    print (kol1 + kol2 + kol3 + kol4 + kol5 + kol6 + kol7 + kol8 + kol9 + kol10 + kol11 + kol12 )


        
        
    

elif(Pin == 2):
    print("год не весакосный")
    for i in range(1,32):
        kol1 += int(i/10) + int(i%10)
    print ("Январь" )
    print (kol1)

    for i in range(1,29):
        kol2 += int(i/10) + int(i%10)
    print ("февраль")
    print (kol2)

    for i in range(1,32):
        kol3 += int(i/10) + int(i%10)
    print ("Март") 
    print (kol3) 

    for i in range(1,31):
        kol4 += int(i/10) + int(i%10)
    print ("Апрель")
    print (kol4)

    for i in range(1,32):
        kol5 += int(i/10) + int(i%10)
    print ("Май")
    print (kol5)

    for i in range(1,31):
        kol6 += int(i/10) + int(i%10)
    print ("Июнь")
    print (kol6)

    for i in range(1,32):
        kol7 += int(i/10) + int(i%10)
    print ("Июль")
    print (kol7)

    for i in range(1,32):
        kol8 += int(i/10) + int(i%10)
    print ("Август")
    print (kol8)

    for i in range(1,31):
        kol9 += int(i/10) + int(i%10)
    print ("Сентабрь")
    print (kol9)

    for i in range(1,32):
        kol10 += int(i/10) + int(i%10)
    print ("Октябрь")
    print (kol10)

    for i in range(1,31):
        kol11 += int(i/10) + int(i%10)
    print ("Ноябрь")
    print (kol11)

    for i in range(1,32):
        kol12 += int(i/10) + int(i%10)
    print ("Декабрь")
    print (kol12)

    print ("В году ")
    print (kol1 + kol2 + kol3 + kol4 + kol5 + kol6 + kol7 + kol8 + kol9 + kol10 + kol11 + kol12 )


else:
    print("вы ввел и не верное значение")
