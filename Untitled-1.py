Pin = int (input("Введите каличество операций: "))
Nomber1 = float (input("Введите первое значение: "))

i = 0
while i < Pin:
    op = input("Введите операцию: ")
    if op == "+":
        Nomber2 = float (input("Введите значение: "))
        Nomber1 = Nomber1 + Nomber2
        print ("результат: ")
        print (Nomber1)
    elif op == "-":
        Nomber2 = float (input("Введите значение: "))
        Nomber1 = Nomber1 - Nomber2
        print ("результат: ")
        print (Nomber1)
    elif op == "*":
        Nomber2 = float (input("Введите значение: ")) 
        Nomber1 = Nomber1 * Nomber2
        print ("результат: ")
        print (Nomber1)

    elif op == "/":
        Nomber2 = float (input("Введите значение: "))
        if Nomber2 == 0:
            print ("ошибка на 0 делить нельзя")
        else:
            Nomber1 = Nomber1 / Nomber2
            print ("результат: ")
            print (Nomber1)    
    i+=1