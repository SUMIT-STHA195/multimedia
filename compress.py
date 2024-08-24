from PIL import Image
import os
def compress_image(input_image_path, output_image_path, quality=85):
    try:
        # Open the image file
        img = Image.open(input_image_path)
        # Compress the image and save it
        img.save(output_image_path, "JPEG", quality=quality, optimize=True)  
        # Show original and compressed image sizes
        original_size = os.path.getsize(input_image_path)
        compressed_size = os.path.getsize(output_image_path)
        
        print(f"Original Image Size: {original_size / 1024:.2f} KB")
        print(f"Compressed Image Size: {compressed_size / 1024:.2f} KB")
    except Exception as e:
        print(f"An error occurred: {e}")
def main():
    # Path to the image to compress
    input_image_path = "./image/logo.png"
    # Path to save the compressed image
    output_image_path = "compressed_image.jpg"
    # Set compression quality (1-100, lower is more compression)
    compression_quality = 60
    # Compress the image
    compress_image(input_image_path, output_image_path, quality=compression_quality)
if __name__ == "__main__":
    main()