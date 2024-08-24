import numpy as np
import cv2

# Load images
img_color = cv2.imread('./image/logo.png', cv2.IMREAD_COLOR)
img_gray = cv2.imread('./image/logo.png', cv2.IMREAD_GRAYSCALE)

# Check if the images are loaded successfully
if img_color is None:
    print("Error: Could not load color image './image/logo.png'")

if img_gray is None:
    print("Error: Could not load grayscale image './image/logo.png'")

# Set desired width and height
desired_width = 300  # Example width
desired_height = 200  # Example height

# Resize images if they are loaded correctly
if img_color is not None:
    img_color= cv2.resize(img_color, (desired_width, desired_height))

if img_gray is not None:
    img_gray= cv2.resize(img_gray, (desired_width, desired_height))

# Display resized images
if img_color is not None:
    cv2.imshow('Color Image', img_color)

if img_gray is not None:
    cv2.imshow('Grayscale Image', img_gray)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print shape and first channel of the resized color image
if img_color is not None:
    print("Color image shape:", img_color.shape)
    print("First channel (Blue) of color image:\n", img_color[:, :, 0])
