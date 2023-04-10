import random
possible_symbols = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
password = ''
my_password = ''
print('Здравствуйте!')
print('Вы должны создать Google аккаунт!')
login = input('Введите свой логин: ')
mode_password = input('Вы хотите писать пароль 1.свой или 2.генерировать?')

if mode_password == '1':
  my_password = input('Введите свой пароль(минимум 4!): ')
  print('Ваш логин: ' + login)
  print('Ваш пароль: ' + my_password)
else:
  password_length = int(input('Введите длину пароля: '))
  for i in range(password_length):
    password += str(random.choice(possible_symbols))
  print('Ваш логин' + login)
  print('Ваш пароль: ' + password)