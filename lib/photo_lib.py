import random

from PIL import Image, ImageDraw, ImageFont, ImageOps

from lib.config import config
from lib.file_path import FONT_PATH, TEXT_PATH


def create_image(size, bg_color, message):

    font = ImageFont.truetype(str(FONT_PATH), config['font_size'])
    font_color = config['font_color']

    W, H = size

    img = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(img)

    _, _, w, h = draw.textbbox((0, 0), message, font=font)

    draw.text(((W - w) / 2, (H - h) / 2), message, font=font, fill=font_color)
    return img


def add_border(img):
    color = config['border_color']
    border = config['border_size']
    img = ImageOps.expand(img, border=border, fill=color)
    return img


def get_text_length():
    with open(TEXT_PATH, 'r', encoding='utf-8') as f:
        text_list = f.read().splitlines()
    return len(text_list)


def generate_images():
    with open(TEXT_PATH, 'r', encoding='utf-8') as f:
        text_list = f.read().splitlines()

    for i in range(len(text_list)):
        img = create_image(
            config["image_size"],
            config["image_color"],
            text_list[i].replace('/', '\n'),
        )
        img = add_border(img)
        img.save(f'output/{i}.png', 'PNG')


def concatenate_images():

    text_length = get_text_length()

    nums = random.sample([i for i in range(text_length)], k=text_length)

    result = None

    for i in range(5):

        temp = Image.open(f'output/{nums[i*5]}.png')

        for j in range(1, 5):

            img = Image.open(f'output/{nums[j + i*5]}.png')

            temp = get_concat_h(temp, img)

        if not result:
            result = temp
        else:
            result = get_concat_v(result, temp)

    return result


def get_concat_h(im1, im2):
    img = Image.new('RGB', (im1.width + im2.width, im1.height))
    img.paste(im1, (0, 0))
    img.paste(im2, (im1.width, 0))
    return img


def get_concat_v(im1, im2):
    img = Image.new('RGB', (im1.width, im1.height + im2.height))
    img.paste(im1, (0, 0))
    img.paste(im2, (0, im1.height))
    return img


def create_bingo_sheet(file_path):
    img = concatenate_images()
    img.save(file_path, 'PNG')
