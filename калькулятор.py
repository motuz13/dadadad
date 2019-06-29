import sys, datetime
def cont():
    h=input("Продолжить? ('Y'/'N') ")
    if h == 'n' or h == 'N' or h == 'н' or h == 'Н':
          sys.exit()
    elif h == 'y' or h == 'Y' or h == 'д' or h == 'Д':
        pass
    else:
        cont()
while True:
    a=str(input("Первое значение: "))
    z=str(input("Оператор: "))
    g=str(input("Второе значение значение: "))
    x=None
    y=None
    if a.find('.') != -1:
        x=float(a)
    elif a.isdigit():
        x=int(a)
    if g.find('.') != -1:
        y=float(g)
    elif g.isdigit():
        y=int(g)
    if z=='+':
        result=x+y
    elif z=='-':
        result=x-y
    elif z==pow:
        result=pow(x,y)
    elif z=='*':
        result=x*y
    elif y!=0:
        if z=='/':
            result=x/y
        elif z==div:
            result=x//y
        elif z==mod:
            result=x%y
    elif y==0:
        result="Деление на 0!"
    print("Результат вычислений =",result)
    f = open('Калькулятор.txt', 'a')
    f.write('[' + str(datetime.datetime.utcnow()) + ']' + ' | ' + str(x) + ' ' + z + ' ' + str(y) + ' = ' + str(result) + '\n')
    f.close()
    cont()
