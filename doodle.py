from nbt_structure_utils import NBTStructure, Vector, Cuboid, BlockData
nbtstructure = NBTStructure()
c1, c2 = Vector(0, 0, 0), Vector(4, 4, 4)
nbtstructure.fill(Cuboid(c1, c2), BlockData("stone"))
nbtstructure.get_nbt().write_file(filename="nbts\\hollow_box.nbt")