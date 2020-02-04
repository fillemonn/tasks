# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
# przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi


def generator(kod1, kod2):
    code_list = []
    kod1 = list(kod1)
    kod2 = list(kod2)
    kod1.pop(2)
    kod2.pop(2)
    k1 = int(''.join(kod1))
    k2 = int(''.join(kod2))
    for i in range(k1 + 1, k2):
        code_list.append(str(i)[0:2] + '-' + str(i)[2:])
    return code_list

print(generator('79-900', '80-155'))
