user = input('What is your name?')

hi_user = f'{user}' #приветствие
new_user = (hi_user.replace(" ", ''))
print(new_user)
print('Hello ', new_user.capitalize())


print('Qty of letters in name - ', len(new_user)) #  wiLLaM
print('Back to front - ',  user[::-1])