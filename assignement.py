def hello_name(user_name):
    print("hello_"+user_name+"!")

def first_odds():
    for x in range(50):
        print(2*x+1)

def max_num_in_list(a_list):
    big = a_list[0]
    for x in list:
        if x > big:
            big = x
    return big

def is_leap_year(a_year):
    if a_year%4 == 0 and (a_year%100 != 0 or (a_year%100 == 0 and a_year%400 == 0)):
        leap = True
    else:
        leap = False
    return leap

def is_consecutive(a_list):
    prem = a_list[0]
    for x in range(len(a_list) - 1):
        if a_list[x + 1] == prem + 1:
            prem +=1
        else:
            return False
    if prem == a_list[-1]:
        return True





