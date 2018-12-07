import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D


def init():
    ax.scatter(x, y, z1, alpha=0.5)
    ax.scatter(x, y, z2, alpha=0.5)
    ax.scatter(x, y, z3, alpha=0.5)

    ax.set_xlabel('$NaOH$ (mL)')
    ax.set_ylabel('$CaCl_2$ (mL)')
    ax.set_zlabel('pH')
    return fig,


def animate(i):
    ax.view_init(elev=10., azim=i)
    return fig,


if __name__ == '__main__':
    fig = plt.figure()
    ax = Axes3D(fig)

    df = pd.read_csv('../data/data.csv')

    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    z1 = df.iloc[:, 2]
    z2 = df.iloc[:, 3]
    z3 = df.iloc[:, 4]

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=30, blit=True)
    anim.save('../results/animation.mp4', fps=60, extra_args=['-vcodec', 'libx264'])
