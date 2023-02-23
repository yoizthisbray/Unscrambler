def unscrambler(scrambled):
    un_list = []
    for i in scrambled:
        if i not in "!@#$%^&*=,()":
            un_list.append(i)
    unscrambled = ""
    print(unscrambled.join(un_list))


def unit():
    unscrambler(input("Scrambled text: "))

#
unit()
