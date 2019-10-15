
import matplotlib.pyplot as plt
import numpy as np

# x,y=np.loadtxt('GL100108a.TXT',
#                delimiter=',',
#                unpack=True)
# plt.plot(x,y,label='ZnCoO')
# plt.xlabel('Wavelength(nm)')
# plt.ylabel('Intensity(a.u.)')
# plt.title('Fluorescence of ZnCoO')
#
# plt.legend()
# plt.show()

import pandas as pd
data1=pd.read_csv('GL100108a.csv')
print(data1)
'''This is the fluorescence result of my sample which I synthesized in MPI-Polymer Lab, Germany.
The following is the sample&measurement information:
GL100108.SPC	Dateiname	Filename
Exitation (1)	Art	Type
ZnCoO169;powder;m440;s4,0/4,0;t0,5;RA;f=345z;150K	Kommentar	Comment
300.0000	Start	Start
410.0000	Ende	End
1.0000	Schrittweite	Increment
0.5000	Integrationszeit	Integration Time
440.0000	Feste Position	Position1
S/R	Signalart	Signal0
(mv)	Signaleinheit	SignalUnits0
4.0000	Spalt Anregung	slit6
4.0000	Spalt Emission	slit7
Guangqiang Lu P130 AK Wegner	Zusatzkommentar	setup path
Kein Wert	Korrekturdatei	correction0
950.0000	Hochspannung Signal	High Voltage 1
170.0000	Hochspannung Referenz	High Voltage 2
10.01.2006	Datum	date
15:50	Zeit	time
 111 	Anzahl	number of points
X-Wert	Y-Wert	Y-Norm

'''

number0=data1.a.iloc[100:110]
print(number0)
print(sum(number0))
# x=data1.a
# y=data1.b
plt.xlabel('Wavelength(nm)')
plt.ylabel('Intensity(a.u.)')
plt.title('Fluorescence of Zinc Cobalt Oxide')
# plt.plot(x,y,label='ZnCoO169')
# plt.legend()
# plt.show()
number=data1.iloc[3]
print(number)
number1=data1.iat[4,2]
print(number1)

# x=np.linspace(-10.0,9.0,num=50)
#
# y=x
# y1=x**2+2*x-1
# y2=x**3
# # plt.plot(x,y)
# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.show()

# x = np.arange(0, 10, 1)  # arange函数用于创建等差数组,arange返回一个array对象,第三个数代表的是步长
# plt.plot(x, 2*x)
# plt.plot(x, x/2)
# plt.plot(x, x**2)
# plt.show()

# x = np.arange(-np.pi, np.pi, 0.01)
# plt.plot(x, np.sin(x), x, np.cos(x))
# plt.grid(True)
# plt.show()

