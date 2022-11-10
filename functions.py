def multiply(start, end): # Створи функцію, яка приймає параметри start та end, підсумовує всі цілі числа від значення start до величини end включно. Якщо користувач задасть перше число більше, ніж друге, поміняй їх місцями
    return range(start, end+1)
start = int(input("Start: "))
end = int(input("End: "))
total = 0
numbers = range(start, end+1)
for number in numbers:
    total += number
print('Summa:', total)

######################

N = int(input("Enter numbers: ")) # Можем использовать N = (123456) ## Створи три функції, які обчислюють суму чисел у списку з while-циклом
summ = 0
while N !=0:
    p = N % 10
    summ = summ + p
    N = N // 10
print(summ)
#######################
a = [1,2,3,4] ##for-циклом
s =0
for item in a:
    if item !=0:
        s += item
print(s)

#############
#Створи функцію, яка відображає число секунд у вигляді дні:години:хвилини:секунди. Функція може прийняти число як рядок так і як ціле число.

i = 0 # Seconds # Проверка. Ввод 2000000
ii = 0 # Minutes
iii = 0 # Hours
iiii = 0 # Day
time_user = int(input('Enter qty seconds : '))

for q in range(time_user):

    i += 1
    #print ("QTY Seconds :", i )
    if(i % 60) == 0:
        ii += 1
        #print ("QTY Minutes :", ii )
    if(i % 3600) == 0:
        iii += 1
        #print("QTY Hours :", iii )
    if(i % 86400) ==0:
        iiii +=1
Seconds = i % 60
Minutes = ii % 60
Hours = iii % 60
Day = iiii % 24
print(Seconds)
print(Minutes)
print(Hours)
print(Day)
print("Days: ", Day,"Hours: ", Hours, "Minutes: ", Minutes,  "Seconds: ", Seconds)