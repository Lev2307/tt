def build_field_letterY(user_num):
    field = ['_'] * user_num
    for i in range(user_num):
        if i != 0:
            field[i-1] = '_'
            field[user_num-i] = '_'
        if i > (user_num-2) / 2:
            field[int((user_num-1)/2)] = 'X'
        else:
            field[user_num-i-1] = 'X'
            field[i] = 'X'
        print(field)
    
build_field_letterY(7)