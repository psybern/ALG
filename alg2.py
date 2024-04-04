a = float(input())
b = float(input())
k = 0
sigma = 0.001
max_step = 10
f_a = a
f_b = b
xm = (a + b) / 2
for k in range(max_step):
    f_xm = xm
    if (b - a > sigma):

        print('Номер итерации: -- ', k)
    else:
        if f_a * f_b <= 0:
            b = xm
            f_b = f_xm
            print('Номер итерации, если ПЕРОВЕ условие не выполнено: -- ', k)
        else:
            a = xm
            f_a = f_xm
            print('Номер итерации, если ВТОРОЕ условие не выполнено: -- ', k)

print(xm)
