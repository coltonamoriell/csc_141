#
# Colton Amoriell
# Difficulty 6/10
#


tickets = True
while tickets:
    age_of_person = input("how old are you?: ")
    if age_of_person == 'quit':
        break
    elif int(age_of_person) < 3:
        print('You can watch the movie for free.')
    elif int(age_of_person) >= 3 and int(age_of_person) <= 12:
        print('Your ticket price is $10.')
    else:
        print('Your ticket price is $15.')