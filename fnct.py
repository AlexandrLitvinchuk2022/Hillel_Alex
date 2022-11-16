####################### Fibonacci
def fib(n):
    if n ==1:
        return 1
    if n==2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))
######################### Функция с рекурсией_1
def listsum(numlist):
    thesum = 0
    for i in numlist:
        thesum = thesum + i
    return thesum
print(listsum([1,3,5,7,9]))



######################### Функция с рекурсией_2
def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])


print(listsum([1, 3, 5, 7, 9]))


########################### Декоратор
def main_decor(func_to_decor):
    print("Помидор")
    def warapper():
        print("Сир")
        func_to_decor()
        #print(" ")
    print("Мясо")
    return warapper


@main_decor
def main_func():
    print('Хлеб')

main_func()