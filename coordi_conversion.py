from PIL import Image


StartX = -2486
StartY = -1150
EndX = 2127
EndY = 3455
ResX = 1024
ResY = 1024
SizeX = EndX - StartX
SizeY = EndY - StartY


def draw_point(x1, y1, x2, y2, PointRadius):
    im = Image.open('de_dust2.png')
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


def draw_points(x_list, y_list, PointRadius):
    im = Image.open('de_dust2.png')
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


def draw_figure(x_list_list, y_list_list, delta, color_list, name="out"):
    
    im = Image.open('de_dust2.png')
    pixelMap = im.load()

    img = Image.new( im.mode, im.size)
    pixelsNew = img.load()
    print(f'Img size: {img.size[0]}x{img.size[1]}')

    mask = [[0 for i in range(img.size[0])] for j in range(img.size[1])]

    for ind, (x_list, y_list, color) in enumerate(zip(x_list_list,y_list_list, color_list)):
        for (x,y) in zip(x_list,y_list):
            # print(f'x: {x}, delta: {delta}')
            for i in range(x, x+delta):
                for j in range(y, y+delta):
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

def convert_x(x):
    x = x - StartX
    x = (float) (x / SizeX) * ResX
    x = int(x)
    return x


def convert_y(y):
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