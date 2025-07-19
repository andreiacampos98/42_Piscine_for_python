import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    inverted = 255 - array
    plt.imshow(inverted)
    plt.savefig("inverted.jpeg")
    return inverted


def ft_red(array) -> np.ndarray:
    """
    Show only the red colour.
    """
    red = array * 1
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    plt.imshow(red)
    plt.savefig("red.jpeg")
    return red


def ft_green(array) -> np.ndarray:
    """
    Show only the green colour.
    """
    green = array - array
    green[:, :, 1] = array[:, :, 1]
    plt.imshow(green)
    plt.savefig("green.jpeg")
    return green


def ft_blue(array) -> np.ndarray:
    """
    Show only the blue colour.
    """
    blue = np.zeros_like(array)
    blue[:, :, 2] = array[:, :, 2]
    plt.imshow(blue)
    plt.savefig("blue.jpeg")
    return blue


def ft_grey(array) -> np.ndarray:
    """
    Transform in black and white picture.
    """
    r = array[:, :, 0].astype(np.int32)
    g = array[:, :, 1].astype(np.int32)
    b = array[:, :, 2].astype(np.int32)
    
    grey_val = (r + g + b) // 3
    grey = np.zeros_like(array)
    grey[:, :, 0] = grey_val
    grey[:, :, 1] = grey_val
    grey[:, :, 2] = grey_val
    plt.imshow(grey)
    plt.savefig("grey.jpeg")
    return grey
