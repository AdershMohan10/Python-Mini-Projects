import os
#os.remove('bye.txt')
#os.rename('hello.txt','hlo.txt')

pa="C:\\Users\\Dell\\Desktop\\python september\\hlo.txt"

if os.path.exists(pa):
    if os.path.isfile(pa):
        print('its file')
    elif os.path.isdir(pa):
        print('its folder')
