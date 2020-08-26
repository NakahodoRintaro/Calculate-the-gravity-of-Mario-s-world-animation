//moonの方は動作が重い
%matplotlib inline
#%matplotlib nbagg # JupyterLabでは上手く動かないので今回は使わない。
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.animation import ArtistAnimation
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

import sympy as sym
# Jupyter Notebook上で、レンダリングされた結果を表示する
sym.init_printing()

#公式
from IPython.display import Math
display(Math(r'f = a * x**2 + b * x + c '))
x = sym.Symbol('x') # 変数を一個ずつ指定
y = sym.Symbol('y') # 変数を一個ずつ指定

a, b, c = sym.symbols('a b c') # 変数をまとめて指定("Symbol"じゃなくて"symbols"になってる)

f = a * x**2 + b * x + c # 関数の定義
eq1 = sym.Eq(f.subs(x,0),0)
eq2 = sym.Eq(f.subs(x,14/30),4*1.55)
eq3 = sym.Eq(f.subs(x,28/30),0)
ans = sym.solve([eq1,eq2,eq3],[a,b,c])
g = ans[a]*x**2+ans[b]*x+ans[c]
df =sym.diff(g,x)
df2 = sym.diff(df,x)


def here_function(x):
    y = 26.5714285714286 * x + 1/2 * df2 * x**2 
    y = np.where(y >= 0, y ,0)
    return y

def here_function2(x):
    y = 26.5714285714286 * x + 1/2 * -G * x**2
    y = np.where(y >= 0, y ,0)
    return y

def here_function3(x):
    y = 26.5714285714286 * x + 1/2 * -G/6 * x**2
    y = np.where(y >= 0, y ,0)
    return y

G = 9.80665
start = 0 #定義域の左端　
last = 2* 26.5714285714286*6 /G# 定義域の右端 終了時間

fig = plt.figure(figsize=(12,4), dpi=150) # Figureオブジェクトを作成
ax1 = fig.add_subplot(1,3,1) # figに属するAxesオブジェクトを作成 (縦,横, 自分の番号)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)# figに属するAxesオブジェクトを作成 (縦,横, 自分の番号)
#ax.set_aspect('equal')

ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['bottom'].set_position('zero')
ax1.spines['left'].set_position('zero')
ax1.grid() 
#ax1.set_title('base y = -(x - 3)^2 + 9') # グラフタイトル

ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['bottom'].set_position('zero')
ax2.spines['left'].set_position('zero')
ax2.grid() 

ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax3.spines['bottom'].set_position('zero')
ax3.spines['left'].set_position('zero')
ax3.grid() 
dx = 0.1

x = np.arange(start,last+dx,dx)
y = here_function(x)

y2 = here_function2(x)
y3 =here_function3(x)
#ax2.set_title('diff dx:'+str(dx)) # グラフタイトル

artist_list = []

for i in range(len(x)-1):
    art = ax1.plot(0,y[i], marker='.', color='red', markersize=6, linestyle='None') # 点   
    
    art += ax2.plot(0,y2[i], marker='.', color='red', markersize=6, linestyle='None') # 点  
    art += ax3.plot(0,y3[i], marker='.', color='red', markersize=6, linestyle='None') # 点  
    artist_list.append(art)

    

ani = ArtistAnimation(fig, artist_list, interval = 100)

plt.close() 
HTML(ani.to_jshtml())
