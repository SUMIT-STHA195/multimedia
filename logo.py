from PIL import Image, ImageDraw, ImageFont

# Create a new image with a white background
width, height = 600, 400
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Load a font
try:
    # Try to use a system font if available
    font = ImageFont.truetype("arial.ttf", 40)
except IOError:
    # If the system font is not available, use the default Pillow font
    font = ImageFont.load_default()

# Define colors
black = "black"
green = (34, 139, 34)
orange = (255, 165, 0)

# Draw shapes
# Circle in the center
circle_radius = 50
circle_center = (width // 2, height // 3)
draw.ellipse([circle_center[0] - circle_radius, circle_center[1] - circle_radius,
              circle_center[0] + circle_radius, circle_center[1] + circle_radius],
             outline=black, fill=green, width=5)

# Rectangle below the circle
rectangle_top_left = (width // 2 - 75, height // 3 + 75)
rectangle_bottom_right = (width // 2 + 75, height // 3 + 125)
draw.rectangle([rectangle_top_left, rectangle_bottom_right], outline=black, fill=orange)

# Diagonal line across the shapes
draw.line([circle_center[0] - circle_radius, circle_center[1] + circle_radius,
           rectangle_bottom_right[0], rectangle_top_left[1]],
          fill=black, width=5)

# Add text below the shapes
text = "Simple Logo"
text_width, text_height = draw.textsize(text, font=font)
text_x = (width - text_width) // 2
text_y = height - text_height - 50
draw.text((text_x, text_y), text, fill=black, font=font)

# Save the image
image.save("simple_logo.png")

# Display the image
image.show()
