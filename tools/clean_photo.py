# tools/clean_photo.py
import sys
import io
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def prepare_photo(input_path, output_path):
    print("✂️  Removing background with rembg...")
    with open(input_path, "rb") as f:
        input_bytes = f.read()
    
    output_bytes = remove(input_bytes)
    img_rgba = Image.open(io.BytesIO(output_bytes)).convert("RGBA")
    
    img_np = np.array(img_rgba)
    rgb = img_np[:, :, :3]
    alpha = img_np[:, :, 3]
    
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    
    # CLAHE equalization for clean shadow/highlight balance
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    equalized = clahe.apply(gray)
    
    white_bg = np.ones_like(equalized) * 255
    alpha_factor = alpha / 255.0
    final_gray = (equalized * alpha_factor + white_bg * (1 - alpha_factor)).astype(np.uint8)
    
    Image.fromarray(final_gray).save(output_path)
    print(f"✅ Saved clean photo to {output_path}")

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "my-photo.jpg"
    prepare_photo(src, "assets/photo-ready.png")