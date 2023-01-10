def hello_name(name):
    
    print("hello_"+name+"!")
hello_name('PIPI')

def first_odds():
    for x in range(50):
        print(2*x+1)
first_odds()

def max_num_in_list(list):
    big = int(list[0])
    for x in list:
        if int(x) > big:
            big = int(x)
    print(big)
max_num_in_list([1,2,7,3,7,2,6,3,7,8,4,8,8,3,23,423,65,73])

def is_leap(year):
    if year%4 == 0 and (year%100 != 0 or (year%100 == 0 and year%400 == 0)):
        leap = True
    else:
        leap = False
    print(leap)
    return leap

def is_consecutive(a_list):
    prem = a_list[0]
    for x in range(len(a_list) - 1):
        if a_list[x + 1] == prem + 1:
            prem +=1
        else:
            print(False)
            break
    if prem == a_list[-1]:
        print(True)
        return True
is_consecutive([3,4,5,6,7,8,9])


