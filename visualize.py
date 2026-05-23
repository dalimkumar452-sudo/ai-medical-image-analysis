import cv2
import matplotlib.pyplot as plt

def show_xray(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    plt.imshow(img, cmap='gray')
    plt.title("Sample Chest X-Ray")
    plt.axis('off')
    plt.show()

# Replace with your actual file path
# show_xray("data/train/NORMAL/IM-0115-0001.jpeg")