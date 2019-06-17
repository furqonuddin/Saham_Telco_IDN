import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

df1 = pd.read_csv('EXCL.JK.csv', index_col= False, parse_dates=['Date'])
df2 = pd.read_csv('FREN.JK.csv', index_col= False, parse_dates=['Date'])
df3 = pd.read_csv('ISAT.JK.csv', index_col= False, parse_dates=['Date'])
df4 = pd.read_csv('TLKM.JK.csv', index_col= False, parse_dates=['Date'])

df11 = pd.DataFrame(df1)
df22 = pd.DataFrame(df2)
df33 = pd.DataFrame(df3)
df44 = pd.DataFrame(df4)


perusahaan = np.array(['PT. XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk'])
tgl = df11['Date'].values

xl = df11['Close'].values
smart = df22['Close'].values
ind = df33['Close'].values
tele = df44['Close'].values

plt.plot(tgl,xl, 'r-')  
plt.plot(tgl,smart, 'g-')
plt.plot(tgl,ind, 'b-')
plt.plot(tgl,tele, 'y-')
plt.title('Harga Historis Saham Provider Indonesia')
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
