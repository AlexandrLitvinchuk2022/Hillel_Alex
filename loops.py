inputed = input("Enter word: ")
uppere_case = ''

gl_wodr = ''
digit_counter = 0
indexes =[]
for element in inputed:
    if element.isdigit():
        digit_counter +=1

        if digit_counter ==3:
            break

    else:
        if element.isupper():
            uppere_case += element

        if element in 'IOEAUYioeauy':
            gl_wodr += element

for  index, element in enumerate(inputed):
    #print(f'{index=} | {element=}')
    if element == " ":
        indexes.append(index)


print(uppere_case)
print(gl_wodr)
print(indexes)