import math


def vincent(fi_p, lambda_p, fi_k, lambda_k, a, e2):
    fi_p = math.radians(fi_p)
    lambda_p = math.radians(lambda_p)
    fi_k = math.radians(fi_k)
    lambda_k = math.radians(lambda_k)

    b = a * math.sqrt(1 - e2)
    f = 1 - b / a

    U1 = math.atan(math.tan(fi_p) * (1 - f))
    U2 = math.atan(math.tan(fi_k) * (1 - f))

    dlambda = lambda_k - lambda_p

    epsilon = 0.000001

    cos_alpha2 = 1
    cos_2_sigma = 1
    cos_sigma = 1
    sin_sigma = 1
    sigma = 1

    l_i = dlambda
    while True:
        sin_sigma = math.sqrt((math.cos(U2) * math.sin(l_i)) ** 2 + (
                    math.cos(U1) * math.sin(U2) - math.sin(U1) * math.cos(U2) * math.cos(l_i)) ** 2)

        cos_sigma = math.sin(U1) * math.sin(U2) + math.cos(U1) * math.cos(U2) * math.cos(l_i)

        sigma = math.atan2(sin_sigma, cos_sigma)

        sin_alpha = (math.cos(U1) * math.cos(U2) * math.sin(l_i)) / sin_sigma
        cos_alpha2 = 1 - sin_alpha ** 2

        cos_2_sigma = cos_sigma - (2 * math.sin(U1) * math.sin(U2)) / cos_alpha2
        c = (f / 16) * cos_alpha2 * (4 + f * (4 - 3 * cos_alpha2))

        l_prev_i = l_i
        l_i = dlambda + (1 - c) * f * sin_alpha * (
                    sigma + c * sin_sigma * (cos_2_sigma + c * cos_sigma * (-1 + 2 * cos_2_sigma ** 2)))

        if abs((math.degrees(l_i - l_prev_i) * 3600)) < epsilon:
            break

    u2 = ((a ** 2 - b ** 2) / b ** 2) * cos_alpha2
    A = 1 + (u2 / 16384) * (4096 + u2 * (-768 + u2 * (320 - 175 * u2)))
    B = (u2 / 1024) * (256 + u2 * (-128 + u2 * (74 - 47 * u2)))

    dsigma = B * sin_sigma * (cos_2_sigma + (1 / 4) * B * (
                cos_sigma * (-1 + 2 * cos_2_sigma ** 2) - (1 / 6) * B * cos_2_sigma * (-3 + 4 * cos_2_sigma ** 2)))

    s = b * A * (sigma - dsigma)

    Ap = math.degrees(math.atan2(math.cos(U2) * math.sin(l_i),
                                 math.cos(U1) * math.sin(U2) - math.sin(U1) * math.cos(U2) * math.cos(l_i)))
    App = math.degrees(math.atan2(math.cos(U1) * math.sin(l_i),
                                  - math.sin(U1) * math.cos(U2) + math.cos(U1) * math.sin(U2) * math.cos(l_i)))

    if Ap < 0:
        Ap = Ap + 360

    if App < 0:
        App = App + 360



    return Ap, App, s


    a = 6378137.000
    e2 = 0.00669438002290