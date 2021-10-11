from typing import Sized
import pandas as pd
import datetime 
import numpy as nm
from matplotlib import pyplot as plt

hamma= pd.read_csv('C:\\Users\\HP PAVILION GAMING\\Desktop\\15 сент 2021\\birlashgan.csv')
print(hamma)

plt.plot(hamma.year_zodiac, hamma.eco_frequency)
plt.plot(hamma.year_zodiac, hamma.lit_frequency)
plt.plot(hamma.year_zodiac, hamma.med_frequency)
plt.plot(hamma.year_zodiac, hamma.pe_frequency)
plt.plot(hamma.year_zodiac, hamma.ph_frequency)
plt.plot(hamma.year_zodiac, hamma.ch_frequency)
font1 = {'family':'serif','color':'blue','size':20}
plt.title('Nobel prize winners\' zodiacs of born year', fontdict = font1, loc = 'center')
plt.legend(['economy', 'literature', 'medicine', 'peace', 'phyzics', 'chemistry'], bbox_to_anchor=(0.9,1), loc="upper left")
#plt.legend(bbox_to_anchor=(1.05,1))
plt.xlabel('zodiacs of year')
plt.xticks(rotation=90)
plt.ylabel('frequency')

ax = plt.subplot()
ax.grid(True)
plt.show()