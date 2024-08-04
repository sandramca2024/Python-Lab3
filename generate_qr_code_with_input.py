import cv2

# In-memory storage
users = []

# Lambda functions
create_user = lambda artist_name, class_type, artist_email, artist_phone: {
    "artist_name": artist_name,
    "class_type": class_type,
    "artist_email": artist_email,
    "artist_phone": artist_phone,
}
insert_user = lambda user: users.append(user)
fetch_all_users = lambda: users

# Function to read and decode SmartScan Code using OpenCV
def read_smartscan_code(image_path):
    try:
        img = cv2.imread(image_path)
        detector = cv2.QRCodeDetector()
        data, points, _ = detector.detectAndDecode(img)
        if data:
            return data
        else:
            print("No data found in the code.")
    except Exception as e:
        print(f"Error reading the SmartScan Code: {e}")
    return ""

# User Registration Function
def RegisterUserFromSmartScan(image_path):
    user_data = read_smartscan_code(image_path)
    if user_data:
        try:
            artist_name, class_type, artist_email, artist_phone = user_data.split(',')
            new_user = create_user(artist_name, class_type, artist_email, artist_phone)
            insert_user(new_user)
            print(fetch_all_users())
        except ValueError:
            print("Invalid data format in SmartScan Code.")
    else:
        print("Failed to decode the SmartScan Code.")
