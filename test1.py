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