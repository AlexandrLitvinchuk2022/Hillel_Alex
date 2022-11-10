#inputed = input("Enter word: ")
#text = inputed.split(' ')
#print(text)
#print(text [2: 200:3])


## hh jj kk ll gg ff rr ss a  ee rrt
mix_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]
digits = []
for el in mix_list:
    if el.isdigit():
        digits.append(el)
    else:
        digits.append(-1)
gen_list = [el for el in mix_list if el.isdigit()]
gen_list_ternary = [el if el.isdigit() else -1 for el in mix_list]
print(f"{digits=}")
print(f"{gen_list=}")
print(f"{gen_list_ternary=}")
