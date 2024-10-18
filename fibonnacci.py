input_data = open('input.txt', 'r') #открываем файлы
output_data = open('output.txt', 'w')
n = input_data.readline()
# Ввод первых  значений последовательности
a = 0
b = 1
# Вывод 2 значений последовательности через запятую
output_data.write(str(a))
output_data.write(", ")
output_data.write(str(b))
output_data.write(", ")
for i in range(2, int(n) + 1): # Входим в цикл
    a, b = b, a + b # Выводим в файл новое значение переменной b
    output_data.write(str(b))
    if i != (int(n)):
     output_data.write(", ")
input_data.close() #закрываем файлы
output_data.close()
