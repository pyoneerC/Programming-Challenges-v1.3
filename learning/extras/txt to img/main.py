from PIL import Image, ImageDraw, ImageFont

# Open the background image
background = Image.open('C:\\Users\\User\\Desktop\\prog chall py\\learning\\extras\\txt to img\\sub.png')

# Open the text file and read its content
with open('C:\\Users\\User\\Desktop\\prog chall py\\learning\\extras\\txt to img\\text.txt', 'r') as file:
    text = file.read()

# Get a font and text size that will fit the entire text on the image (centered)
font = ImageFont.truetype('arial.ttf', 36) # text font and size
text_width, text_height = font.getsize(text)
while text_width > background.width or text_height > background.height: # text not too long
    font = ImageFont.truetype('arial.ttf', font.size - 1)
    text_width, text_height = font.getsize(text)

# Create a new image drawer and draw the text on the image (centered)
draw = ImageDraw.Draw(background)
text_pos = ((background.width - text_width) / 2, (background.height - text_height) / 2) # centered
draw.text(text_pos, text, font=font, fill=(0, 0, 0))

# Save the image as a PNG file
background.save('C:\\Users\\User\\Desktop\\prog chall py\\learning\\extras\\txt to img\\result.png')
