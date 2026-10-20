# Multiples of Ten
# Colton Amoriell
# Difficulty 6/10


while True: 
    chosen_number = input("what is your number?: ")
    yes_or_no = int(chosen_number) % 10
    if yes_or_no == 0:
       print (f'{chosen_number} is a multiple of ten')
    else:
        print(f'{chosen_number} is not a multiple of ten')