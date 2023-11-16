# import colorgram
# rgb_list = list()
# colors = colorgram.extract('hirst_painting.jpg', 40)
# for color in colors:
#     first_color = color
#     rgb = first_color.rgb
#     rgb_list.append([rgb[0], rgb[1], rgb[2]])
#
# print(rgb_list)

import random

colour_list = [[223, 177, 3], [2, 135, 196], [7, 149, 97], [228, 114, 156], [127, 160, 203], [242, 122, 43], [26, 17, 62], [226, 238, 246], [240, 164, 195], [232, 82, 112], [64, 12, 68], [235, 201, 46], [3, 173, 118], [83, 30, 20], [194, 15, 39], [231, 53, 30], [195, 69, 36], [140, 208, 236], [197, 30, 50], [6, 66, 158], [0, 123, 72], [18, 157, 206], [126, 181, 157], [150, 28, 21], [238, 202, 7], [180, 181, 220], [162, 209, 188], [233, 173, 160], [90, 127, 184], [12, 68, 45], [93, 80, 20], [0, 110, 126]]
print(len(colour_list))
import turtle as t
t.colormode(255)
tim = t.Turtle()


def change_colour():
    x = random.randint(0, 31)
    colour = colour_list[x]
    return colour

tim.speed(999)

tim.penup()
tim.goto(-920, -470)
tim.pendown()
x = 0
for _ in range (10):
    x += 100
    for _ in range (19):
        tim.penup()
        colour = change_colour()
        tim.pencolor(colour)
        tim.fillcolor(colour)
        tim.begin_fill()
        print(colour)
        tim.dot(30)
        tim.end_fill()
        tim.penup()
        tim.forward(100)
        tim.pendown()
    tim.penup()
    tim.goto(-920, -470 + x )



































screen = t.Screen()
screen.screensize(670, 670)
screen.exitonclick()

