x=float(input("Первое значение: "))
z=str(input("Оператор: "))
y=float(input("Второе значение значение: "))
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
