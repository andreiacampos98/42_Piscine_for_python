from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(picture: np.ndarray):
    """The functions takes the pixels of a picture, zoom in and rotate."""
    try:
        new_array = picture[100:500, 400:800]
        if new_array.ndim == 3 and new_array.shape[2] == 3:
            new_array = new_array.mean(axis=2, keepdims=True).astype(np.uint8)
        print(f"New shape after slicing: {new_array.shape}")
        print(new_array)
        return (new_array)
    except Exception as e:
        print(f"Error during zoom: {e}")
        return None


def ft_rotate(picture: np.ndarray):
    """This function takes a picture and rotate it."""
    print(picture.shape)
    array = picture.tolist()
    height = len(array)
    width = len(array[0])
    new_array_transpose = []
    for i in range(height):
        new_row = []
        for j in range(width):
            new_row.append(array[j][i][0])
        new_array_transpose.append(new_row)
    result = np.array(new_array_transpose, dtype=np.uint8)
    print(f"New shape after Transpose: {result.shape}")
    print(result)
    return (result)


def display_image(picture: np.ndarray):
    """The functions takes the pixels of a picture and displays it."""
    try:
        plt.imshow(picture.squeeze(), cmap='gray')
        plt.savefig("rotate.jpeg")
        print("Picture saved as 'rotate.jpeg'")
    except Exception as e:
        print(f"Error displaying image: {e}")


def main():
    """Load the image, do the zooming, rotate and display the picture."""
    img_array = ft_load("Python_1/animal.jpeg")
    if img_array is not None:
        new_array = ft_zoom(img_array)
        if new_array is not None:
            result = ft_rotate(new_array)
            display_image(result)


if __name__ == "__main__":
    main()
