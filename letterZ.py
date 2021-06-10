def build_field_letterZ(user_num):
    field = ['_'] * user_num
    for r in range(user_num):
        field = ['_'] * user_num
        if r == 0 or r == user_num-1:
            field = ['X'] * user_num
        else:
            field[user_num-r-1] = 'X'
            field[user_num-r] = '_'
        print(field)

build_field_letterZ(5)