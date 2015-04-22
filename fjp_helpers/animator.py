import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def get_ims_x(U, xg, yg, Nt):
    ims = []
    for j in xrange(Nt):
        ims.append((plt.pcolormesh(xg[1:-1], yg[1:-1], U[:, :, j], norm=plt.Normalize(0, 1)), ))
    return ims


def get_ims_y(U, xg, yg, Nt, p):
    ims = []
    for j in xrange(Nt):
        U_j = np.vstack([arr.transpose() for arr in np.array_split(U[:, :, j].transpose(), p)])
        ims.append((plt.pcolormesh(xg[1:-1], yg[1:-1], U_j, norm=plt.Normalize(0, 1)), ))
    return ims


def get_ims_xy(U, xg, yg, nx, ny, Nt, p, px, py):
    ims = []
    for j in xrange(Nt):
        U_j = U[:, :, j].reshape(ny, p*nx)
        temp = [None for i in xrange(py)]
        for i in xrange(py):
            temp[i] = U_j[:, i*px*nx : (i+1)*px*nx]

        U_j = np.vstack(temp)
        ims.append((plt.pcolormesh(xg[1:-1], yg[1:-1], U_j, norm=plt.Normalize(0, 1)), ))
    return ims


def mesh_animator(U, xg, yg, nx, ny, Nt, method, p, px, py):
    fig = plt.figure()
    print 'creating meshes...'
    if px == 1:
        ims = get_ims_y(U, xg, yg, Nt, p)
    elif py == 1:
        ims = get_ims_x(U, xg, yg, Nt)
    else:
        ims = get_ims_xy(U, xg, yg, nx, ny, Nt, p, px, py)
    print 'done creating meshes, attempting to put them together...'
    print 'saving...'
    im_ani = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=3000, blit=False)
    im_ani.save('./anims/MPI_SUPER_%s_%dpx_%dpy.mp4' % (method, px, py))
    print 'saved.'
