import cv2
import numpy as np

# Load the image
image = cv2.imread('flower.jpg')

# Get image dimensions
height, width = image.shape[:2]

# Define the scaling factors
scale_x = 0.5  # Scaling factor along the x-axis
scale_y = 0.5  # Scaling factor along the y-axis

# Perform scaling
scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y)

# Define the rotation angle
angle = 45  # Rotation angle in degrees

# Perform rotation
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Define the translation offsets
translation_x = 100  # Translation offset along the x-axis
translation_y = 50   # Translation offset along the y-axis

# Perform translation
translation_matrix = np.float32([[1, 0, translation_x], [0, 1, translation_y]])
translated_image = cv2.warpAffine(image, translation_matrix, (width, height))

# Display the original, scaled, rotated, and translated images
cv2.imshow('Original Image', image)
cv2.imshow('Scaled Image', scaled_image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
