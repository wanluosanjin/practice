import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

N = 100

fk = [ 2/N, 40/N , 45/N ]  #频率
A = [ 7, 3 ,4 ]  #振幅
phi = [ np.pi, 2, 2*np.pi ]    #初始相位

#生成由这些基矢信号叠加而成的混合信号
n = np.arange( N )
s_array = []
for p in zip( A, fk, phi ):
    s_array.append( p[0] * np.sin( 2 * np.pi * p[1] * n + p[2] ) )
s_array = np.array( s_array )

#做出波形图
s = np.sum( s_array, axis=0 )
plt.figure( 1 )
plt.axhline(y=0, color='grey', lw=0.5)
for nn in range( len(fk) ):
    plt.plot( n, s_array[ nn, : ], ':',marker ='+', alpha=0.5 , label='$f_k={}/{},A_k={},\phi_k={}$'.format( int(fk[nn]*N), N, A[nn], round( phi[nn],2 )) )
plt.plot( n, s , 'r-o', lw=2 )
plt.legend()
plt.xlabel( 'n' )
plt.ylabel( 's' )
plt.show()

b, a = signal.butter(8, 0.8, 'lowpass')   #配置滤波器 8 表示滤波器的阶数
filtedData = signal.filtfilt(b, a, s)  #data为要过滤的信号
plt.figure() #做出序列的“频率-振幅”图
plt.plot( filtedData,'r-o')
plt.show()

g = np.fft.rfft( s )    #做傅立叶变换
fg = np.fft.rfft( filtedData )

gf = np.abs( g ) / N 
fgf = np.abs( fg ) / N 
n51=np.arange(N//2+1)
plt.figure() #做出序列的“频率-振幅”图
plt.plot( n51, gf, '.' )
plt.plot( n51, fgf, '+' )
plt.show()

