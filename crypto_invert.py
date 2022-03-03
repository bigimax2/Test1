def decrypt(str_):
    str_numb = ''
    str_lett = ''
    for i in str_:
        if i.isalpha():
            str_lett += i
            str_numb += ' '
        else:
            str_numb += i
    list_num = list(map(int, str_numb.split()))
    return ''.join([l * n for l, n in zip(str_lett, list_num)])


s = 'K8D8Y9d4K4u2t9N15X3h1a20U10J6w8S13Y9I8O8o8U20o15n4P5E15j6S7D17p13v6M15y2Z7d1i1'
print(decrypt(s))



