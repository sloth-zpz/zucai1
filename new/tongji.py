def tongji_daxiao(num,pankou):
    if pankou == '2/2.5':
        if num < 2:
            return -1
        if num == 2:
            return -0.5
        if num > 2:
            return 1
    if pankou == '2.5':
        if num <= 2:
            return -1
        if num > 2:
            return 1
    if pankou == '2.5/3':
        if num < 3:
            return -1
        if num == 3:
            return 0.5
        if num > 3:
            return 1
    if pankou == '3':
        if num < 3:
            return -1
        if num == 3:
            return 0
        if num > 3:
            return 1

    if pankou == '1/1.5':
        if num < 1:
            return -1
        if num == 1:
            return -0.5
        if num > 1:
            return 1
    if pankou == '1.5':
        if num <= 1:
            return -1
        if num > 1:
            return 1
    if pankou == '1.5/2':
        if num < 2:
            return -1
        if num == 2:
            return 0.5
        if num > 2:
            return 1
    if pankou == '2':
        if num < 2:
            return -1
        if num == 2:
            return 0
        if num > 2:
            return 1

    if pankou == '3/3.5':
        if num < 3:
            return -1
        if num == 3:
            return -0.5
        if num > 3:
            return 1
    if pankou == '3.5':
        if num <= 3:
            return -1
        if num > 3:
            return 1
    if pankou == '3.5/4':
        if num < 4:
            return -1
        if num == 4:
            return 0.5
        if num > 4:
            return 1
    if pankou == '4':
        if num < 4:
            return -1
        if num == 4:
            return 0
        if num > 4:
            return 1

def tongji_yapan(zhu,ke,pankou):
    if pankou == '平手':
        if zhu - ke >= 0:
            return 1
        if zhu - ke == -1:
            return 1
        if zhu - ke < -1:
            return -1

    if pankou == '平手/半球':
        if zhu - ke >= 0:
            return 1
        if zhu - ke == -1:
            return -1
        if zhu - ke < -1:
            return -1

    if pankou == '半球':
        if zhu - ke >= 0:
            return 1
        if zhu - ke < 0:
            return -1

    if pankou == '半球/一球':
        if zhu - ke >= 1:
            return 1
        if zhu - ke == 0:
            return 1
        if zhu - ke < 0:
            return -1

    if pankou == '一球':
        if zhu - ke >= 1:
            return 1
        if zhu - ke == 0:
            return 1
        if zhu - ke < 0:
            return -1

    if pankou == '一球/球半':
        if zhu - ke >= 1:
            return 1
        if zhu - ke == 0:
            return -1
        if zhu - ke < 0:
            return -1

    if pankou == '球半':
        if zhu - ke >= 1:
            return 1
        if zhu - ke < 1:
            return -1

    if pankou == '球半/两球':
        if zhu - ke >= 2:
            return 1
        if zhu - ke == 1:
            return 1
        if zhu - ke < 1:
            return -1

    if pankou == '受平手/半球':
        if ke - zhu >= 0:
            return 1
        if ke - zhu == -1:
            return -1
        if ke - zhu < -1:
            return -1

    if pankou == '受半球':
        if ke - zhu >= 0:
            return 1
        if ke - zhu < 0:
            return -1

    if pankou == '受半球/一球':
        if ke - zhu >= 1:
            return 1
        if ke - zhu == 0:
            return 1
        if ke - zhu < 0:
            return -1

    if pankou == '受一球':
        if ke - zhu >= 1:
            return 1
        if ke - zhu == 0:
            return 1
        if ke - zhu < 0:
            return -1

    if pankou == '受一球/球半':
        if ke - zhu >= 1:
            return 1
        if ke - zhu == 0:
            return -1
        if ke - zhu < 0:
            return -1

    if pankou == '受球半':
        if ke - zhu >= 1:
            return 1
        if ke - zhu < 1:
            return -1

    if pankou == '受球半/两球':
        if ke - zhu >= 2:
            return 1
        if ke - zhu == 1:
            return 1
        if ke - zhu < 1:
            return -1