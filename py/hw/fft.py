#python

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


#定义函数，用于计算所有基矢的频率
def gen_freq( N, fs ):
    k = np.arange( 0, math.floor(N/2) + 1 , 1 )
    return ( k * fs ) / N

#总数据量
N = 100

#定义多个不同频率的基矢(可修改fk,A,phi的长度，来改变基矢的个数)
# fk = [ 2/N, 5/N ]  #频率
# A = [ 7, 3 ]  #振幅
# phi = [ np.pi, 2 ]    #初始相位

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

g = np.fft.rfft( s )    #做傅立叶变换

#做出采样率为1和15时的“频率-振幅”图
for fs in [ 1, 15]:
    #将采样间隔设置为1，即退化为没有时间意义的离散点
    freq = gen_freq( N, fs = fs )   #计算频率序列
    ck = np.abs( g ) / N    #计算每个频率对应的振幅（复数形式傅里叶展开）
    print(ck)
    plt.figure() #做出序列的“频率-振幅”图
    plt.plot( freq, ck, '.' )
    for f in fk:
        ck0 = round( ck[ np.where( freq==f*fs )][0],1 )
        plt.annotate('$({},{})$'.format( f*fs, ck0), xy=(f*fs, ck0),xytext=(5,0), textcoords='offset points')
    plt.xlabel( '$f$,  (SampleFrequence={})'.format(fs) )
    plt.ylabel( '$c(f)$' )
    plt.show()
