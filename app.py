import streamlit as st

import numpy as np

import matplotlib.pyplot as plt

st.title("🌙 Moon vs Earth Jump Simulation")

st.write("调整参数，看看在不同重力下跳跃的变化！")

# 参数输入

v0 = st.slider("Initial velocity (m/s)", 1.0, 20.0, 5.0)

g_moon = 1.62

g_earth = 9.8

# 模拟函数

def simulate_jump(v0, g, dt=0.1):

    t = 0

    y = 0

    vy = v0

    traj = []

    while y >= 0:

        traj.append(y)

        y = y + vy * dt

        vy = vy - g * dt

        t += dt

    return traj

# 运行模拟

moon_traj = simulate_jump(v0, g_moon)

earth_traj = simulate_jump(v0, g_earth)

# 画图

fig, ax = plt.subplots()

ax.plot(moon_traj, label="Moon (g=1.62)")

ax.plot(earth_traj, label="Earth (g=9.8)")

ax.set_title("Jump Comparison")

ax.set_xlabel("Time Step")

ax.set_ylabel("Height")

ax.legend()

st.pyplot(fig)

# 输出数据

st.write("### Results")

st.write(f"Moon max height: {max(moon_traj):.2f} m")

st.write(f"Earth max height: {max(earth_traj):.2f} m")
