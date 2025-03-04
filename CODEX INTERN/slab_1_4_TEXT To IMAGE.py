from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# Function to convert text to image
def text_to_image(text, font_size=40, image_size=(800, 400), font_path="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
    # Create a blank white image
    img = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(img)

    # Load font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print("Font not found, using default.")
        font = ImageFont.load_default()

    # Calculate text position (centered)
    text_size = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_size[2], text_size[3]
    position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)

    # Draw text on the image
    draw.text(position, text, fill="black", font=font)

    # Show the image
    plt.imshow(img)
    plt.axis("off")
    plt.show()

    # Save image
    img.save("text_image.png")
    print("Image saved as 'text_image.png'.")

# Get user input text
user_text = input("Enter text to convert into an image: ")
text_to_image(user_text)

