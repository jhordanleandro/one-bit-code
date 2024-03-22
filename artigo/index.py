from PIL import Image, ImageEnhance

# Load the image
img_path = '/home/jhordan/downloads/Chapeu De Lampião.jpeg'
image = Image.open(img_path)

# Enhance the brightness
enhancer = ImageEnhance.Brightness(image)
brightened_image = enhancer.enhance(1.2)  # Increase brightness by 20%

# Save the brightened image
brightened_img_path = '/home/jhordan/downloads/brightened_Chapeu_De_Lampião.jpeg'
brightened_image.save(brightened_img_path)
brightened_img_path
