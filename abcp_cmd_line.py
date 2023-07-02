# Army body fat; one touch tape test
def body_fat_men(waist, weight):
    return (-26.97 - (0.12 * weight) + (1.99 * waist))

def body_fat_female(waist, weight):
    return (-9.15 - (0.015 * weight) + (1.27 * waist))


print('Welcome to the new Army Body Fat Calculator')
gender = input('Are you a male or a female? ')
if gender == 'male'.lower():
    waist = int(input('Enter waist: '))
    weight = int(input('Enter weight: '))
    print(f'Your body fat is: {body_fat_men(waist, weight):.2f}%')
elif gender == 'female'.lower():
    waist = int(input('Enter waist: '))
    weight = int(input('Enter weight: '))
    print(f'Your body fat is: {body_fat_female(waist, weight):.2f}%')
else:
    print(f"Did not reconginize entry: '{gender}', try again.")



