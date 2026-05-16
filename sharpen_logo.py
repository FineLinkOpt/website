from PIL import Image, ImageFilter
import os

def sharpen_image():
    img_path = 'assets/FineLinK_Logo_Rect.png'
    
    if not os.path.exists(img_path):
        print(f"Error: {img_path} not found")
        return
        
    try:
        # Open the image
        img = Image.open(img_path)
        
        # Apply Unsharp Mask filter
        # Radius defines the size of the edges to be enhanced.
        # Percent controls the strength of the sharpening.
        # Threshold controls the minimum brightness change that will be sharpened.
        sharpened_img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=200, threshold=3))
        
        # Save the image, overwriting the original
        sharpened_img.save(img_path)
        print("Successfully sharpened FineLinK_Logo_Rect.png")
        
    except Exception as e:
        print(f"Failed to process image: {e}")

if __name__ == '__main__':
    sharpen_image()
