from PIL import Image
import cv2
import numpy as np
import math



# Retrieves pixel data from a PNG image.
# Returns:
#         A list of tuples, where each tuple represents a pixel's RGBA values (Red, Green, Blue, Alpha).
def RGBA_PixelData(image):
    img = image.convert("RGBA")  # Ensure the image is in RGBA format
    pixel_data = np.array(img)
    return pixel_data

#does reverse; convert arr to img 
def PixelData_RGBA(pixels):
    return Image.fromarray(pixels, 'RGBA')

def PixelData_RGB(pixels):
    return Image.fromarray(pixels, 'RGB')



#Removes the background of an image, makes background transparent
#   takes input path, saves cleared image into the output path given
def RemoveBackGround(pixels):
    (num_rows, num_cols) = pixels[:,:,0].shape

    for r  in range(num_rows):
        for c in  range(num_cols):
            if pixels[r][c][0] > 100:
                pixels[r][c][0] = 255
                pixels[r][c][1] = 255
                pixels[r][c][2] = 255
                pixels[r][c][3] = 0
    return pixels
    


# Get bounds for the image, want to center the part of  the  image that isn't transparent,
# minimize image size
# ARGS:
    #alpha_channel = 2d array, alpha pixel values of the image
#RETURN:
    #returns tuple of image edge locations (left, upper, right, lower)
def GetImgBounds(alpha_channel):
    (num_rows, num_cols) = alpha_channel.shape

    left_edge = num_cols
    right_edge = 0
    top_edge = num_rows
    bottom_edge  = 0

    for row  in range(num_rows):
        for col in range(num_cols):
            if alpha_channel[row][col] != 0:
                if col  < left_edge:
                    left_edge =  col
                if col > right_edge:
                    right_edge = col
                if row < top_edge:
                    top_edge = row
                if row > bottom_edge:
                    bottom_edge = row
    return (left_edge, top_edge, right_edge, bottom_edge)
        

# Crops an image using the given coordinates.
#Args:
        # image_path (str): Path to the input image.
        # coordinates (tuple): Tuple of (left, upper, right, lower) coordinates.
        # output_path (str): Path to save the cropped image.
def CropImage(coordinates, image):
    cropped_img = image.crop(coordinates)
    return cropped_img
   


#resizes an image by a ratio of the original size 0-1 = smaller, >1 = larger
    #save to output_path = Images_resize
def Resize(ratio, image):
    width, height  = image.size
    
    new_width = math.floor(ratio*width)
    new_height = math.floor(ratio*height)

    resized_img = image.resize((new_width, new_height), Image.LANCZOS)
    return resized_img





#rotate an image by an angle, make sure to not cut off anything from the photo
def Rotate_KeepFullImg(angle, image, output_path):

    # Convert PIL image to NumPy array
    numpy_image = np.array(image)
    # Convert RGB to BGR (OpenCV's default color format)
    image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)

    # Taking image height and width 
    # image =  cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    height, width = image.shape[:2]
    image_center = (width/2, height/2)

    rotation_matrix = cv2.getRotationMatrix2D(image_center, angle, 1.)

    abs_cos = abs(rotation_matrix[0,0])
    abs_sin = abs(rotation_matrix[0,1])

    new_width = int(height * abs_sin + width * abs_cos)
    new_height = int(height * abs_cos + width * abs_sin)

    rotation_matrix[0, 2] += new_width/2 - image_center[0]
    rotation_matrix[1, 2] += new_height/2 - image_center[1]

    rotated_image = cv2.warpAffine(image, rotation_matrix, (new_width, new_height), borderMode=cv2.BORDER_CONSTANT, borderValue=(255,255,255))

    cv2.imwrite(output_path, rotated_image)



