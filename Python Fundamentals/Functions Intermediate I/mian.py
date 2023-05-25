import random

def rand_num(min = 0 , max = 100):
    if max < min:
        temp = min
        min = max 
        max = temp
    return random.randint(min , max)


print ( rand_num())

print ( rand_num(max = 20))

print ( rand_num(min = 90))

print ( rand_num(min = -10 , max = -1))


def ran_nums (min = 0 , max = 100):
    number_rand = random.random()* (max - min ) + min
    rounded = round(number_rand)
    return rounded

print (ran_nums(min = 100 , max = 50))