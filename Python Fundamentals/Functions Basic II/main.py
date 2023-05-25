emptylist = []
def countsDown(x):
    for i in range (x , -1 , -1):
        emptylist.append(i)
    return emptylist

print (countsDown(10))


def print_and_return(list_two):
    print(list_two[0])
    return(list_two[1])

print_and_return([4,2])


def sumList(list_one):
    sum = list_one[0] + len(list_one)
    return sum

print(sumList([1,2,3,4,5,6]))


list_four = []
def كريم (List_three):
    for i in range(len(List_three)):
        if List_three[i] > List_three[1]:
            list_four.append(List_three[i])
    return list_four


print(كريم([5, 2, 3, 2, 1, 4]))

list_five = []
def Length_Value(size , value):
    for i in range (0 , size , 1):
        list_five.append(value)
    return list_five

print(Length_Value(5,5))