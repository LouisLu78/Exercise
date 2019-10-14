
import matplotlib.pyplot as plt
import numpy as np

# x,y=np.loadtxt('C:/Users/Basanwei/eclipse-workspace/pydata/test.TXT',
#                delimiter=',',
#                unpack=True)
# plt.plot(x,y,label='ZnO83')
# plt.xlabel('Wavenumber')
# plt.ylabel('Intensity')
# plt.title('Raman spectrum of Zinc Oxide of Sample ZnO83')
# plt.legend()
# plt.show()

import pandas as pd
data1=pd.read_csv('GL100108a.csv')
print(data1)
'''This is the fluorescence result of my sample which I synthesized in MPIP Lab, Germany. 
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

number=data1.a.iloc[100]
print(number)
x=data1.a
y=data1.b
plt.xlabel('Wavelength(nm)')
plt.ylabel('Intensity(a.u.)')
plt.title('Fluorescence of ZnCoO')
plt.plot(x,y)


plt.legend()
plt.show()