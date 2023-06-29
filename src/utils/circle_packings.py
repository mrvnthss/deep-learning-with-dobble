import numpy as np
import os


def read_coordinates_from_file(num_circles, packing_type, packing_types_dict, coords_dir_path):
    """Read the coordinates of the specified circle packing from a text file.

    Args:
        num_circles (int): The number of circles in the circle packing.
        packing_type (str): The type of circle packing.  Must be one of the keys in the 'packing_types' dictionary.
        packing_types_dict (dict[str, tuple[function, str]]): A dictionary mapping packing types to their
            radii functions.
        coords_dir_path (str): The path to the directory containing the coordinates files.

    Returns:
        list[list[float]]: A list of coordinates of all the circles in the circle packing.

    Raises:
        FileNotFoundError: If the text file for the specified packing type and number of circles is not found.
        ValueError: If the 'packing_type' is not one of the supported packing types.
    """
    # Validate the packing_type argument
    if packing_type not in packing_types_dict:
        raise ValueError(f"Invalid packing type: '{packing_type}' is not supported.")

    filename = os.path.join(coords_dir_path, packing_type, packing_type + str(num_circles) + '.txt')

    try:
        with open(filename, 'r') as file:
            # Read values line by line, split into separate columns and get rid of first column of text file
            coordinates = [line.strip().split()[1:] for line in file.readlines()]
            coordinates = [[float(coord) for coord in coord_list] for coord_list in coordinates]
        return coordinates
    except FileNotFoundError:
        raise FileNotFoundError(f"Coordinates file for '{packing_type}' packing with {num_circles} circles not found.")


def read_radius_from_file(num_circles, packing_type, packing_types_dict, coords_dir_path):
    """Read the radius of the largest circle of the specified circle packing from a text file.

    Args:
        num_circles (int): The number of circles in the circle packing.
        packing_type (str): The type of circle packing.  Must be one of the keys in the 'packing_types_dict' dictionary.
        packing_types_dict (dict[str, tuple[function, str]]): A dictionary mapping packing types to their
            radii functions.
        coords_dir_path (str): The path to the directory containing the coordinates files.

    Returns:
        float: The radius of the largest circle of the circle packing.

    Raises:
        FileNotFoundError: If the 'radius.txt' file for the specified packing type is not found.
        ValueError: If the 'packing_type' is not one of the supported packing types.
        ValueError: If no radius is found for the specified packing type and number of circles.
    """
    # Validate the packing_type argument
    if packing_type not in packing_types_dict:
        raise ValueError(f"Invalid packing type: '{packing_type}' is not supported.")

    filename = os.path.join(coords_dir_path, packing_type, 'radius.txt')

    try:
        with open(filename, 'r') as file:
            for line in file:
                values = line.strip().split()
                if len(values) == 2 and int(values[0]) == num_circles:
                    return float(values[1])

        raise ValueError(f"No radius found for packing type '{packing_type}' with {num_circles} circles.")
    except FileNotFoundError:
        raise FileNotFoundError(f"Radius file for '{packing_type}' packing not found.")


def compute_radii(largest_radius, num_circles, packing_type, packing_types_dict):
    """Compute the radii of circles in a circle packing.

    Args:
        largest_radius (float): The radius of the largest circle in the circle packing.
        num_circles (int): The total number of circles in the circle packing.
        packing_type (str): The type of circle packing.  Must be one of the keys in the 'packing_types_dict' dictionary.
        packing_types_dict (dict[str, tuple[function, str]]): A dictionary mapping packing types to their
            radii functions.

    Returns:
        list[float]: The computed radii of the circles in the circle packing.

    Raises:
        ValueError: If the 'packing_type' is not one of the supported packing types.
    """
    # Validate the packing_type argument
    if packing_type not in packing_types_dict:
        raise ValueError(f"Invalid packing type: '{packing_type}' is not supported.")

    fctn, monotonicity = packing_types_dict[packing_type]
    fctn_vals = [fctn(n + 1) for n in range(num_circles)]

    # If the function 'fctn' is decreasing, we reverse the order of 'fctn_vals' so that the values are
    # listed in increasing order
    if monotonicity == "decreasing":
        fctn_vals.reverse()

    ratio = largest_radius / fctn_vals[-1]
    radii = [fctn_vals[n] * ratio for n in range(num_circles)]

    return radii


def convert_coords_to_pixels(rel_coords, image_size):
    """
    Convert relative coordinates to pixel values based on the size of a square image.

    The function takes relative coordinates in the range of [-1, 1] and converts them to pixel values
    based on the size of a square image.  The relative coordinates are assumed to be in a normalized form,
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
        >>> convert_coords_to_pixels((-0.5, 0.75), 512)
        (128, 448)

        >>> convert_coords_to_pixels((0.25, 0.5), 256)
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


def convert_radius_to_image_size_in_pixels(rel_radius, bg_size):
    """
    Convert a relative radius from 0 to 1 to image size in pixels based on the size of a square image (background).

    Args:
        rel_radius (float): Relative radius in the range of [0, 1].
        bg_size (int): Size of the square image in pixels that serves as background.

    Returns:
        int: Size of the square image in pixels to be placed on the background.

    Raises:
        ValueError: If the relative radius is outside the valid range of [0, 1].

    Example:
        >>> convert_radius_to_image_size_in_pixels(0.5, 512)
        256
    """
    if rel_radius < 0 or rel_radius > 1:
        raise ValueError("Relative radius must be in the range of [0, 1].")

    image_size = int(rel_radius * bg_size)

    return image_size
