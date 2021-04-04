from PIL import Image

maps = dict()

# de_dust2

# StartX = -2486
# StartY = -1150
# EndX = 2127
# EndY = 3455
# ResX = 1024
# ResY = 1024
# SizeX = EndX - StartX
# SizeY = EndY - StartY

# maps['de_dust2'] = dict()
# maps['de_dust2']['StartX'] = StartX
# maps['de_dust2']['StartY'] = StartY
# maps['de_dust2']['EndX'] = EndX
# maps['de_dust2']['EndY'] = EndY
# maps['de_dust2']['ResX'] = ResX
# maps['de_dust2']['ResY'] = ResY
# maps['de_dust2']['SizeX'] = SizeX
# maps['de_dust2']['SizeY'] = SizeY

# StartX = -2486
# StartY = -1150
# EndX = 2127
# EndY = 3455
# ResX = 1024
# ResY = 1024
# SizeX = EndX - StartX
# SizeY = EndY - StartY

# maps['de_overpass'] = dict()
# maps['de_overpass']['StartX'] = StartX
# maps['de_overpass']['StartY'] = StartY
# maps['de_overpass']['EndX'] = EndX
# maps['de_overpass']['EndY'] = EndY
# maps['de_overpass']['ResX'] = ResX
# maps['de_overpass']['ResY'] = ResY
# maps['de_overpass']['SizeX'] = SizeX
# maps['de_overpass']['SizeY'] = SizeY

map_info = dict()
map_info['de_dust2'] = ('de_dust2', 2127, 3455, 1024, 1024, -2486, -1150)
map_info['de_cache'] = ('de_cache', 3752, 3187, 1024, 1024, -2031, -2240)
map_info['de_cbble'] = ('de_cbble', 2282, 3032, 1024, 1024, -3819, -3073)
map_info['de_inferno'] = ('de_inferno', 2797, 3800, 1024, 1024, -1960, -1062)
map_info['de_mirage'] = ('de_mirage', 1912, 1682, 1024, 1024, -3217, -3401)
map_info['de_overpass'] = ('de_overpass', 503, 1740, 1024, 1024, -4820, -3591)
map_info['de_train'] = ('de_train', 2262, 2447, 1024, 1024, -2436, -2469)


def draw_point(x1, y1, x2, y2, PointRadius, map):
    im = Image.open(f'static/{map}.png')
    pixelMap = im.load()

    img = Image.new( im.mode, im.size)
    pixelsNew = img.load()
    print(f'Img size: {img.size[0]}x{img.size[1]}')
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if (abs(i - x1)**2 + abs(j - y1)**2 < PointRadius**2) or (abs(i - x2)**2 + abs(j - y2)**2 < PointRadius**2):
                pixelsNew[i,j] = (0,0,255,255)
            else:
                pixelsNew[i,j] = pixelMap[i,j]
                
    img.show()
    img.save("static/out.png") 
    img.close()


def draw_points(x_list, y_list, PointRadius, map):
    im = Image.open(f'static/{map}.png')
    pixelMap = im.load()

    img = Image.new( im.mode, im.size)
    pixelsNew = img.load()
    print(f'Img size: {img.size[0]}x{img.size[1]}')

    mask = [[0 for i in range(img.size[0])] for j in range(img.size[1])]

    for (x,y) in zip(x_list,y_list):
        for i in range(x-PointRadius, x+PointRadius+1):
            for j in range(y-PointRadius, y+PointRadius+1):
                if 0<=i<img.size[0] and 0<=j<img.size[1] and (abs(i - x)**2 + abs(j - y)**2 < PointRadius**2):
                    # print(f'i: {i}, j: {j}, dist: {abs(i - x)**2 + abs(j - y)**2}')
                    mask[i][1024-j] = 1
    
    # for i in range(img.size[0]):
    #     for j in range(img.size[1]):
    #         if mask[i][j]:
    #             print(f'({i},{j})')
    

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            # flag = False

            # for (x,y) in zip(x_list,y_list):
            #     if (abs(i - x)**2 + abs(j - y)**2 < PointRadius**2):
            #         flag = True

            if mask[i][j]:
                # print(f'({i},{j})')
                pixelsNew[i,j] = (0,0,255,255)
            else:
                pixelsNew[i,j] = pixelMap[i,j]
                
    img.show()
    img.save("static/out.png") 
    img.close()


def draw_figure(x_list_list, y_list_list, delta, color_list, map, name="out"):
    
    im = Image.open(f'static/{map}.png')
    # im = Image.open(f'de_dust2.png')
    pixelMap = im.load()

    img = Image.new( im.mode, im.size)
    pixelsNew = img.load()
    print(f'Img size: {img.size[0]}x{img.size[1]}')

    mask = [[0 for i in range(img.size[0])] for j in range(img.size[1])]

    for ind, (x_list, y_list, color) in enumerate(zip(x_list_list,y_list_list, color_list)):
        for (x,y) in zip(x_list,y_list):
            
            for i in range(x, x+delta):
                for j in range(y, y+delta):
                    # print(f'i: {i}, j: {1024-j}, ind: {ind}, delta: {delta}')
                    if 0<=i<1024 and 0<=j<1024:
                        mask[i][1024-j] = ind+1

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            # flag = 0

            # for (x,y) in zip(x_list, y_list):
            #     if (0 <= i - x < delta) and (0 <= j - y < delta):
            #         flag = 1
            
            
            if mask[i][j]:
                # print(f'{i}, {j}: \t {mask[i][j]-1}')
                pixelsNew[i,j] = color_list[mask[i][j]-1]
            else:
                pixelsNew[i,j] = pixelMap[i,j]
                
    # img.show()
    img.save(f"static/{name}.png")
    img.close()


def convert_x(x, map):
    StartX = int(map_info[map][5])
    SizeX = int(map_info[map][1]) - StartX
    ResX = int(map_info[map][3])

    x = x - StartX
    x = (float) (x / SizeX) * ResX
    x = int(x)
    return x


def convert_y(y, map):
    StartY = int(map_info[map][6])
    SizeY = int(map_info[map][2]) - StartY
    ResY = int(map_info[map][4])

    y = y - StartY
    y = (float) (y / SizeY) * ResY
    y = int(y)
    return y


def main():
    x1 = 1023
    y1 = 1023
    x2 = 0
    y2 = 0

    # draw_point(x1, y1, x2, y2, 5)

    # while(True):
    x1 = float(input('X1: '))
    y1 = float(input('Y1: '))

    x2 = float(input('X2: '))
    y2 = float(input('Y2: '))

    x1 = convert_x(x1)
    y1 = convert_y(y1)
    x2 = convert_x(x2)
    y2 = convert_y(y2)



    print(f'\nX1: {x1}\tY1: {y1}')
    print(f'\nX2: {x2}\tY2: {y2}')

    draw_point(x1, y1, x2, y2, 5)


if __name__ == "__main__":
    main()