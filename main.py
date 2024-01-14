import random
digits = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890,./#;]=-!£[$%^&*+}~"'
number = int(input('How many digits do you want to be in your password? '))
print('Your Generated password is:', "".join(random.sample(digits, number)))

