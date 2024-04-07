import cv2
import requests

API_URL = "https://api-inference.huggingface.co/models/yangy50/garbage-classification"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()


def capture_photo():
    # Open the default camera (index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    # Capture a frame
    ret, frame = cap.read()

    if ret:
        # Display the captured frame
        cv2.imshow('Webcam', frame)
        # Save the captured frame as a photo
        cv2.imwrite('captured_photo.jpg', frame)
        print("Photo captured successfully")
        output = query("captured_photo.jpg")
        print(output)
    else:
        print("Error: Could not capture photo")

    # Release the camera
    cap.release()
    # Close the window after a key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    capture_photo()

