from sys import stdin

summa = 0
lst = []


def jump(point, count):
    global summa
    while count!=0:
        for line in range(point, len(lst)):
            if 'print' in lst[line]:
                summa+=int(lst[line].split(' ')[-1])
        count -= 1


def account(index):
    global summa
    if 'print' in lst[index]:
        summa += int(lst[index].split(' ')[-1])
    else:
        point = int(lst[index].split(' ')[-2])
        count = int(lst[index].split(' ')[-1])
        jump(point-1, count)
        lst[index] = 'jump {} {}'.format(point, 0)


for line in stdin:
    lst.append(line.replace('\n', ''))
    account(-1)
    print(summa)




