from helper_functions import *

#-----------------------FILL IN THE FOLDER WHERE YOUR IMAGE EXISTS--------------------------
datafolder = "images/"
imgpath = datafolder + "1.jpg" 
#----------------------------------------STARTER CODE----------------------------------------
# Convert the color image to grayscale and returns the grayscale pixels 
pixel_values = read_colorimg(imgpath)
# The returned pixel values INCLUDE 2 boundary rows and 2 boundary colns. Therefore,
numb_rows = len(pixel_values) - 2
numb_colns = len(pixel_values[0]) - 2
#
#----------------------------------------WRITE YOUR CODE HERE----------------------------------------
#TODO 
    #Create a Empty 2D List with numb_rows * numb_colns

new_pixel_values = [[0 for _ in range(numb_colns)] for _ in range(numb_rows)]
# print(len(new_pixel_values), len(new_pixel_values[0]))


# Define the 3 x 3 mask as a tuple of tuples
mask = ((-1,-1,-1),(-1,8,-1),(1,-1,-1))

# Implement a function to slice a part from the image as a 2D list
def get_slice_2d_list(neighbour_pixels, x_coordinate, y_coordinate):
    sliced_list = [[each_pixel for each_pixel in row[y_coordinate-1:y_coordinate+2]] for row in neighbour_pixels[x_coordinate-1:x_coordinate+2]]
    return sliced_list

# Implement a function to flatten a 2D list or a 2D tuple
def flatten(matrix3x3):
    flattend_list = [pixel for row in matrix3x3 for pixel in row] 
    return flattend_list

# For each of the pixel values, excluding the boundary values
    # Create little local 3x3 box using list slicing
    neighbour_pixels = get_slice_2d_list()
    # Apply the mask
    mult_result = map(None, None, None)        
    # Sum all the multiplied values and set the new pixel value
#        
flat_mask = flatten(mask)
for x_coordinate in range(1, numb_rows+1):
    for y_coordinate in range(1, numb_colns+1):
        neighbour_pixels = get_slice_2d_list(pixel_values, x_coordinate, y_coordinate)
        flat_neighbours_list = flatten(neighbour_pixels)
        mult_result = list(map(lambda x,y: x*y, flat_neighbours_list, flat_mask))
        sigma_result = sum(mult_result)
        new_pixel_values[x_coordinate-1][y_coordinate-1] = sigma_result


#----------------------------------------END YOUR CODE HERE----------------------------------------
# Verify your result
verify_result(pixel_values, new_pixel_values, mask)
# View the original image and the edges of the image
view_images(imgpath, new_pixel_values)