# # В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
#  Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

n = int(input('Введите количество учеников в классе а - '))
n1 = int(input('Введите количество учеников в классе б - '))
n2 = int(input('Введите количество учеников в классе с - '))



#print(n//2+n1//2+n2//2 + (n%2 !=0) + (n1%2 !=0) + (n2%2 !=0))
print((n+1)//2 + (n1+1)//2 + (n2+1)//2)


# if (n % 2 == 0):
#     m1 = n//2
# else: 
#     m1 = n//2 + 1

# if (n1 % 2 == 0):
#     m2 = n1//2
# else: 
#     m2 = n1//2 + 1

# if (n2 % 2 == 0):
#     m3 = n2//2
# else: 
#     m3 = n2//2 + 1
# print(m1 + m2 + m3)