

weight = input('What is your weight?')
weight_user= f'{weight}'
print(weight_user)
print (type(weight_user))
weight_user_fl = float(weight_user)
print(weight_user_fl)
print (type(weight_user_fl))
weight_user_rd = round(weight_user_fl)
print("Round - ", weight_user_rd)

exponentiation = weight_user_rd ** 4
print(exponentiation)

square_root_1 = weight_user_rd ** 0.5
print (square_root_1)

square_root_2 = exponentiation ** 0.5
print (square_root_2)

division_remainder = weight_user_rd % 2
print('Remaider of division by 2 - ', division_remainder)