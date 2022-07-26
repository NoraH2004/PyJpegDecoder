import numpy as np


def YCbCr_to_RGB(image_array: np.ndarray) -> np.ndarray:
    """Takes a 3-dimensional array representing an image in the YCbCr color
    space, and returns an array of the image in the RGB color space:
    array(width, heigth, YCbCr) -> array(width, heigth, RGB)
    """
    print("\nConverting colors from YCbCr to RGB...")
    Y = image_array[..., 0].astype("float64")
    Cb = image_array[..., 1].astype("float64")
    Cr = image_array[..., 2].astype("float64")

    R = Y + 1.402 * (Cr - 128.0)
    G = Y - 0.34414 * (Cb - 128.0) - 0.71414 * (Cr - 128.0)
    B = Y + 1.772 * (Cb - 128.0)

    output = np.stack((R, G, B), axis=-1)
    np.clip(output, a_min=0.0, a_max=255.0, out=output)

    return np.round(output).astype("uint8")


def bytes_to_uint(bytes_obj: bytes) -> int:
    """Convert a big-endian sequence of bytes to an unsigned integer."""
    return int.from_bytes(bytes_obj, byteorder="big", signed=False)
