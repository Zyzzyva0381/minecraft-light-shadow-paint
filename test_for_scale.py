from PIL import Image
import os
from numpy import mean
import json

test_folder = "tests"


def grey(r, g, b):
    return r * 0.299 + g * 0.587 + b * 0.114


def main():
    print("Testing images...")
    grey_table = dict()
    for file_name in list(os.walk(test_folder))[0][2]:
        image = Image.open(os.path.join(test_folder, file_name)).convert("RGB")
        block_name = file_name.split(".")[0]
        pixels = image.load()
        width, height = image.size
        grey_list = []
        for x in range(width):
            for y in range(height):
                # noinspection PyUnresolvedReferences
                r, g, b = pixels[x, y]
                grey_list.append(grey(r, g, b))
        mean_grey = round(mean(grey_list), 2)
        grey_table[mean_grey] = block_name
        print(file_name, "is tested")
    with open("test_results.json", "w") as f:
        json.dump(grey_table, f)


if __name__ == "__main__":
    main()
