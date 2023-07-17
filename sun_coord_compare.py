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

# 좌표 입력
x_site = 	-56286979.62194103
y_site = 	129616845.01029563
z_site =  	56188360.107969224

x_calc = -56538121.15588646
y_calc = 128057407.74187401
z_calc =  55511555.651647896

x_spice = -56289324.06000696
y_spice = 129615982.1728326
z_spice =  55773768.51302104

x_astro_gcrs  = -54846235.54483388
y_astro_gcrs  = 128660530.91391857
z_astro_gcrs  =  55787557.97113865

x_astro_teme  = -56203706.13468422
y_astro_teme  = 129647145.54279512
z_astro_teme  =  56207557.90068312 

x_astro_icrs  = -148077529.7489035
y_astro_icrs  = -26282480.58826596
z_astro_icrs  = -7391307.071477198


# 각도 계산
angle_site_to_lib    = calculate_angle(0, 0, 0, x_site, y_site, z_site, x_astro_gcrs, y_astro_gcrs, z_astro_gcrs)
angle_lib_to_calc    = calculate_angle(0, 0, 0, x_astro_gcrs, y_astro_gcrs, z_astro_gcrs, x_calc, y_calc, z_calc)
angle_calc_to_site    = calculate_angle(0, 0, 0, x_calc, y_calc, z_calc, x_site, y_site, z_site)
angle_spice_to_site    = calculate_angle(0, 0, 0, x_spice, y_spice, z_spice, x_site, y_site, z_site)

angle_site_to_gcrs  = calculate_angle(0, 0, 0, x_site, y_site, z_site, x_astro_gcrs, y_astro_gcrs, z_astro_gcrs)
angle_site_to_teme  = calculate_angle(0, 0, 0, x_site, y_site, z_site, x_astro_teme, y_astro_teme, z_astro_teme)
angle_site_to_icrs  = calculate_angle(0, 0, 0, x_site, y_site, z_site, x_astro_icrs, y_astro_icrs, z_astro_icrs)

print(f"site to lib   : {angle_site_to_lib}")
print(f"lib to calc   : {angle_lib_to_calc}")
print(f"calc to site  : {angle_calc_to_site}")
print(f"spice to site : {angle_spice_to_site}\n")

print(f"site to gcrs  : {angle_site_to_gcrs}")
print(f"site to teme  : {angle_site_to_teme}")
print(f"site to icrs  : {angle_site_to_icrs}")
