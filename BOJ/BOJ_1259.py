try:
    while True:
        in_str = input()
        if in_str == '0':
            break
        else:
            in_lst = list(in_str)
        
        reversed_lst = list(reversed(in_lst))
        if in_lst == reversed_lst:
            print('yes')
        else:
            print('no')
except:
    pass