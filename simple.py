
input_data = open('input.txt','r')
output_data = open('output.txt','w')
data = input_data.read()
data = data.split()
a = int(data[0])

for i in range(2,25000):
    if a % i == 0 and i != a:
        output_data.write(str('N'))
        break
    elif i == a:
        output_data.write(str('Y'))
    if a == 1:
        output_data.write(str('N'))



input_data.close()
output_data.close()



