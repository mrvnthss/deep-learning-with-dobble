import numpy as np


def convert_coords_to_pixels(rel_coords, image_size):
    """
    Convert relative coordinates to pixel values based on the size of a square image.

    The function takes relative coordinates in the range of [-1, 1] and converts them to pixel values
    based on the size of a square image. The relative coordinates are assumed to be in a normalized form,
    where the origin (0, 0) corresponds to the center of the image and the values (-1, -1) and (1, 1)
    correspond to the lower left and upper right corner of the image, respectively.

    Args:
        rel_coords (np.ndarray or tuple): Relative coordinates in the range of [-1, 1] in the form (x, y).
        image_size (int): Size of the square image.

    Returns:
        tuple[int, int]: Pixel values corresponding to the relative coordinates.

    Raises:
        ValueError: If the relative coordinates are outside the range of [-1, 1].

    Examples:
        >>> rel_coords = np.array([-0.5, 0.75])
        >>> image_size = 512
        >>> convert_coords_to_pixels(rel_coords, image_size)
        (128, 448)

        >>> rel_coords = (0.25, 0.5)
        >>> image_size = 256
        >>> convert_coords_to_pixels(rel_coords, image_size)
        (160, 192)
    """
    # Convert rel_coords to NumPy array if necessary
    if not isinstance(rel_coords, np.ndarray):
        rel_coords = np.array(rel_coords)

    # Check if the relative coordinates are within the range of [-1, 1]
    if np.any((rel_coords < -1) | (rel_coords > 1)):
        raise ValueError("Relative coordinates must be in the range of [-1, 1].")

    # Shift coordinates from [-1, 1] to [0, 1]
    rel_coords = rel_coords / 2 + 0.5

    # Scale coordinates from [0, 1] to [0, card_size] and convert to integer values
    coords = np.floor(rel_coords * image_size).astype('int')

    return tuple(coords)
