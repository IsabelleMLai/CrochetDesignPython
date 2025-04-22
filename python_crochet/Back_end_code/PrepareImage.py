from rembg import remove
from PIL import Image
import numpy as np

#Removes the background of an image, makes background transparent
#   takes input path, saves cleared image into the output path given
def RemoveBackGround(input_path, output_path):
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_image.save(output_path)


# Retrieves pixel data from a PNG image.
# Returns:
#         A list of tuples, where each tuple represents a pixel's RGBA values (Red, Green, Blue, Alpha).
def GetPixelData(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGBA")  # Ensure the image is in RGBA format
        pixel_data = np.array(img)
        return pixel_data
    except FileNotFoundError:
        print(f"Error at  GetPixelData: Image file not found at '{image_path}'")
        return None
    except Exception as e:
         print(f"Error at  GetPixelData: An error occurred: {e}")
         return None
    

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
def CropImage(image_path, coordinates, output_path):
    try:
        img = Image.open(image_path)
        cropped_img = img.crop(coordinates)
        cropped_img.save(output_path)
    except FileNotFoundError:
        print(f"Error at CropImage: Image file not found at {image_path}")
    except Exception as e:
        print(f"Error at CropImage: An error occurred: {e}")


