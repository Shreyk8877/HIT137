# QUESTION 2
# CHAPTER 1: THE GATEKEEPER

import time
from PIL import Image

# Generate the number (n) based on time
current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

# Load the image 
img=Image.open("D:/CDU IT/HIT137 - Software now/Assignment 2/chapter1.jpg")
             
# Get the image dimensions
width, height=img.size
pixels=img.load()

# Initialize redkey to store the total sum of red values
redkey = 0

# Iterate over all the pixels in the image
for x in range(width):
    for y in range(height):
        # Get the RGB values of the pixel at position (x, y)
        r, g, b = pixels[x, y]

        # Add the generated number to each color channel, ensuring the values don't exceed 255
        new_r = min(r + generated_number,255)
        new_g = min(g + generated_number,255)
        new_b = min(b + generated_number,255)

        # Update the pixel with the new RGB values
        pixels[x, y] = (new_r, new_g, new_b)

        # Add the new red channel values to redkey
        redkey += new_r
       
# Save the image
img.save("D:/CDU IT/HIT137 - Software now/Assignment 2/chapter1out.png")

# Print the generated number and the total red, green, and blue channel sums
print(f"Generated number: {generated_number}")
print(f"Total red pixel values in new imange(Redkey): {redkey}")


