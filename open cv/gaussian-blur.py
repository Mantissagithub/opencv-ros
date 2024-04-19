import cv2

# Read the source image
src_img = cv2.imread('denise-jans-laoBHO09sU0-unsplash.jpg')

# Convert the image into grayscale if not already so
if len(src_img.shape) == 3:
    src_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blurring
ksize = (5, 5)  # Kernel size
sigmaX = 0     # Standard deviation along X direction; set automatically based on ksize
dst_img = cv2.GaussianBlur(src_img, ksize, sigmaX)

# Save the resultant image
cv2.imwrite('result_image.jpg', dst_img)