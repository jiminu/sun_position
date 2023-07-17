from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
import numpy as np


def make_3d_ax() :
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x_ratio = [[0], [1]]
    y_ratio = [[0], [1]]
    z_ratio = [[0], [1]]
    ax.set_box_aspect(aspect = (0.8,1,1))
    # ax.set_box_aspect((np.ptp(x_ratio), np.ptp(y_ratio), np.ptp(z_ratio)))
    
    return ax

def create_sphere(cx,cy,cz, r, resolution=10):
    phi = np.linspace(0, 2*np.pi, 2*resolution)
    theta = np.linspace(0, np.pi, resolution)

    theta, phi = np.meshgrid(theta, phi)

    r_xy = r*np.sin(theta)
    x = cx + np.cos(phi) * r_xy
    y = cy + np.sin(phi) * r_xy
    z = cz + r * np.cos(theta)

    return np.stack([x,y,z])
    
def draw_3d_coordinate(ax, _list, _c = 'black', _s = 5, _alpha = 1, _marker = '.') :
    """ draw point from [[x,y,z]] coordinate list.

    Args:
        _list ([[x,y,z]]): [[x,y,z]] list.
        _c (str, optional): point color. Defaults to 'black'.
        _s (int, optional): point size. Defaults to 5.
        _alpha (int, optional): point transparency. Defaults to 1.
        _marker (str, optional): point style. Defaults to '.'.
    """
    xli = []
    yli = []
    zli = []
    for i in range(len(_list)) :
        xli.append(_list[i][0])
        yli.append(_list[i][1])
        zli.append(_list[i][2])
    ax.scatter(xli, yli, zli, c= _c, s= _s, alpha= _alpha, marker= _marker)
    
def read_3d_point(path, state = True) :
    import math
    li = []
    if (state) :
        with open (path, 'r') as f :
            for line in f :
                xyPoint = line.split('\t')
                li.append([])
                x = xyPoint[0]
                y = xyPoint[1]
                z = xyPoint[2][:-1]
                li[-1].append(float(x))
                li[-1].append(float(y))
                li[-1].append(float(z))
                
def calculate_angle(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    # 벡터 AB 계산
    AB_x = x2 - x1
    AB_y = y2 - y1
    AB_z = z2 - z1

    # 벡터 AC 계산
    AC_x = x3 - x1
    AC_y = y3 - y1
    AC_z = z3 - z1

    # AB와 AC의 내적 계산
    dot_product = AB_x * AC_x + AB_y * AC_y + AB_z * AC_z

    # 벡터의 크기 계산
    AB_length = math.sqrt(AB_x**2 + AB_y**2 + AB_z**2)
    AC_length = math.sqrt(AC_x**2 + AC_y**2 + AC_z**2)

    # 코사인 값 계산
    cos_theta = dot_product / (AB_length * AC_length)

    # 각도 계산 (라디안에서 도로 변환)
    angle = math.acos(cos_theta) * (180 / math.pi)

    return angle

if __name__ == '__main__' :
    answer_path = 'C:\code\hy_python\sun_position\output\sun_pos_sec.txt'
        
    ax = make_3d_ax()
    li = read_3d_point(answer_path)
    
    angles = []
    for i in range(len(li)-1):
        x_prev, y_prev, z_prev = li[i]
        x_next, y_next, z_next = li[i+1]

        angle = calculate_angle(0,0,0, x_prev, y_prev, z_prev, x_next, y_next, z_next)
        angles.append(angle)
        
    # --------------- draw point
    draw_3d_coordinate(ax, li)
    
    # # --------------- make sphere
    earth = create_sphere(0,0,0, 6371, 10)
    ax.plot_surface(earth[0], earth[1], earth[2], color='b', linewidth=0, alpha=1, rstride=1, cstride=1)
        
    plt.show()