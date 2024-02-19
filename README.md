## Introduction to this project

This project aims to create a pixel artwork out of the lighting mechanism of certain shaders. 


## Progress
Install Optifine in Minecraft 1.20.4. Replace the shaderpacks folder with the provided folder in the repo. 

In a superflat world, put a 100*100 layer of white concrete on y=-61, and a layer of the same shape on y=100 composed of different kinds of blocks to create shadows. The viewer looks downwards at y=35. 

test_for_scale.py does the testing job. Fill the 100*100 layer on y=100 with identical blocks, look downwards the way described above, and take a screenshot. Crop the screenshot and save it in the "tests" folder in the repo, named as "\<blockname>.png". Run test_for_scale.py, test_results.json will be generated to include the matching greyscale of the shadows cast by each kind of block. 