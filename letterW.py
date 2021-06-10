def build_field_letterW(user_num):
    field = ['_'] * user_num
    for i in range(user_num):
        field[0] = 'X'
        field[-1] = 'X'
        if i != 0:
            field[i-1] = '_'
            field[user_num-i] = '_'
        if i > (user_num-2)/2:
            field[user_num-i-1] = 'X'
            field[i] = 'X'
        print(field)
    
build_field_letterW(7)