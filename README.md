## Introduction to this project

This project aims to create a pixel artwork out of the lighting mechanism of certain shaders. 


## Progress
Install Optifine in Minecraft 1.20.4. Replace the shaderpacks folder with the provided folder in the repo. 

In a superflat world, put a 100*100 layer of white concrete on y=-61, and a layer of the same shape on y=100 composed of different kinds of blocks to create shadows. The viewer looks downwards at y=35. 

test_for_scale.py does the testing job. Fill the 100*100 layer on y=100 with identical blocks, look downwards the way described above, and take a screenshot. Crop the screenshot and save it in the "tests" folder in the repo, named as "\<blockname>.png". Run test_for_scale.py, test_results.json will be generated to include the matching greyscale of the shadows cast by each kind of block. 

After sufficient testing, place the source images in "source_folder", and run "generate_nbt.py". The generation process may take long, and the resulting nbt files will be stored in the "nbts" folder. 


## Running requirements
Run the python source files with Python 3.11.5 installed with the following packages: 
joblib              1.3.2
NBT                 1.5.1
nbt-structure-utils 0.3.0
numpy               1.26.3
pillow              10.2.0
pip                 22.3.1
scikit-learn        1.4.0
scipy               1.12.0
setuptools          65.5.1
threadpoolctl       3.2.0
wheel               0.38.4