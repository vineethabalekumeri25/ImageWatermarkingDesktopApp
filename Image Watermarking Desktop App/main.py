from tkinter import Tk, filedialog, Canvas, Button, Label, Entry
from PIL import Image, ImageDraw, ImageFont, ImageTk

# Global variable to store image path
image_path = ""

def select_image():
    global image_path
    # Open a file dialog to select an image
    image_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
    )
    if image_path:
        # Display the selected image
        img = Image.open(image_path)
        img.thumbnail((300, 300))  # Resize for display
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(150, 150, image=img_tk)
        canvas.image = img_tk  # Keep reference to avoid garbage collection


from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog

from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont

from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont

def apply_watermark():
    global image_path
    if not image_path:
        messagebox.showerror("Error", "Please select an image first!")
        return

    watermark_text = watermark_entry.get()
    if not watermark_text:
        messagebox.showerror("Error", "Please enter a watermark text!")
        return

    try:
        # Open the image
        img = Image.open(image_path)
        img = img.convert("RGBA")  # Ensure image is in RGBA mode for transparency

        # Initialize ImageDraw to add text
        draw = ImageDraw.Draw(img)

        # Set a very large bold font (ensure 'arialbd.ttf' is available or use default)
        try:
            font = ImageFont.truetype("arialbd.ttf", 150)  # Arial Bold, size 150
        except IOError:
            font = ImageFont.load_default()  # Fallback to default font if Arial is not found

        # Calculate text size using bounding box
        text_width, text_height = draw.textbbox((0, 0), watermark_text, font=font)[2:4]

        # Ensure that the text dimensions are valid
        if text_width == 0 or text_height == 0:
            messagebox.showerror("Error", "Error calculating text size.")
            return

        # Position: center of the image
        position = ((img.width - text_width) // 2, (img.height - text_height) // 2)

        # Draw the watermark text in bold and white
        draw.text(position, watermark_text, font=font, fill=(255, 255, 255))  # White color

        # Save the watermarked image
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png", filetypes=[("Image Files", "*.png;*.jpg")]
        )
        if save_path:
            img.save(save_path)
            messagebox.showinfo("Success", "Watermark applied and image saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error applying watermark: {e}")
        print(f"Exception: {e}")  # Print out the exception for debugging

# Tkinter setup
window = Tk()
window.title("Image Watermarking App")
window.geometry("400x500")

# Widgets
canvas = Canvas(window, width=300, height=300, bg="pink")
canvas.pack(pady=10)

select_button = Button(window, text="Select Image", command=select_image, bg="light blue")
select_button.pack()

watermark_label = Label(window, text="Enter Watermark Text:")
watermark_label.pack()

watermark_entry = Entry(window, width=30)
watermark_entry.pack()

apply_button = Button(window, text="Apply Watermark", command=apply_watermark, bg="light green")
apply_button.pack(pady=10)

error_label = Label(window, text="", fg="red")
error_label.pack()

window.mainloop()