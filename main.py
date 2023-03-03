import random as rd
import pandas as pd

EPS = 10 ** (-6)
a0 = b0 = g1 = g2 = 0
while g1 == 0 or g2 == 0 or a0 == 0 or b0 == 0:
    g1 = rd.random()
    g2 = (1-g1**2)**0.5
    a0 = rd.uniform(-10, 10)
    b0 = rd.uniform(-10, 10)


def f1(gamma):
    a = a0 + gamma*g1
    b = b0 + gamma*g2
    return (b + 1)**2 + (a + b + 2)**2 + (2*a + b + 4)**2 + (3*a + b - 1)**2 + (4*a + b + 3)**2


def f2(gamma):
    a = a0 + gamma*g1
    b = b0 + gamma*g2
    return abs(b + 1) + abs(a + b + 2) + abs(2*a + b + 4) + abs(3*a + b - 1) + abs(4*a + b + 3)


# дихотомия
aa = []
bb = []
ee = []
cc = []
dd = []
f1c = []
f1d = []
a = -10
b = 10
n = 0
while round((b - a) / 2, 6) > EPS:
    aa.append(round(a, 6))
    bb.append(round(b, 6))
    ee.append(round((b - a) / 2, 6))
    c = (a + b) / 2 - EPS / 2
    cc.append(round(c, 6))
    d = (a + b) / 2 + EPS / 2
    dd.append(round(d, 6))
    f1c.append(round(f1(c), 6))
    f1d.append(round(f1(d), 6))
    if round(f1(c), 6) >= round(f1(d), 6):
        a = c
    else:
        b = d
print(round((b + a) / 2, 6))

df = pd.DataFrame({'a': aa, 'b': bb, 'e': ee, 'c': cc, 'd': dd, 'f1c': f1c, 'f1d': f1d})
df.to_excel('dih_f1.xlsx')

aa = []
bb = []
ee = []
cc = []
dd = []
f1c = []
f1d = []
a = -10
b = 10
while round((b - a) / 2, 6) > EPS:
    aa.append(round(a, 6))
    bb.append(round(b, 6))
    ee.append(round((b - a) / 2, 6))
    c = (a + b) / 2 - EPS / 2
    cc.append(round(c, 6))
    d = (a + b) / 2 + EPS / 2
    dd.append(round(d, 6))
    f1c.append(round(f1(c), 6))
    f1d.append(round(f1(d), 6))
    if round(f2(c), 6) >= round(f2(d), 6):
        a = c
    else:
        b = d
print(round((b + a) / 2, 6))

df = pd.DataFrame({'a': aa, 'b': bb, 'e': ee, 'c': cc, 'd': dd, 'f1c': f1c, 'f1d': f1d})
df.to_excel('dih_f2.xlsx')

# золотое сечение
aa = []
bb = []
ee = []
cc = []
dd = []
f1c = []
f1d = []
a = -10
b = 10
z = (3 - 5**0.5)/2
c = a + z * (b - a)
d = b - z * (b - a)
while round((b - a) / 2, 6) > EPS:
    aa.append(round(a, 6))
    bb.append(round(b, 6))
    ee.append(round((b - a) / 2, 6))
    cc.append(round(c, 6))
    dd.append(round(d, 6))
    f1c.append(round(f1(c), 6))
    f1d.append(round(f1(d), 6))
    if round(f1(c), 6) >= round(f1(d), 6):
        a = c
        c = d
        d = b - z * (b - a)
    else:
        b = d
        d = c
        c = a + z * (b - a)
print(round((b + a) / 2, 6))

df = pd.DataFrame({'a': aa, 'b': bb, 'e': ee, 'c': cc, 'd': dd, 'f1c': f1c, 'f1d': f1d})
df.to_excel('zs_f1.xlsx')

aa = []
bb = []
ee = []
cc = []
dd = []
f1c = []
f1d = []
a = -10
b = 10
c = a + z * (b - a)
d = b - z * (b - a)
while round((b - a) / 2, 6) > EPS:
    aa.append(round(a, 6))
    bb.append(round(b, 6))
    ee.append(round((b - a) / 2, 6))
    cc.append(round(c, 6))
    dd.append(round(d, 6))
    f1c.append(round(f1(c), 6))
    f1d.append(round(f1(d), 6))
    if round(f2(c), 6) >= round(f2(d), 6):
        a = c
        c = d
        d = b - z * (b - a)
    else:
        b = d
        d = c
        c = a + z * (b - a)
print(round((b + a) / 2, 6))

df = pd.DataFrame({'a': aa, 'b': bb, 'e': ee, 'c': cc, 'd': dd, 'f1c': f1c, 'f1d': f1d})
df.to_excel('zs_f2.xlsx')



