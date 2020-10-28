import sys
# import judete as j
# import luni as l
# import colors as c


def eroare():
    print('\n CNP-ul nu este valid')


# sys.stdout.write(c.GREEN)
cnp_test = '279146358279'
cnp = input('Introduceti CNP-ul Dvs:\n \n')
cnp_flag = True

# sys.stdout.write(c.RED)
while cnp_flag:
    try:
        type(cnp) == int
    except ValueError:
        eroare()

    S = cnp[0]
    AA = cnp[1:3]
    LL = cnp[3:5]
    ZZ = cnp[5:7]
    JJ = cnp[7:9]
    NNN = cnp[9:12]

    if len(cnp) == 13 and int(S) and int(AA) and int(ZZ) and int(LL) and int(JJ) and int(NNN) > 0:
        pass
    else:
        eroare()
        break
    if int(LL) < 12 and int(ZZ) < 31 and int(JJ) < 52:
        pass
    else:
        eroare()
        break

    cnp_test_sum = int(cnp[0])*int(cnp_test[0]) + int(cnp[1])*int(cnp_test[1]) + int(cnp[2])*int(cnp_test[2]) + int(cnp[3])*int(cnp_test[3]) + int(cnp[4])*int(cnp_test[4]) + int(cnp[5]) * \
        int(cnp_test[5]) + int(cnp[6])*int(cnp_test[6]) + int(cnp[7])*int(cnp_test[7]) + \
        int(cnp[8])*int(cnp_test[8]) + int(cnp[9]) * \
        int(cnp_test[9]) + int(cnp[10])*int(cnp_test[10]) + \
        int(cnp[11])*int(cnp_test[11])

    cnp_test_modulo = cnp_test_sum % 11

    # sys.stdout.write(c.GREEN)
    if int(cnp[-1]) == cnp_test_modulo:
        print('\n\n Cnp-ul este Valid!')
        # sys.stdout.write(c.CYAN)
        print('\n Sunteti nascut in anul {}, luna {}, in Judetul {}.\n'.format(int(AA), l.luni[int(LL)],
                                                                               j.judete[int(JJ)]))
        break
    else:
        # sys.stdout.write(c.RED)
        eroare()
        cnp_flag = False
    sys.stdout.write(c.RESET)

    print(cnp_test_modulo, int(cnp[-1]))