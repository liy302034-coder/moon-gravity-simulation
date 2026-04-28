import numpy as np
import matplotlib.pyplot as plt

# 月球重力加速度
g_moon = 1.62  

# 初始速度（跳跃速度）
v0 = 5.0  

# 时间步长
dt = 0.01  

# 初始状态
y = 0
v = v0

trajectory = []

# 模拟运动
for i in range(1000):
    v = v - g_moon * dt
    y = y + v * dt
    
    if y < 0:
        break
        
    trajectory.append(y)

# 画图
plt.plot(trajectory)
plt.title("Jump on the Moon")
plt.xlabel("Time")
plt.ylabel("Height")
plt.savefig("image.png")  # 保存图片
plt.show()
