l = float(input("Введите начальное число: "))
s = float(input("Введите число которое получится при сложении: "))
e = int(input("Введите количество символов после запятой: "))
sum = 0 # задаем  значение 0 
a = 1 # Задаем значение 1
iteration  = 0 # Задаем  значение 0
s = float(round(s, e)) 
while sum + l < s: # задаем условие 
    sum += 1 / (a * a) #Считаем сумму последовательности 
    a = a + 1
    iteration += 1 # Считаем чиссло итераций 

if sum + l >= s:
   
    print("Число итераций =", iteration-1)