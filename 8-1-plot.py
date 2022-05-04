import numpy as np
import matplotlib.pyplot as plt

#with open("settings.txt", "r") as settings:
#    tmp = [float(i) for i in settings.read().split("\n")]

tmp = [9.06, 1289.06]

sett_array = np.loadtxt("settings.txt", dtype = float)
data_array = np.loadtxt("data.txt", dtype = float)

data_array *= sett_array[1] / 1000

x = [0] * len(data_array)

for i in range(len(data_array)):
    x[i] = i / sett_array[0]

y = data_array

fig, ax = plt.subplots(figsize=(16, 10), dpi = 400)

ax.grid(
        color = 'gray',
        linewidth = 0.45,
        linestyle = 'dashed')

ax.minorticks_on()
ax.grid(which='minor',
        color = 'orange',
        linewidth = 0.25,
        linestyle = 'dashed')

ax.plot(x, y, '-b', markevery=15, marker = "s", label = 'Зависимость напряжения от времени')
ax.legend()
plt.xlim(0, 55)
plt.ylim(0, 4000)
ax.set_xlabel("Время, 0.1 с")
ax.set_ylabel("Напряжение, мВ")
ax.set_title("Процесс заряда и разряда в RC-цеопчке")

ax.text(10, 50, r'время зарядки=20.15 с, время разрядки=20 с', fontsize = 17)


fig.savefig("plot.png")