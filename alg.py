a = float(input)
b = float(input)
sigma = 0.001
max_step = 100
k = 0

def f(x): # если не использовать функцию f(x) теряеться смысл 
    return x * 3 + 3

while k < max_step and b - a > sigma:
    xm = (a + b) / 2

    if f(a) * f(xm) <= 0:
        b = xm
    else:
        a = xm

    k += 1

print(xm)
