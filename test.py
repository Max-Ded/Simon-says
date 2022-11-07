import winsound
import random
import matplotlib.pyplot as plt
from time import sleep

def son(N=10):
    f_s = 500
    f_l = 100
    L_s = []
    L_l = []
    L_o =[]
    for i in range(N):

        f_s= random.randint(f_s-30,f_s+30)
        f_l = random.randint(f_l-20,f_l+20)

        while f_s <40 or f_l < 50:

            f_s= random.randint(f_s-30,f_s+30)
            f_l = random.randint(f_l-20,f_l+20)

        L_s.append(f_s)
        L_l.append(f_l)
        winsound.Beep(f_s,f_l)
        sleep(f_l/1000)
        L_o.append(i)
    plt.subplot(1,2,1)
    plt.plot(L_o,L_s)
    plt.subplot(1,2,2)
    plt.plot(L_o,L_l)
    plt.show()