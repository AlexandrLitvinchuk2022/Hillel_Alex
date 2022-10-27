f_num = float(input('Enter the first operand: '))
s_num = float(input('Enter the second operand: '))
oper = input('What operator to execute?  ')
if oper == '+':
    print(f_num + s_num)
elif oper == '-':
    print(f_num - s_num)
elif oper == '*':
    print(f_num * s_num)
elif oper == '/':
    print(f_num / s_num)
elif oper == '**':
    print(f_num ** s_num)
else:
    print('What are you doing?')



