import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegFileWriter
import matplotlib as mpl


def fourier(t, C):
    f = np.zeros(t.shape)
    A, B = C.real, C.imag
    for k in range(len(C)):
        f = f + A[k]*np.cos(k*t) + B[k]*np.sin(k*t)
    return f


def elephant(t, p1, p2, p3, p4, p5):
    npar = 6
    Cx = np.zeros((npar,), dtype='complex')
    Cy = np.zeros((npar,), dtype='complex')

    Cx[1] = p1.real*1j
    Cx[2] = p2.real*1j
    Cx[3] = p3.real
    Cx[5] = p4.real

    Cy[1] = p4.imag + p1.imag*1j
    Cy[2] = p2.imag*1j
    Cy[3] = p3.imag*1j

    x = np.append(fourier(t,Cx), [-p5.imag])
    y = np.append(fourier(t,Cy), [p5.imag])

    return x, y


def update(i):
    xnew = x.copy()
    xnew[s:s+l] -= np.array(list(range(l)))*(19-abs(20-i))/200
    xnew[s+l:s+2*l] -= np.array(list(range(l-1, -1, -1)))*(19-abs(20-i))/200

    line.set_ydata(-xnew)
    return line, ax


# elephant parameters
p1, p2, p3, p4 = (50 - 30j, 18 + 8j, 12 - 10j, -14 - 60j)
p5 = 40 + 20j  # eyepiece
x, y = elephant(np.linspace(0, 2 * np.pi, 1000), p1, p2, p3, p4, p5)

idx = (y>p5.real).nonzero()
s, l = idx[0][0], len(idx[0])//2

# ------------------------------------------------------------
# set up figure and animation
dt = 1. / 30  # 30 fps
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=True)
plt.axis('off')
line, = ax.plot(y, -x, '.')

if __name__ == '__main__':
    # mpl.rcParams['animation.convert_path'] = r'/usr/local/Cellar/imagemagick/7.0.10-16/bin/convert'
    anim = FuncAnimation(fig, update, frames=np.arange(0, 40), interval=100)
    # anim.save('~/Downloads/elephant.gif', writer='ffmpeg', codec='gif')
    plt.show()
