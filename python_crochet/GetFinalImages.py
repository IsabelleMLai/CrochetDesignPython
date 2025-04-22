from Back_end_code.PrepareImage import *
import math
import os


####################################################
# clears all .png images from an image folder
def ClearFolder(folder_name):
    for filename in os.listdir(folder_name):
        if filename.endswith('.png'):
            os.remove(os.path.join(folder_name, filename))

# deletes a folder
def DelFolder(folder_name):
    ClearFolder(folder_name)
    os.rmdir(folder_name)
    print(f"Deleted: {folder_name}")
####################################################


####################################################
# prepares initial raw photo (PNG type)
    # gets rid  of background and extra space
def PrepNewImg(stitch):
    orig_img_path = "./Images/"+stitch+".png"

    final_img_name = stitch+ "_final.png"
    final_img_path = "./Images_final/"+final_img_name

    image = Image.open(orig_img_path)

    
    ######## clear image background
    #RGBA_PixelData returns 3d numpy array  of pixel data (RGBA)
    pixels = RGBA_PixelData(image)
    pix_transparent = RemoveBackGround(pixels)

    ######### to get rid of extra space around img
    alpha_channel = pix_transparent[:,:,3]
    new_image_bounds = GetImgBounds(alpha_channel)
    #convert pixel data back into img to easily crop
    img  =  PixelData_RGBA(pix_transparent)
    cropped_img = CropImage(new_image_bounds, img)
    cropped_img.save(final_img_path)
####################################################



####################################################
#rotates and prepares images in a folder for magic circle placement
def MagicCircImages(stitch, num_sts):
    folder_name = "Images_"+stitch+"_MagicCirc_"+str(num_sts)
    os.mkdir(folder_name)

    img_name = stitch+ "_final.png"
    img_path = "./Images_final/"+img_name
    image = Image.open(img_path)

    ######### to rotate img
    #saves to final img path  since using cv2
    angle_increment = math.floor(360/num_sts)
    curr_angle = 0
    for i in range(num_sts):
        MC_img_name = img_name[:(len(img_name)-4)] + "_"+ str(curr_angle)+".png"
        MC_img_path = "./"+folder_name+"/"+MC_img_name
        Rotate_KeepFullImg(curr_angle, image, MC_img_path)

    ######### to finalize images
    #reopen image for PIL
        image_rotated = Image.open(MC_img_path)
        pixels_fin = RGBA_PixelData(image_rotated)
        pix_transparent_fin = RemoveBackGround(pixels_fin)

        alpha_channel_fin = pix_transparent_fin[:,:,3]
        new_image_bounds_fin = GetImgBounds(alpha_channel_fin)
        img_fin  =  PixelData_RGBA(pix_transparent_fin)
        cropped_img_fin = CropImage(new_image_bounds_fin, img_fin)
        # cropped_img_fin.save(final_img_path)

        ratio = 0.5
        resized = Resize(ratio, cropped_img_fin)
        resized.save(MC_img_path)

        curr_angle += angle_increment
####################################################


