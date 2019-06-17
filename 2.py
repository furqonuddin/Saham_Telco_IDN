import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

df1 = pd.read_csv('EXCL.JK.csv', index_col= 'Date', parse_dates=['Date'])
df2 = pd.read_csv('FREN.JK.csv', index_col= 'Date', parse_dates=['Date'])
df3 = pd.read_csv('ISAT.JK.csv', index_col= 'Date', parse_dates=['Date'])
df4 = pd.read_csv('TLKM.JK.csv', index_col= 'Date', parse_dates=['Date'])

df11 = pd.DataFrame(df1)
df22 = pd.DataFrame(df2)
df33 = pd.DataFrame(df3)
df44 = pd.DataFrame(df4)


perusahaan = np.array(['PT. XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk'])
dftgl = pd.date_range(start='4/1/2019', end='4/30/2019')

plt.plot(df1['04-2019'].index, df1['04-2019']['Close'], 'r-')
plt.plot(df2['04-2019'].index, df2['04-2019']['Close'], 'g-')
plt.plot(df3['04-2019'].index, df3['04-2019']['Close'], 'b-')
plt.plot(df4['04-2019'].index, df4['04-2019']['Close'], 'y-')


plt.title('Harga Historis Saham Provider Indonesia(April 2019)')
plt.xlabel('Tanggal')
plt.ylabel('Rupiah(IDR)')
plt.xticks(rotation = 60)
plt.legend(
    perusahaan,
    scatterpoints=1,
    loc='lower left',
    ncol=3,
    fontsize=8
)

plt.tight_layout()
plt.show()

