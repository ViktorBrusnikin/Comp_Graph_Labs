from PIL import Image
import numpy as np

def dotted_line(image, x0, y0, x1, y1, count, color, name):
    step = 1.0 / count
    for t in np.arange(0, 1, step):
        x = round((1.0 - t) * x0 + t * x1)
        y = round((1.0 - t) * y0 + t * y1)
        image[y, x] = color
    img = Image.fromarray(image, mode='L')
    img.save(f'{name}.png')


def dotted_line_v2(image, x0, y0, x1, y1, color, name):
    count = np.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
    step = 1.0 / count
    for t in np.arange(0, 1, step):
        x = round((1.0 - t) * x0 + t * x1)
        y = round((1.0 - t) * y0 + t * y1)
        image[y, x] = color
    img = Image.fromarray(image, mode='L')
    img.save(f'{name}.png')


def x_loop_line(image, x0, y0, x1, y1, color, name):
    for x in np.arange(x0, x1):
        t = (x - x0) / (x1 - x0)
        y = round((1.0 - t) * y0 + t * y1)
        image[y, x] = color
    img = Image.fromarray(image, mode='L')
    img.save(f'{name}.png')


def x_loop_line_hotfix_1(image, x0, y0, x1, y1, color, name):
    if (x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    for x in np.arange(x0, x1):
        t = (x - x0) / (x1 - x0)
        y = round((1.0 - t) * y0 + t * y1)
        image[y, x] = color
    img = Image.fromarray(image, mode='L')
    img.save(f'{name}.png')


def x_loop_line_hotfix_2(image, x0, y0, x1, y1, color, name):
    flag = False
    if (abs(x0 - x1) < abs(y0 - y1)):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        flag = True

    for x in np.arange(x0, x1):
        t = (x - x0) / (x1 - x0)
        y = round((1.0 - t) * y0 + t * y1)
        if (flag):
            image[x, y] = color
        else:
            image[y, x] = color

    img = Image.fromarray(image, mode='L')
    img.save(f'{name}.png')


def x_loop_line_v2(image, x0, y0, x1, y1, color, name):
    flag = False
    if (abs(x0 - x1) < abs(y0 - y1)):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        flag = True
    if (x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    for x in np.arange(x0, x1):
        t = (x - x0) / (x1 - x0)
        y = round((1.0 - t) * y0 + t * y1)
        if (flag):
            image[x, y] = color
        else:
            image[y, x] = color

    img = Image.fromarray(image, mode='L')
    img.save(f'{name}.png')


def x_loop_line_v2_no_y_calc(image, x0, y0, x1, y1, color, name):
    flag = False
    if (abs(x0 - x1) < abs(y0 - y1)):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        flag = True
    if (x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    y = y0
    dy = abs(y1 - y0) / (x1 - x0)
    derror = 0.0
    y_update = 1 if y1 > y0 else -1
    for x in range(x0, x1):
        if (flag):
            image[x, y] = color
        else:
            image[y, x] = color
        derror += dy
        if (derror > 0.5):
            derror -= 1.0
            y += y_update

    img = Image.fromarray(image, mode='L')
    img.save(f'{name}.png')


def x_loop_line_v2_no_y_calc_v2_for_some_unknown_reasons(image, x0, y0, x1, y1, color, name):
    flag = False
    if (abs(x0 - x1) < abs(y0 - y1)):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        flag = True
    if (x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    y = y0
    dy = 2 * (x1 - x0) * abs(y1 - y0) / (x1 - x0)
    derror = 0.0
    y_update = 1 if y1 > y0 else -1
    for x in range(x0, x1):
        if (flag):
            image[x, y] = color
        else:
            image[y, x] = color
        derror += dy
        if (derror > 2 * (x1 - x0) * 0.5):
            derror -= 2 * (x1 - x0) * 1.0
            y += y_update

    img = Image.fromarray(image, mode='L')
    img.save(f'{name}.png')


def bresenham_line(image, x0, y0, x1, y1, color, name):
    flag = False
    if (abs(x0 - x1) < abs(y0 - y1)):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        flag = True
    if (x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    y = y0
    dy = 2 * abs(y1 - y0)
    derror = 0.0
    y_update = 1 if y1 > y0 else -1
    for x in range(x0, x1):
        if (flag):
            image[x, y] = color
        else:
            image[y, x] = color
        derror += dy
        if (derror > (x1 - x0)):
            derror -= 2 * (x1 - x0)
            y += y_update

    img = Image.fromarray(image, mode='L')
    img.save(f'{name}.png')

h = 200
w = 200
#image = np.zeros((h, w), dtype = np.uint8)
for i in range(13):
    x0 = 100
    x1 = int(100 + 95*np.cos(i*2*np.pi/13))
    y0 = 100
    y1 = int(100 + 95*np.sin(i*2*np.pi/13))
    count = 50
    color = 255
    #dotted_line(image, x0, y0, x1, y1, count, color, 'dotted_line')
    #dotted_line_v2(image, x0, y0, x1, y1, color, 'dotted_line_v2')
    #x_loop_line(image, x0, y0, x1, y1, color, 'x_loop_line')
    #x_loop_line_hotfix_1(image, x0, y0, x1, y1, color, 'x_loop_line_hotfix_1')
    #x_loop_line_hotfix_2(image, x0, y0, x1, y1, color, 'x_loop_line_hotfix_2')
    #x_loop_line_v2(image, x0, y0, x1, y1, color, 'x_loop_line_v2')
    #x_loop_line_v2_no_y_calc(image, x0, y0, x1, y1, color, 'x_loop_line_v2_no_y_calc')
    #x_loop_line_v2_no_y_calc_v2_for_some_unknown_reasons(image, x0, y0, x1, y1, color, 'x_loop_line_v2_no_y_calc_meh')
    #bresenham_line(image, x0, y0, x1, y1, color, 'bresenham_line')

#image = np.zeros((1000, 1000), dtype = np.uint8)
file = open(r"C:\Users\Victor\Desktop\model\model_1.obj")
v = []
for str in file:
    splitted_str = str.split(' ')
    if(splitted_str[0] == 'v'):
        v.append([float(x) for x in splitted_str[1:4]])
file.close()

#for coords in v:
#    image[int(5000*coords[0]+500), int(5000*coords[1]+500)] = 255
#img = Image.fromarray(image, mode='L')
#img.save('test.png')
f = []
file = open(r"C:\Users\Victor\Desktop\model\model_1.obj")
for str in file:
    splitted_str = str.split()
    if(splitted_str[0] == 'f'):
       v1 = v[int(splitted_str[1].split('/')[0])-1]
       v2 = v[int(splitted_str[2].split('/')[0])-1]
       v3 = v[int(splitted_str[3].split('/')[0])-1]
       f.append([v1, v2, v3])
file.close()
image = np.zeros((1000, 1000), dtype = np.uint8)
for i in f:
    bresenham_line(image, int(5000*i[0][0]+500), int(5000*i[0][1]+500), int(5000*i[1][0]+500), int(5000*i[1][1]+500), 100, 'final')
    bresenham_line(image, int(5000*i[0][0]+500), int(5000*i[0][1]+500), int(5000*i[2][0]+500), int(5000*i[2][1]+500), 100, 'final')
    bresenham_line(image, int(5000*i[1][0]+500), int(5000*i[1][1]+500), int(5000*i[2][0]+500), int(5000*i[2][1]+500), 100, 'final')
img = Image.fromarray(image, mode='L')