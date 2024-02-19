import time
from nbt_structure_utils import NBTStructure, Vector, BlockData
import json
from PIL import Image
import os
from test_for_scale import grey
import numpy as np
from sklearn.neighbors import NearestNeighbors

edge_num_blocks = 100
canvas_origin = Vector(0, 1, 0)
cover_origin = Vector(0, 162, 0)

with open("test_results.json", "r") as f:
    test_results = json.load(f)
keys_num = list(map(float, list(test_results.keys())))
neighbour_model = NearestNeighbors(n_neighbors=1)
neighbour_model.fit(np.array(keys_num).reshape(-1, 1))


def main():
    source_folder = "source_folder"
    for file_name in list(os.walk(source_folder))[0][2]:
        image = Image.open(os.path.join(source_folder, file_name)).convert("RGB")
        image_name = file_name.split(".")[0]
        width, height = image.size
        if width > height:
            new_width = round(width / height * 100)
            new_height = 100
        else:
            new_height = round(height / width * 100)
            new_width = 100
        new_image = image.resize((new_width, new_height), Image.BICUBIC)
        assert new_image.size == (new_width, new_height)
        # new_image.show()
        pixels = new_image.load()
        pixel_greyscale = np.zeros((new_width, new_height))
        for x in range(new_width):
            for y in range(new_height):
                # noinspection PyUnresolvedReferences
                r, g, b = pixels[x, y]
                pixel_greyscale[x, y] = round(grey(r, g, b), 2)

        structure = NBTStructure()
        structure.fill((canvas_origin, canvas_origin + Vector(new_width-1, 0, new_height-1)), BlockData("white_concrete"))
        for x in range(new_width):
            for y in range(new_height):
                scale = pixel_greyscale[x, y]
                found = keys_num[neighbour_model.kneighbors([[scale]], return_distance=False)[0][0]]
                block_name = test_results[str(found)]
                structure.set_block(cover_origin + Vector(x, 0, y), BlockData(block_name))
        structure.get_nbt().write_file(filename=os.path.join("nbts", image_name + ".nbt"))
        # Buggy! Unable to load too large structures, floors not loaded


if __name__ == "__main__":
    main()
