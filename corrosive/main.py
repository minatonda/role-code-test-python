


# from PIL import Image
# from numpy import array_equiv, asarray, ndarray


# def find_diff(img_arr_a: ndarray, img_arr_b: ndarray):
#     y_len = len(img_arr_a)
#     x_len = len(img_arr_a[0])

#     diff_points = []

#     y = 0
#     while y < y_len:
#         x = 0
#         while x < x_len:
#             same = array_equiv(img_arr_a[y][x], img_arr_b[y][x])
#             if not same:
#                 diff_points.append([y, x])
#             x += 1
#         y += 1

#     return diff_points


# def sharp_diff(img_arr_a: ndarray, img_arr_b: ndarray, diff: list):
#     y_len = len(img_arr_a)
#     x_len = len(img_arr_a[0])

#     diff_points = []

#     for y, x in diff:
#         val_a = img_arr_a[y][x]
#         val_b = img_arr_b[y][x]

#         diff_points.append([y, x])

#     return diff_points


# def highlight_diff(img_arr_a: ndarray, diff: list):
#     img_arr_new = img_arr_a.copy()

#     for y, x in diff:
#         img_arr_new[y][x] = [255, 0, 0]

#     return img_arr_new


# img_a = Image.open("./data/0.jpg")
# img_b = Image.open("./data/1.jpg")

# img_arr_a = asarray(img_a)
# img_arr_b = asarray(img_b)

# res_diff = find_diff(img_arr_a, img_arr_b)
# res_diff_sharpen = sharp_diff(img_arr_a, img_arr_b, res_diff)
# # print(res_diff)
# res_diff_highlighted = highlight_diff(img_arr_a, res_diff)

# im = Image.fromarray(res_diff_highlighted)
# im.save("./data/3.jpg")
