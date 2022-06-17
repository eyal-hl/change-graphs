from math import ceil

from PIL import Image


def get_blank_image(img) -> Image.Image:
    return Image.new('RGB', img.size, (255, 255, 255))


def get_array_of_points(img) -> list:
    pixels = list(img.getdata())
    width, height = img.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    pixels_locations = []
    for w in range(width):
        points = 0
        height_sum = 0
        for h in range(height):
            if pixels[h][w] != (255, 255, 255, 255) and pixels[h][w] != (255, 255, 255):
                height_sum += h
                points += 1
        if points > 0:
            pixels_locations.append((w, ceil(height_sum / points)))
    return pixels_locations


def add_pixel(img, x, y, height, color, shadow_size: int, shadow_color: str):
    for i in range(height):
        cur_y = y - ceil(height / 2) + i
        if 0 <= cur_y < img.height:
            # somehow translates hex to the color in rgb format
            img.putpixel((x, cur_y), tuple(int(color[i:i + 2], 16) for i in (0, 2, 4)))

    for i in range(shadow_size):
        cur_y = y - ceil(height / 2) - 1 - i
        if 0 <= cur_y < img.height:
            # somehow translates hex to the color in rgb format
            img.putpixel((x, cur_y), tuple(int(shadow_color[i:i + 2], 16) for i in (0, 2, 4)))

        cur_y = y + ceil(height / 2) + i
        if height % 2:
            cur_y -= 1
        if 0 <= cur_y < img.height:
            # somehow translates hex to the color in rgb format
            img.putpixel((x, cur_y), tuple(int(shadow_color[i:i + 2], 16) for i in (0, 2, 4)))


def remove_sides(img: Image.Image) -> Image.Image:
    pixels = list(img.getdata())
    width, height = img.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    min_point = width
    max_point = 0
    for h in range(height):
        for w in range(width):
            if not min_point < w < max_point and pixels[h][w] != (255, 255, 255, 255) and pixels[h][w] != (
                    255, 255, 255):
                if w < min_point:
                    min_point = w
                if w > max_point:
                    max_point = w

    return img.crop((min_point, 0, max_point + 1, height))


def handle(img: Image.Image, colors: dict, height: int, shadow_size: int):
    cropped_img = remove_sides(img)
    re = get_blank_image(cropped_img)

    for x, y in get_array_of_points(cropped_img):
        add_pixel(re, x, y, height, get_color(colors, x / cropped_img.width), shadow_size,
                  list(colors.values())[len(colors) - 1])
    return re


if __name__ == '__main__':
    print("re")


def get_color(colors: dict, num):
    keys = list(colors.keys())
    num *= keys[len(keys) - 1]
    for key in list(reversed(keys)):
        if num > float(key):
            return colors.get(key)
    return colors.get(0)


