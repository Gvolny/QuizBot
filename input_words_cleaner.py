
'''with open('test.txt',mode='r+') as file:
    for line in file:
        print(0)
        if not line.isspace():
            print(1)
            file.write(line)'''


def empty_string_cleaner():
    with open('ENGtoRU.txt') as f:
        lines = f.readlines()
        non_empty_lines = (
            line for line in lines if not line.isspace()
        )

        with open('ENGtoRU.txt', 'w') as n_f:
            n_f.writelines(non_empty_lines)





def numbers_cleaner():
    res_str = ''
    new = list()
    with open('ENGtoRU.txt') as f:
        lines = f.readlines()
        for s in lines:
            for elem in s:
                if not elem.isdigit() and elem != '.':  # remove digits and points
                    res_str += elem
            res_str = res_str.replace(' ', '')   # remove ' To '

            new.append(res_str)
            res_str = ''



    with open('ENGtoRU.txt', 'w') as n_f:
        n_f.writelines(new)


# empty_string_cleaner()
numbers_cleaner()