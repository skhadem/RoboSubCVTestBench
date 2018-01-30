import cv2 as c
import numpy as np
import math


def find_max_min_x_y(lines):
    xs = []
    ys = []
    for i in lines:
        xs.append(i[0][0])
        xs.append(i[0][2])
        ys.append(i[0][1])
        ys.append(i[0][3])

    return([min(xs), max(xs)], [min(ys), max(ys)])

def find_die(lines):
    num_lines = len(lines)



    final_xs = [0,0]
    final_ys = [0,0]

    # first_point = [lines[0][0]]
    # xs = [first_point[0][0], first_point[0][2]]
    # ys = [first_point[0][1], first_point[0][3]]
    #
    # if ys[0] == ys[1]:
    #     for i in lines:
    #         if i[0][1] != i[0][3]:
    #             ys[0] = i[0][1]
    #             ys[1] = i[0][3]
    #             break
    references = find_max_min_x_y(lines)

    xs = references[0]
    ys = references[1]
    # print(xs)

    left_inc_x = 0
    right_inc_x = 0

    for i in lines:
        current_x = i[0][0]
        # print(current_x)

        if abs(xs[0] - current_x) < 15:
            final_xs[0] = final_xs[0] + current_x
            # print("left")
            left_inc_x = left_inc_x + 1
        elif abs(xs[1] - current_x) < 15:
            final_xs[1] = final_xs[1] + current_x
            right_inc_x = right_inc_x + 1
            # print("righxt")

        # print(final_xs)

        current_x = i[0][2]
        # print(current_x)
        if abs(xs[0] - current_x) < 15:
            final_xs[0] = final_xs[0] + current_x
            left_inc_x = left_inc_x + 1
            # print("left")
        elif abs(xs[1] - current_x)<15:
            final_xs[1] = final_xs[1] + current_x
            right_inc_x = right_inc_x + 1
            # print("right")

        #print(final_xs)

    # print(ys)
    left_inc_y = 0
    right_inc_y = 0
    for i in lines:
        current_y = i[0][1]
        # print(current_y)
        if abs(ys[0] - current_y)< 15:
            final_ys[0] = final_ys[0] + current_y
            left_inc_y = left_inc_y + 1

        elif abs(ys[1] - current_y)< 15:
            final_ys[1] = final_ys[1] + current_y
            right_inc_y = right_inc_y + 1
        current_y = i[0][3]
        # print(current_y)
        if abs(ys[0] - current_y)< 15:
            final_ys[0] = final_ys[0] + current_y
            left_inc_y = left_inc_y + 1

        elif abs(ys[1] - current_y)< 15:
            final_ys[1] = final_ys[1] + current_y
            right_inc_y = right_inc_y + 1
            # print("y worked")


    # print('increments:\n')
    # print(left_inc)
    # print(right_inc)

    final_xs[0] = final_xs[0]/left_inc_x
    final_xs[1] = final_xs[1]/right_inc_x
    final_ys[0] = final_ys[0]/left_inc_y
    final_ys[1] = final_ys[1]/right_inc_y
    # final_xs = [x / (left_inc) for x in final_xs]
    # final_ys = [y /(y_inc) for y in final_ys]


    return (final_xs, final_ys)


