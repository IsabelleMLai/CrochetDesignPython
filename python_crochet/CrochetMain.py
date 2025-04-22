# ####### downloads to have:
#     #rembg = strip image of background


from GetUserInput import *
from ArrangeDiagram import *

from GetFinalImages import *


DelFolder("Images_MagicCirc")


# PrepNewImg("DC")
# PrepNewImg("HDC")
# PrepNewImg("SC")

MagicCircImages("DC", 15)


# magic_circ_num_st = int(Prompt_MagicCircNumSt())

# print(magic_circ_num_st)
# if magic_circ_num_st>20:
#     magic_circ_num_st = 20
# elif magic_circ_num_st < 3:
#     magic_circ_num_st = 3

# ShowMagicCirc(magic_circ_num_st)
