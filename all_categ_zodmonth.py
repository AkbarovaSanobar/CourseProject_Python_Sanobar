
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
ggzm=pd.read_csv('C:\\Users\\HP PAVILION GAMING\\Desktop\\new\\my_data111.csv')
ggzm
      ID gender  win year  ... zod_year    zod_month          zod all
0    198   male      1938  ...      rat  sagittarius  rat sagittarius
1    211   male      1950  ...    tiger       cancer     tiger cancer
2    208   male      1948  ...    tiger          leo        tiger leo
3    269   male      1987  ...   dragon        libra     dragon libra
4    239   male      1970  ...    horse        virgo      horse virgo
..   ...    ...       ...  ...      ...          ...              ...
929  100   male      1974  ...    horse        libra      horse libra
930   46   male      1938  ...       ox        libra         ox libra
931  116   male      1980  ...     goat        libra       goat libra
932  944   male      2017  ...   monkey        libra     monkey libra
933  108   male      1977  ...    snake        libra      snake libra

[934 rows x 10 columns]
ggzm1=ggzm['zod_month'].value_counts(normalize=True)
ggzm1
gemini         0.108137
virgo          0.097430
libra          0.096360
cancer         0.086724
aries          0.084582
taurus         0.082441
sagittarius    0.077088
scorpio        0.077088
leo            0.076017
pisces         0.076017
aquarious      0.07387
capricorn      0.064240
Name: zod_month, dtype: float64
ggzm1.to_csv('allzod_month')
ggzm1.to_csv('all_zodmonth.csv')
chemzodmon=ggzm[ggzm.category =="chemistry"]
chemzodmon
      ID gender  win year  ... zod_year    zod_month          zod all
0    198   male      1938  ...      rat  sagittarius  rat sagittarius
1    211   male      1950  ...    tiger       cancer     tiger cancer
2    208   male      1948  ...    tiger          leo        tiger leo
3    269   male      1987  ...   dragon        libra     dragon libra
4    239   male      1970  ...    horse        virgo      horse virgo
..   ...    ...       ...  ...      ...          ...              ...
182  829   male      2008  ...   dragon        virgo     dragon virgo
183  212   male      1951  ...     goat        virgo       goat virgo
184  251   male      1978  ...   monkey        libra     monkey libra
185  268   male      1987  ...   rabbit        libra     rabbit libra
186  270   male      1988  ...     goat        libra       goat libra

[187 rows x 10 columns]


chzm=chemzodmon['zod_month'].value_counts(normalize=True)
chzm
virgo          0.122995
libra          0.096257
taurus         0.096257
cancer         0.090909
aries          0.090909
leo            0.085561
pisces         0.085561
gemini         0.080214
sagittarius    0.069519
aquarious      0.069519
capricorn      0.058824
scorpio        0.053476
Name: zod_month, dtype: float64

chzm.to_csv('chemzm.csv')
chemzm1=pd.read_csv('chemzm.csv')
chemzm1
     Unnamed: 0  zod_month
0         virgo   0.122995
1         libra   0.096257
2        taurus   0.096257
3        cancer   0.090909
4         aries   0.090909
5           leo   0.085561
6        pisces   0.085561
7        gemini   0.080214
8   sagittarius   0.069519
9     aquarious   0.069519
10    capricorn   0.058824
11      scorpio   0.053476
chemzm1.rename(columns= {'Unnamed: 0': 'zod_month', 'zod_month':'frequency'}, inplace=True)
chemzm1
     