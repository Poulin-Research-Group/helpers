import os


def writer(t_total, direc, filename):
    """
    Write the time to a file in a specific directory. Check to see if the
    directory exists first, and then if the file exists. If either of these are
    not true, then they are created.

    Parameters
    ----------
    t_total : float64
        Time. In our (read: my) cases, this is the amount of time it took for
        the equations to be solved numerically.
    direc : string
        The name of the directory that the file will be located in.
    filename : string
        The name of the file that the time is written to. This should not
        include the directory.
    """

    # check to see if directory exists; if it doesn't, create it.
    if not os.path.isdir(direc):
        os.makedirs(direc)

    filename = os.path.join(direc, filename)

    # check to see if file exists; if it doesn't, create it.
    if not os.path.exists(filename):
        open(filename, 'a').close()

    # write time to the file
    F = open(filename, 'a')
    F.write('%f\n' % t_total)
    F.close()
