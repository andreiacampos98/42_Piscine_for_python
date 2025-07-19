from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(picture: np.ndarray):
    """The functions takes the pixels of a picture and zoom in."""
    try:
        new_array = picture[100:500, 400:800]
        if new_array.ndim == 3 and new_array.shape[2] == 3:
            new_array = new_array.mean(axis=2, keepdims=True).astype(np.uint8)
        print(f"New shape after slicing: {new_array.shape}")
        print(new_array)
        return new_array
    except Exception as e:
        print(f"Error during zoom: {e}")
        return None


def display_image(picture: np.ndarray):
    """The functions takes the pixels of a picture and displays it."""
    try:
        plt.imshow(picture.squeeze(), cmap='gray')
        plt.savefig("zoom.jpeg")
        print("Picture saved as 'zoom.jpeg'")
    except Exception as e:
        print(f"Error displaying image: {e}")


def main():
    """Load the image, do the zooming and display the picture."""
    img_array = ft_load("Python_1/animal.jpeg")
    if img_array is not None:
        new_array = ft_zoom(img_array)
        if new_array is not None:
            display_image(new_array)


if __name__ == "__main__":
    main()
