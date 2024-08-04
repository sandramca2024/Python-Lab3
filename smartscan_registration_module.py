import qrcode
import re

# Prompt user for input
artist_name = input("Enter artist name: ").strip()
class_type = input("Enter class type: ").strip()
artist_email = input("Enter artist email: ").strip()
artist_phone = input("Enter artist phone number: ").strip()

# Validate email format
if not re.match(r"[^@]+@[^@]+\.[^@]+", artist_email):
    print("Invalid email address.")
else:
    # Combine details into a single string
    artist_info = f"{artist_name},{class_type},{artist_email},{artist_phone}"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(artist_info)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the QR code image
    image_path = "smartscan_image.png"
    img.save(image_path)

    print(f"QR code saved as {image_path}")
