def bigger_size(list_one):
    for i in range (len(list_one)):
        if list_one[i] >= 1:
            list_one[i] ="big"
    return list_one

print (bigger_size([-1,4,5,-2]))



import random
def count_positives(list_two):
    list_two[ len(list_two)-1] = random.randint (1,9)
    return list_two

print(count_positives([1,2,3,4,-5]))




def sum_total (list_three):
    x = 0
    for i in range (len(list_three)):
        x = x + list_three[i] 
    return x

print(sum_total([1,2,3,4]))



def average(list_four):
    sum = 0
    for i in range (len(list_four)):
        sum = sum + list_four[i]
    return sum/len(list_four)

print(average([1,2,3,4]))



def length (list_five):
    return len(list_five)

print (length([1,2,3,4]))



def minimum (list_six):
    if list_six == []:
        return False
    else:
        count = 0
    for i in range (len(list_six)):
        if list_six[count] > list_six[i]:
            count = i
    return list_six[count]

print(minimum([]))


def maximum (list_seven):
    if list_seven == []:
        return False
    else:
        count = 0
    for i in range (len(list_seven)):
        if list_seven[count] < list_seven[i]:
            count = i
    return list_seven[count]

print(maximum([100,1,2,3,4,5]))



def Ultimate_analysis (list_eight):
    sum = 0
    min = 0
    max = 0
    for i in range (len(list_eight)):
        sum = sum + list_eight[i]

        avg = sum/len(list_eight)

        if list_eight [min] > list_eight[i]:
            min = i 
        
        if list_eight[max] < list_eight[i]:
            max = i
    return {"sumTital":sum , "average":avg , "Minimum":list_eight[min], "Maximum":list_eight[max], "Length": len(list_eight)}

print (Ultimate_analysis([1,2,3 ,-1]))


def reverse_list(list_nine):
    x = 0
    y = len(list_nine)-1 
    while (x < y):
        temp = list_nine[x]
        list_nine[x] = list_nine[y]
        list_nine[y] = temp
        x +=1
        y -= 1 
    return list_nine

print (reverse_list([1,2,3,4]))