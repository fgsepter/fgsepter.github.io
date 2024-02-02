from PIL import Image
import os

def create_thumbnail(input_path, output_path, size=(128, 128)):
    try:
        with Image.open(input_path) as img:
            img.thumbnail(size)
            img.save(output_path)
            print(f"Thumbnail saved as {output_path}")
    except IOError as e:
        print(f"Error creating a thumbnail for {input_path}: {e}")

# Usage
folders = ['Coat', 'Dress', 'Hoodie', 'Long-Sleeve', 'Pants', 'Shorts', 'Skirt', 'Summer', 'Sweater', 'Tshirt', 'Cardigan']
for folder in folders:
    for i in range(1,100):
        input_image = f'687/{folder}/{i}.png'
        if not os.path.exists(input_image):
            break
        output_image = f'687/{folder}/{i}_thumb.png'
        thumbnail_size = (200, 200)
        create_thumbnail(input_image, output_image, thumbnail_size)