import cv2
import os

def process_image_pipeline(image_path, filename_prefix):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Heatmap
    heatmap = cv2.applyColorMap(img, cv2.COLORMAP_JET)
    cv2.imwrite(f"static/uploads/{filename_prefix}_heatmap.jpg", heatmap)
    # Edges
    edges = cv2.Canny(img, 100, 200)
    cv2.imwrite(f"static/uploads/{filename_prefix}_edges.jpg", edges)
    # Mask
    _, mask = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(f"static/uploads/{filename_prefix}_mask.jpg", mask)
    
    return {
        "original": f"uploads/{filename_prefix}_orig.jpg",
        "heatmap": f"uploads/{filename_prefix}_heatmap.jpg",
        "edges": f"uploads/{filename_prefix}_edges.jpg",
        "mask": f"uploads/{filename_prefix}_mask.jpg"
    }