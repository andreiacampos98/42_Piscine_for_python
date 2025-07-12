import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    inverted = 255 - array * 1
    plt.imshow(inverted)
    plt.show()
    plt.savefig("inverted.jpeg")
    return inverted


def ft_red(array) -> np.ndarray:
    red = array * 1
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    plt.imshow(red)
    plt.show()
    plt.savefig("red.jpeg")
    return red


def ft_green(array) -> np.ndarray:
    green = array - array
    green[:, :, 1] = array[:, :, 1]
    plt.imshow(green)
    plt.show()
    plt.savefig("green.jpeg")
    return green


def ft_blue(array) -> np.ndarray:
    blue = np.zeros_like(array)
    blue[:, :, 2] = array[:, :, 2]
    plt.imshow(blue)
    plt.show()
    plt.savefig("blue.jpeg")
    return blue


def ft_grey(array) -> np.ndarray:
    grey_val = (array[:, :, 0] + array[:, :, 1] + array[:, :, 2]) // 3
    grey = np.zeros_like(array)
    grey[:, :, 0] = grey_val
    grey[:, :, 1] = grey_val
    grey[:, :, 2] = grey_val
    plt.imshow(grey)
    plt.show()
    plt.savefig("grey.jpeg")
    return grey
