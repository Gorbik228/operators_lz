
input_data = open('input.txt','r') # открываем файлы
output_data = open('output.txt','w')
data = input_data.read()
data = data.split()
a = int(data[0]) #вводим переменную

for i in range(2,25000): #сооздаем цикл
    if a % i == 0 and i != a:#задаем условие
        output_data.write(str('N'))
        break #завершаем цикл,если условие верно
    elif i == a:
        output_data.write(str('Y'))
    if a == 1:
        output_data.write(str('N'))#вводим полный ответ



input_data.close() #закрывыем файлы
output_data.close()



