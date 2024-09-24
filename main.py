from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import *

# 1. Create tkinter window
window = Tk()
window.title("Image watermark application")
window.config(pady=50, padx=50)


def add_watermark():
    file_path = filedialog.askopenfilename(title="Open image",
                                           filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
    if file_path:
        display_image(file_path)


def display_image(file_path):
    # Open the image
    image = Image.open(file_path)
    image = image.resize((400, 400))  # Resize image to fit the window

    # Create a draw object to add text (watermark)
    draw = ImageDraw.Draw(image)

    # Add the watermark text at the bottom right of the image
    text = "digitibetlab.com"

    # Set the font (you may need to adjust the path to a .ttf file if not found)
    try:
        font = ImageFont.truetype("arial.ttf", 36)  # You can replace "arial.ttf" with a different font file
    except IOError:
        font = ImageFont.load_default()  # Use default font if the specified one is not found

    # Get the width and height of the image and the text
    text_width, text_height = draw.textlength(text, font=font)
    width, height = image.size

    # Position the text at the bottom right
    position = (width - text_width - 10, height - text_height - 10)

    # Add the text (watermark)
    draw.text(position, text, (255, 255, 255), font=font)

    # Convert the image with the watermark to a format Tkinter can display
    photo = ImageTk.PhotoImage(image)

    # Display the image with the watermark
    image_label.config(image=photo)
    image_label.photo = photo  # Keep a reference to avoid garbage collection


# Label for displaying the image (initially shows a message)
image_label = Label(window, text="Add watermark", font=("Ariel", 18, "bold"), pady=20)
image_label.grid(row=0, column=1)

# Button for selecting a file
button1 = Button(window, text="Select File", background="Blue", highlightthickness=1, command=add_watermark)
button1.grid(row=2, column=1)

window.mainloop()
