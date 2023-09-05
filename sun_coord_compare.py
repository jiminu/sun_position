import math

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
    # 좌표 입력
    x_spice = -54537787.29746191
    y_spice = 130248863.55205774
    z_spice =  56462268.18020495

    x_astro_gcrs  = -54523500.95223228
    y_astro_gcrs  = 130253905.95454401
    z_astro_gcrs  =  56464454.3778301
    
    x_astro_teme  = -55336272.639175065
    y_astro_teme  = 129962819.70413539
    z_astro_teme  =  56344380.42646843
    
    x_calc  = -54795940.0873033
    y_calc  = 128664548.36510833
    z_calc  =  55774745.50930806


    # 각도 계산
    angle_spice_to_astro_gcrs = calculate_angle(0, 0, 0, x_spice, y_spice, z_spice, x_astro_gcrs, y_astro_gcrs, z_astro_gcrs)
    angle_spice_to_astro_teme = calculate_angle(0, 0, 0, x_spice, y_spice, z_spice, x_astro_teme, y_astro_teme, z_astro_teme)
    angle_spice_to_calc       = calculate_angle(0, 0, 0, x_spice, y_spice, z_spice, x_calc, y_calc, z_calc)
    
    angle_teme_to_calc = calculate_angle(0, 0, 0, x_astro_teme, y_astro_teme, z_astro_teme, x_calc, y_calc, z_calc)
    

    print(f"spice to astro gcrs  : {angle_spice_to_astro_gcrs}")
    print(f"spice to astro teme  : {angle_spice_to_astro_teme}")
    print(f"spice to calc        : {angle_spice_to_calc}")
    print(f"teme to calc         : {angle_teme_to_calc}")
    print("\n")


    ECEF_spice_x = -141205056.63961306
    ECEF_spice_y =   -3800796.8390634153 
    ECEF_spice_z =   56336580.92883327
    
    ECEF_astro_itrs_x = -141207382.45348424
    ECEF_astro_itrs_y =   -3591209.329588586
    ECEF_astro_itrs_z =   56344380.42646843
    
    
    angle_ecef_spice_astro    = calculate_angle(0, 0, 0, ECEF_spice_x, ECEF_spice_y, ECEF_spice_z, ECEF_astro_itrs_x, ECEF_astro_itrs_y, ECEF_astro_itrs_z)
    
    print(f"spice to astro ecef  : {angle_ecef_spice_astro}")
    