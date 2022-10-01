from datetime import date
yearOfBirth = int(input('please tell your birth of year'))
currentYear=date.today().year
age = currentYear - yearOfBirth
print('your age is :', age)
