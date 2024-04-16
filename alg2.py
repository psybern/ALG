a = float(input())
b = float(input())
k = 0
sigma = 0.001
max_step = 10

def f(x):
    return x * 3 + 3

for k in range(max_step):
    xm = (a + b) / 2

    if (b - a) < sigma:
        break

    if f(a) * f(xm) <= 0:
        b = xm
    else:
        a = xm

print(" приблизительный корень: ", xm)