# img = c.imread('dice_num5.png', 1)
#
# dimensions = (480,360)
#
# img = c.resize(img, dimensions)
# edges = c.Canny(img, 100,200)
# edges = c.GaussianBlur(edges, (5,5),0)
#
# circles = c.HoughCircles(edges,c.HOUGH_GRADIENT,2,60.0)
# print("lines:\n")
# lines = c.HoughLinesP(edges, 1, math.pi/180, 200)
# print(lines)
#
# print("\nTrying to find die:\n")
# die_sides = find_die(lines)
# print(find_die(lines))
#
# c.line(img, (die_sides[0][0], die_sides[1][0]), (die_sides[0][0], die_sides[1][1]), (255,248,56))
# c.line(img, (die_sides[0][0], die_sides[1][1]), (die_sides[0][1], die_sides[1][1]), (255,248,56))
# c.line(img, (die_sides[0][1], die_sides[1][1]), (die_sides[0][1], die_sides[1][0]), (255,248,56))
# c.line(img, (die_sides[0][1], die_sides[1][0]), (die_sides[0][0], die_sides[1][0]), (255,248,56))
#
# if lines is not None:
#     for i in lines:
#         c.line(img, (i[0][0], i[0][1]), (i[0][2], i[0][3]), (56, 66, 255))
# print('\ncircles:\n')
# print(circles)
# true_circles = []
# if circles is not None:
#     circles = np.uint16(np.around(circles))
#     for i in circles[0,:]:
#         #print(i)
#         radius = i[2]
#         center = [i[0], i[1]]
#
#         circle_is_good = 1
#
#         if center[0]+radius > max(die_sides[0]):
#             circle_is_good = 0
#         if center[0] - radius < min(die_sides[0]):
#             circle_is_good = 0
#         if center[1] + radius > max(die_sides[1]):
#             circle_is_good = 0
#         if center[1] - radius < min(die_sides[1]):
#             circle_is_good = 0
#
#         if circle_is_good:
#             c.circle(img, (i[0],i[1]), i[2],(81,204,81),2)
#             true_circles.append(i)
#
# print("\n--------------------\n")
# print("Dice is number %s"%len(true_circles))
# c.imshow('with_blur', edges)
# c.imshow('final', img)
# #final_image = np.hstack((edges, img))
# #c.imshow('here', final_image)
# c.waitKey(0)
# c.destroyAllWindows()

def show_images(images):
    #print(images)
    for counter, image in enumerate(images):
        c.imshow('test_%s'%(counter+1), image)
        c.moveWindow('test_%s'%(counter+1), 200, 200)

    c.waitKey(0)
    c.destroyAllWindows()

def detect_number(images):
    dimensions = (480,360)

    images_to_return = []
    for img in images:
        img = c.resize(img, dimensions)

        edges = blurAndFilter(img)

        circles = c.HoughCircles(edges,c.HOUGH_GRADIENT,2,70.0)

        lines = c.HoughLinesP(edges, 1, math.pi/180, 200)
        die_sides = find_die(lines)

        c.line(img, (die_sides[0][0], die_sides[1][0]), (die_sides[0][0], die_sides[1][1]), (255,248,56))
        c.line(img, (die_sides[0][0], die_sides[1][1]), (die_sides[0][1], die_sides[1][1]), (255,248,56))
        c.line(img, (die_sides[0][1], die_sides[1][1]), (die_sides[0][1], die_sides[1][0]), (255,248,56))
        c.line(img, (die_sides[0][1], die_sides[1][0]), (die_sides[0][0], die_sides[1][0]), (255,248,56))

        if lines is not None:
            for i in lines:
                c.line(img, (i[0][0], i[0][1]), (i[0][2], i[0][3]), (56, 66, 255))


        true_circles = []
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0,:]:
                #print(i)
                radius = i[2]
                center = [i[0], i[1]]

                circle_is_good = 1

                if center[0]+radius > max(die_sides[0]):
                    circle_is_good = 0
                if center[0] - radius < min(die_sides[0]):
                    circle_is_good = 0
                if center[1] + radius > max(die_sides[1]):
                    circle_is_good = 0
                if center[1] - radius < min(die_sides[1]):
                    circle_is_good = 0


                if circle_is_good:
                    c.circle(img, (i[0],i[1]), i[2],(81,204,81),2)
                    true_circles.append(i)
        images_to_return.append(img)

    return images_to_return

def blurAndFilter(img):
    dimensions = (480,360)

    # img = c.resize(img, dimensions)
    edges = c.Canny(img, 100,200)
    edges = c.GaussianBlur(edges, (3,3),0)


    return edges


def main():
    images = []
    multiple_images = 1
    if multiple_images:
        for i in range(1,7):
            image_name = "dice_num%s.png"%i
            print(image_name)
            img = c.imread(image_name)
            images.append(img)
    else:
        img = c.imread("dice.png")
        images.append(img)

    images = detect_number(images)

    show_images(images)

if __name__== "__main__":
    main()
