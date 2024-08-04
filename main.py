import os
import subprocess

def main():
    while True:
        # Ask the user if they want to generate a new QR code, use an existing image, or exit
        print("\nMenu:")
        print("1. Generate a new QR code")
        print("2. Use an existing image")
        print("3. Exit")
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == '1':
            # Step 1: Generate QR code with user input
            subprocess.run(["python", "generate_qr_code_with_input.py"])
            image_path = "smartscan_image.png"
        elif choice == '2':
            # Ask for the path to the existing image
            image_path = input("Enter the path to the existing image: ").strip()
            if not os.path.exists(image_path):
                print("The specified image does not exist.")
                continue
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        # Step 2: Register user from the QR code
        from smartscan_registration_module import RegisterUserFromSmartScan
        RegisterUserFromSmartScan(image_path)

if __name__ == "__main__":
    main()
