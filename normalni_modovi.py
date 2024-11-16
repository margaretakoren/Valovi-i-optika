import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

class MassSystem:
    def __init__(self, m1, m2, m3, k1, k2, k3, k4, L, dt, t_max):
        self.m1, self.m2, self.m3 = m1, m2, m3
        self.k1, self.k2, self.k3, self.k4 = k1, k2, k3, k4
        self.L = L
        self.dL = L / 4
        self.dt = dt
        self.t_max = t_max
        self.time = []
        self.x1_list, self.x2_list, self.x3_list = [], [], []
        self.x1, self.x2, self.x3 = 0.03, 0, 0
        self.x1dot, self.x2dot, self.x3dot = 0, 0, 0

    def simulation(self):
        t = 0
        while t < self.t_max:
            F1 = -self.k1 * self.x1 - self.k2 * (self.x1 - self.x2)
            F2 = -self.k3 * (self.x2 - self.x3) - self.k2 * (self.x2 - self.x1)
            F3 = -self.k3 * (self.x3 - self.x2) - self.k4 * self.x3

            x1ddot = F1 / self.m1
            x2ddot = F2 / self.m2
            x3ddot = F3 / self.m3

            self.x1dot += x1ddot * self.dt
            self.x2dot += x2ddot * self.dt
            self.x3dot += x3ddot * self.dt

            self.x1 += self.x1dot * self.dt
            self.x2 += self.x2dot * self.dt
            self.x3 += self.x3dot * self.dt

            self.time.append(t)
            self.x1_list.append(self.x1)
            self.x2_list.append(self.x2)
            self.x3_list.append(self.x3)

            t += self.dt

    def animation(self):
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), facecolor='black')
        ax1.set_xlim(-self.L / 2 - 0.1, self.L / 2 + 0.1)
        ax1.set_ylim(-0.05, 0.05)
        ax1.set_facecolor('black')
        ax1.tick_params(axis='x', colors='green', labelbottom=False)
        ax1.tick_params(axis='y', colors='green',  labelleft=False)
        ax1.spines['bottom'].set_color('green')
        ax1.spines['top'].set_color('green')
        ax1.spines['left'].set_color('green')
        ax1.spines['right'].set_color('green')
        ax1.plot([-self.L / 2, self.L / 2], [0, 0], color='green', linewidth=0.5, linestyle='--')
        mass1, = ax1.plot([], [], 'o', color='blue', markersize=8, label="Masa 1")
        mass2, = ax1.plot([], [], 'o', color='magenta', markersize=8, label="Masa 2")
        mass3, = ax1.plot([], [], 'o', color='lime', markersize=8, label="Masa 3")
        ax1.legend(facecolor='black', edgecolor='green', labelcolor='green')
        ax2.set_xlim(0, self.t_max)
        ax2.set_ylim(min(min(self.x1_list), min(self.x2_list), min(self.x3_list)) - 0.01,
                     max(max(self.x1_list), max(self.x2_list), max(self.x3_list)) + 0.01)
        ax2.set_facecolor('black')
        ax2.set_xlabel("t(s)", color='green')
        ax2.set_ylabel("x(m)",  color='green')
        ax2.tick_params(axis='x', colors='green')
        ax2.tick_params(axis='y', colors='green')
        ax2.spines['bottom'].set_color('green')
        ax2.spines['top'].set_color('green')
        ax2.spines['left'].set_color('green')
        ax2.spines['right'].set_color('green')
        line1, = ax2.plot([], [], color="blue", label="Masa 1")
        line2, = ax2.plot([], [], color="magenta", label="Masa 2")
        line3, = ax2.plot([], [], color="lime", label="Masa 3")
        ax2.legend(facecolor='black', edgecolor='green', labelcolor='green')

        def init():
            mass1.set_data([], [])
            mass2.set_data([], [])
            mass3.set_data([], [])
            line1.set_data([], [])
            line2.set_data([], [])
            line3.set_data([], [])
            return mass1, mass2, mass3, line1, line2, line3

        def update(frame):
            mass1.set_data(-self.L / 2 + self.dL + self.x1_list[frame], 0)
            mass2.set_data(-self.L / 2 + 2 * self.dL + self.x2_list[frame], 0)
            mass3.set_data(-self.L / 2 + 3 * self.dL + self.x3_list[frame], 0)
            line1.set_data(self.time[:frame], self.x1_list[:frame])
            line2.set_data(self.time[:frame], self.x2_list[:frame])
            line3.set_data(self.time[:frame], self.x3_list[:frame])
            return mass1, mass2, mass3, line1, line2, line3

        ani = FuncAnimation(fig, update, frames=len(self.time), init_func=init, blit=True, interval=10)
        return ani, fig
