from skimage import color, io, measure, img_as_ubyte
from skimage.measure import profile_line
from skimage.transform import rescale, resize
import matplotlib.pyplot as plt
import numpy as np
import pydicom as dicom

# Directory containing data and images
in_dir = "data/"

# X-ray image
im_name = "metacarpals.png"

# Read the image.
# Here the directory and the image name is concatenated
# by "+" to give the full path to the image.
im_org = io.imread(in_dir + im_name)
print(im_org.shape)

print(im_org.dtype)
#Exercise 4: Display the image and try to use the simple viewer tools like the zoom tool to inspect the finger bones. You can see the pixel values at a given pixel position (in x, y coordinates) in the upper right corner. Where do you see the highest and lowest pixel values?
#In the bottom right corner is the highest (512,512) and in top left is lowest (0,0)
#io.imshow(im_org)
#plt.title('Metacarpal image')
#io.show()

#Exercise 5: Display an image using colormap:

#Exercise 6: Experiment with different colormaps. For example cool, hot, pink, copper, coolwarm, cubehelix, and terrain.
#io.imshow(im_org, cmap="cubehelix")
#plt.title('Metacarpal image (with colormap)')
#io.show()

#Exercise 7: Try to find a way to automatically scale the visualization, so the pixel with the lowest value in the image is shown as black and the pixel with the highest value in the image is shown as white.

# Had to use the flatten() method

#max_value=max(im_org.flatten())
#min_value=min(im_org.flatten())
#io.imshow(im_org, vmin=min_value, vmax=max_value)
#plt.title('Metacarpal image (with gray level scaling)')
#io.show()

#Exercise 8: Compute and visualise the histogram of the image:

plt.hist(im_org.ravel(), bins=256)
plt.title('Image histogram')
io.show()

#Since the histogram functions takes 1D arrays as input, the function ravel is called to convert the image into a 1D array.
#The bin values of the histogram can also be stored by writing:

h = plt.hist(im_org.ravel(), bins=256)

#The value of a given bin can be found by:

bin_no = 100
count = h[0][bin_no]
print(f"There are {count} pixel values in bin {bin_no}")

#Here h is a list of tuples, where in each tuple the first element is the bin count and the second is the bin edge. So the bin edges can for example be found by:

bin_left = h[1][bin_no]
bin_right = h[1][bin_no + 1]
print(f"Bin edges: {bin_left} to {bin_right}")

#Here is an alternative way of calling the histogram function:

y, x, _ = plt.hist(im_org.ravel(), bins=256)

#Exercise 9: Use the histogram function to find the most common range of intensities? (hint: you can use the list functions max and argmax).
h = plt.hist(im_org.ravel(), bins=256)
max_bincount = np.argmax(h[0])
print("max_bincount " + str(h[0][max_bincount]))
print("bin_edge left "+ str(h[1][max_bincount]))
print("bin_edge right "+ str(h[1][max_bincount+1]))

#Exercise 10: What is the pixel value at (r, c) = (110, 90) ?

r = 100
c = 50
im_val = im_org[r, c]
print(f"The pixel value at (r,c) = ({r}, {c}) is: {im_val}")

r = 110
c = 90

print(f"The pixel value at (r,c) = ({r}, {c}) is: {im_val}")