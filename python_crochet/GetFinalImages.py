from Back_end_code.PrepareImage import *

#change this only:
    #assume image is PNG type
orig_img_name = "HDC.png"

orig_img_path = "./Images/"+orig_img_name
clear_img_name  = orig_img_name[:(len(orig_img_name)-4)] + "_clear.png"
clear_img_path = "./Images_clear/"+clear_img_name
center_img_name = orig_img_name[:(len(orig_img_name)-4)] + "_center.png"
center_img_path = "./Images_center/"+center_img_name

########################################################
######## UNCOMMENT: to clear image background

# RemoveBackGround(orig_img_path, clear_img_path)
########################################################



########################################################
######## UNCOMMENT: to center the image

# #GetPixelData returns 3d numpy array  of pixel data (RGBA)
# pixels = GetPixelData(clear_img_path)
# alpha_channel = pixels[:,:,3]

# new_image_bounds = GetImgBounds(alpha_channel)
# CropImage(clear_img_path, new_image_bounds, center_img_path)
########################################################



########################################################
######## UNCOMMENT: 

########################################################