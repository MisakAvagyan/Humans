def l_u_d_s(st):
    l, u, d, s = False, False, False, False
    for i in st:
        if i.isupper():
            u = True
        elif i.islower():
            l = True
        elif i.isdigit():
            d = True
        elif not st.isalnum():
            s = True
    return l, u, d, s


def check(st, l, u, d, s):
    if len(st) >= 8:
        if l == True and u == True and d == True and s == True:
            return 'Strong password'
        elif l == True and d == True and s == True:
            return 'Medium password'
        elif l == True and u == True and s == True:
            return 'Medium password'
        elif l == True and d == True:
            return 'Medium password'
    if len(st) < 8:
        if l == True and d == True and s == True:
            return 'Weak password'
        return 'Weak password'


def main():
    st = 'Hello123'
    l, u, d, s = l_u_d_s(st)
    result = check(st, l, u, d, s)
    print(result)


if __name__ == '__main__':
    main()
