import csv
import numpy
import matplotlib.pyplot as plt

def dataLuar():
    reader = csv.reader(open("DataTugas2.csv"), delimiter=",")
    x = list(reader)
    return numpy.array(x)

def fnaik (x, a, b):
    return ((x-a)/(b-a))
def fturun (x, a, b):
    return ((b-x)/(b-a))

def PendapatanGraph():
    plt.title('Pendapatan')
    plt.plot([0, 0.6, 1.1], [1, 1, 0], label="rendah")
    plt.plot([0.6, 1.1, 1.2, 1.6], [0, 1, 1, 0], label="sedang")
    plt.plot([ 1.1, 1.6, 2], [0, 1, 1], label="tinggi")
    plt.show()

def HutangGraph():
    plt.title('Hutang')
    plt.plot([0, 20, 40], [1, 1, 0], label="rendah")
    plt.plot([20, 40, 50, 70], [0, 1, 1, 0], label="sedang")
    plt.plot([50, 70, 100], [0, 1, 1], label="tinggi")
    plt.show()

def simpanData(Array):
    with open('BLT.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        x = 0
        spamwriter.writerows([Array])

#Pendapatan#
def pendapatan(x):
    PendapatanTinggi = 0
    PendapatanRendah = 0
    PendapatanSedang = 0

    if (x <= 0.6):
        PendapatanRendah = 1

    elif (x > 0.6 and x < 1.1):
        PendapatanRendah = fturun(x, 0.6, 1.1)
        PendapatanSedang = fnaik(x, 0.6, 1.1)

    if (x >= 1.1 and x < 1.2):
        PendapatanSedang = 1

    elif (x >= 1.2 and x < 1.6):
        PendapatanSedang = fturun(x, 1.2, 1.6)
        PendapatanTinggi = fnaik(x, 1.2, 1.6)

    elif (x >= 1.6):
        PendapatanTinggi = 1

    return PendapatanRendah, PendapatanSedang, PendapatanTinggi

def scores(Layak,TidakLayak):
    return ((Layak*60) - (TidakLayak*30) / (Layak+TidakLayak))

def hutang(x):
    HutangRendah = 0
    HutangSedang = 0
    HutangTinggi = 0
    if (x <= 20):
        HutangRendah = 1

    elif (x > 20 and x < 40):
        HutangRendah = fturun (x,20,40)
        HutangSedang = fnaik (x,20,40)

    elif (x >= 40 and x <= 50):
        HutangSedang = 1

    elif (x >= 50 and x < 70):
        HutangSedang = fturun (x,50,70)
        HutangTinggi = fnaik (x,50,70)

    elif (x >= 70):
        HutangTinggi = 1

    return HutangRendah, HutangSedang, HutangTinggi

def Kelayakan(Pendapatan, Hutang, ValueKelayakan):
    if (Pendapatan<=Hutang):
        if (Pendapatan>=ValueKelayakan):
            return Pendapatan
        else:
            return ValueKelayakan
    elif (Hutang<Pendapatan):
        if (Hutang>=ValueKelayakan):
            return Hutang
        else:
            return ValueKelayakan


def Perhitungan(pr, ps, pt, hr, hs, ht, l, tl):
    if (pr > 0.6):
        l = pr
    if (pr > 0 and hr > 0):
        l = Kelayakan(pr, hr, l)
    if (pr > 0 and hs > 0):
        l = Kelayakan(pr, hs, l)
    if (pr > 0 and ht > 0):
        l = Kelayakan(pr, ht, l)
    if (ps > 0 and hr > 0):
        tl = Kelayakan(ps, hr, tl)
    if (ps > 0 and hs > 0):
        l = Kelayakan(ps, hs, l)
    if (ps > 0 and ht > 0):
        l = Kelayakan(ps, ht, l)
    if (pt > 0 and ht > 0):
        l = Kelayakan(pt, ht, l)
    if (pt > 0 and hr > 0):
        tl = Kelayakan(pt, hr, tl)
    if (pt > 0 and hs > 0):
        tl = Kelayakan(pt, hs, tl)
    return l, tl


List = dataLuar()
x = 0
y = []
for i in List:
    print(x)
    if (i[0] != 'No'):
        h = hutang(float(i[2]))
        p = pendapatan(float(i[1]))
        per = Perhitungan(p[0], p[1], p[2], h[0], h[1], h[2], 0, 0)
        y.append([scores(per[0], per[1]), x])
    x+=1
y.sort()
x = 1
for i in y:
    print(x, i)
    x += 1
z = []
x = 100
while (x != 80):
    z.append(y[x - 1][1])
    x -= 1
print(z)
simpanData(z)
HutangGraph()