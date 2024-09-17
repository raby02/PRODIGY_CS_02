# PRODIGY_CS_02
# Pixel Manipulation for Image Encryption

This project is a simple image encryption tool using pixel manipulation techniques with Python. The tool provides basic encryption and decryption of images by swapping pixel values and applying mathematical operations to the image data. This project uses the Pillow and NumPy libraries to handle image processing.

## Table of Contents
- [Features](#features)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Example Output](#example-output)
- [License](#license)

## Features
- **Image Encryption:** Encrypts an image by applying a bitwise XOR operation on each pixel using a user-specified key. It also swaps the Red and Blue channels of the image to enhance encryption.
- **Image Decryption:** Reverses the encryption process using the same key to restore the original image.
- **Swapping Channels:** A simple method of obscuring the image by swapping the color channels (Red and Blue).

## How It Works
1. The program reads an image file and converts it to a NumPy array for pixel manipulation.
2. A key (integer between 0-255) is used to create a key array, which is then applied to the image data using the XOR operation for encryption.
3. The Red and Blue channels of the image are swapped to add an additional layer of encryption.
4. The encrypted image is saved and can later be decrypted using the same key, reversing the operations.

## Getting Started
### Prerequisites
- Python 3.x installed on your system.
- Libraries: `Pillow` and `NumPy`.
  - You can install these using:
    ```bash
    pip install pillow numpy
    ```

### Installation
1. **Clone the repository**:
    ```bash
    git clone [https://github.com/raby02/PRODIGY_CS_02.git]
    ```
2. **Navigate to the project directory**:
    ```bash
    cd PRODIGY_CS_02
    ```

## Usage
1. **Prepare an image** you want to encrypt. Place the image in the project directory or specify the full path in the code.
2. **Run the program**:
    ```bash
    python image_encryption.py
    ```
3. **Specify the image path** and the encryption key in the script:
    ```python
    original_image_path = r"C:\Users\Rabeeh\Downloads\your-image.png"
    key = 42  # Encryption key (0-255)
    ```
4. **Output**:
    - The script will save the encrypted image as `encrypted_image.png`.
    - It will then decrypt the image and save it as `decrypted_image.png`.

## Code Overview
### Dependencies
- **Pillow**: For opening, processing, and saving images.
- **NumPy**: For pixel manipulation using arrays.

### Functions
1. **`encrypt_image(image_path, key)`**:
    - Opens the image using the specified path.
    - Converts the image to a NumPy array for pixel-level manipulation.
    - Creates a key array of the same shape as the image to perform a bitwise XOR operation.
    - Swaps the Red and Blue channels to enhance encryption.
    - Returns an encrypted image.
2. **`decrypt_image(encrypted_image, key)`**:
    - Converts the encrypted image to a NumPy array.
    - Reverses the channel swap and performs bitwise XOR with the key array to decrypt the image.
    - Returns the decrypted image.
3. **Main Execution**:
    - Takes an image path and key.
    - Encrypts the image, saves it, and then decrypts the image using the same key.

### Example Output
#### Console Output
```plaintext
Starting process with image: C:\Users\Rabeeh\Downloads\watch-dogs-logo-png-transparent.png
Using key: 42
Opening image: C:\Users\Rabeeh\Downloads\watch-dogs-logo-png-transparent.png
Converting image to numpy array
Image dimensions: 500x500, 3 channels
Creating key array
Encrypting the image
Swapping Red and Blue channels
Creating encrypted image
Saving encrypted image
Encrypted image saved
Converting encrypted image to numpy array
Swapping Red and Blue channels back
Decrypting the image
Creating decrypted image
Saving decrypted image
Decrypted image saved
Process completed

