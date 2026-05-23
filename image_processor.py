import cv2
import os

# Create a folder to save processed images
output_folder = 'processed_images'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def process_and_save(image_path, save_name):
    # 1. Load the image
    img = cv2.imread(image_path)
    
    if img is None:
        print(f"Error: Could not find image at {image_path}")
        return

    # 2. Apply processing (e.g., Grayscale conversion)
    processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 3. Save the image automatically
    save_path = os.path.join(output_folder, save_name)
    cv2.imwrite(save_path, processed_img)
    
    print(f"Successfully saved: {save_path}")

# Example usage
# Replace 'your_xray_image.jpg' with your actual file path
process_and_save('your_xray_image.jpg', 'processed_xray.jpg')