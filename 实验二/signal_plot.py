import matplotlib
matplotlib.use('TkAgg') 

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False    


t_continuous = np.linspace(0, 4 * np.pi, 1000)  
cos_continuous = np.cos(t_continuous)           

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)  
plt.plot(t_continuous, cos_continuous, 'b-', linewidth=2, label='连续余弦信号')
plt.title('连续信号 vs 离散信号对比', fontsize=14)
plt.ylabel('信号幅值', fontsize=12)
plt.legend()
plt.grid(True)

n_discrete = np.arange(-5, 10)                  
step_discrete = np.where(n_discrete >= 0, 1, 0) 

plt.subplot(2, 1, 2)  
plt.stem(n_discrete, step_discrete, 'r-', markerfmt='ro', label='离散阶跃信号')
plt.xlabel('时间(n/t)', fontsize=12)
plt.ylabel('信号幅值', fontsize=12)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
