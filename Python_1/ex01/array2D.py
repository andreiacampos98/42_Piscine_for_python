import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    if len(set(len(linha) for linha in family)) != 1:
        raise ValueError("Lists are not the same size")
    array = np.array(family)
    print(f'My shape is : {array.shape}')
    new_array = array[start:end]
    print(f'My new shape is : {new_array.shape}')
    return new_array.tolist()
