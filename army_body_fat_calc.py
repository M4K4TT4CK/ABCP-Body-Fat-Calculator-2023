# Army body fat; one touch tape test
def body_fat_men(waist, weight):
    first_step = (0.12 * weight)
    second_step = (1.99 * waist)
    return  (-26.97 - first_step) + second_step

def body_fat_female(waist, weight):
    first_step = (0.015 * weight)
    second_step = (1.27 * waist)
    return  (-9.15 - first_step) + second_step

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



