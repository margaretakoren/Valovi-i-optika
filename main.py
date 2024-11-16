from normalni_modovi import MassSystem
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,  FFMpegWriter

system = MassSystem(m1=0.15, m2=0.15, m3=0.15, k1=10, k2=5, k3=5, k4=10, L=0.4, dt=0.01, t_max=5)
system.simulation()
ani, fig = system.animation()
plt.tight_layout()
plt.show()
#writer = FFMpegWriter(fps=20, metadata=dict(artist='Margareta'), bitrate=1800)
#ani.save("normalni_modovi.mp4", writer=writer)
