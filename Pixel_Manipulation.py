from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key):
    try:
        print(f"Opening image: {image_path}")
        img = Image.open(image_path)
        print("Converting image to numpy array")
        img_array = np.array(img)

        height, width, channels = img_array.shape
        print(f"Image dimensions: {width}x{height}, {channels} channels")

        print("Creating key array")
        key_array = np.full((height, width, channels), key, dtype=np.uint8)

        print("Encrypting the image")
        encrypted_array = np.bitwise_xor(img_array, key_array)

        print("Swapping Red and Blue channels")
        encrypted_array[:,:,[0, 2]] = encrypted_array[:,:,[2, 0]]

        print("Creating encrypted image")
        encrypted_img = Image.fromarray(encrypted_array)
        return encrypted_img
    except Exception as e:
        print(f"Error in encrypt_image: {e}")
        return None

def decrypt_image(encrypted_image, key):
    try:
        print("Converting encrypted image to numpy array")
        img_array = np.array(encrypted_image)

        height, width, channels = img_array.shape
        print(f"Image dimensions: {width}x{height}, {channels} channels")

        print("Creating key array")
        key_array = np.full((height, width, channels), key, dtype=np.uint8)

        print("Swapping Red and Blue channels back")
        img_array[:,:,[0, 2]] = img_array[:,:,[2, 0]]

        print("Decrypting the image")
        decrypted_array = np.bitwise_xor(img_array, key_array)

        print("Creating decrypted image")
        decrypted_img = Image.fromarray(decrypted_array)
        return decrypted_img
    except Exception as e:
        print(f"Error in decrypt_image: {e}")
        return None

# Example usage
original_image_path = r"C:\Users\Rabeeh\Downloads\watch-dogs-logo-png-transparent.png"
key = 42  # Encryption key (0-255)

print(f"Starting process with image: {original_image_path}")
print(f"Using key: {key}")

if not os.path.exists(original_image_path):
    print(f"Error: Image file not found at {original_image_path}")
else:
    # Encrypt the image
    encrypted_img = encrypt_image(original_image_path, key)
    if encrypted_img:
        print("Saving encrypted image")
        encrypted_img.save("encrypted_image.png")
        print("Encrypted image saved")

        # Decrypt the image
        decrypted_img = decrypt_image(encrypted_img, key)
        if decrypted_img:
            print("Saving decrypted image")
            decrypted_img.save("decrypted_image.png")
            print("Decrypted image saved")
    
print("Process completed")