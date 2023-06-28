import os


def read_coordinates_from_file(num_circles, packing_type, packing_types, coords_dir_path):
    """Read the coordinates of the specified circle packing from a text file.

    Args:
        num_circles (int): The number of circles in the circle packing.
        packing_type (str): The type of circle packing. Must be one of the keys in the 'packing_types' dictionary.
        packing_types (dict[str, tuple[func, str]]): A dictionary mapping packing types to their radii functions.
        coords_dir_path (str): The path to the directory containing the coordinates files.

    Returns:
        list[list[float]]: A list of coordinates of all the circles in the circle packing.

    Raises:
        FileNotFoundError: If the text file for the specified packing type and number of circles is not found.
        ValueError: If the 'packing_type' is not one of the supported packing types.

    Example:
        >>> read_coordinates_from_file(8, "ccib")
        [[-0.6540913321464167, -0.3429239913334197],
         [-0.7020130100112485, 0.20564598785008611],
         [0.3079710449731518, 0.6542463371435355],
         ...
         [0.6018119786520342, 0.048652252753781995]]
    """
    # Validate the packing_type argument
    if packing_type not in packing_types:
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


def read_radius_from_file(num_circles, packing_type, packing_types, coords_dir_path):
    """Read the radius of the largest circle of the specified circle packing from a text file.

    Args:
        num_circles (int): The number of circles in the circle packing.
        packing_type (str): The type of circle packing. Must be one of the keys in the 'packing_types' dictionary.
        packing_types (dict[str, tuple[func, str]]): A dictionary mapping packing types to their radii functions.
        coords_dir_path (str): The path to the directory containing the coordinates files.

    Returns:
        float: The radius of the largest circle of the circle packing.

    Raises:
        FileNotFoundError: If the 'radius.txt' file for the specified packing type is not found.
        ValueError: If the 'packing_type' is not one of the supported packing types.
        ValueError: If no radius is found for the specified packing type and number of circles.

    Example:
        >>> read_radius_from_file(8, "ccib")
        0.39622462840300093
    """
    # Validate the packing_type argument
    if packing_type not in packing_types:
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


def compute_radii(largest_radius, num_circles, packing_type, packing_types):
    """Compute the radii of circles in a circle packing.

    Args:
        largest_radius (float): The radius of the largest circle in the circle packing.
        num_circles (int): The total number of circles in the circle packing.
        packing_type (str): The type of circle packing. Must be one of the keys in the 'packing_types' dictionary.
        packing_types (dict[str, tuple[func, str]]): A dictionary mapping packing types to their radii functions.

    Returns:
        list[float]: The computed radii of the circles in the circle packing.

    Raises:
        ValueError: If the 'packing_type' is not one of the supported packing types.

    Example:
        >>> compute_radii(0.39622462840300093, 8, "ccib")
        [0.26141076581040507,
         0.2684861323639236,
         0.27689251545320875,
         0.2871755529147469,
         0.30028211666492743,
         0.31806597701209205,
         0.34493357344802994,
         0.39622462840300093]
    """
    # Validate the packing_type argument
    if packing_type not in packing_types:
        raise ValueError(f"Invalid packing type: '{packing_type}' is not supported.")

    fctn, monotonicity = packing_types[packing_type]
    fctn_vals = [fctn(n + 1) for n in range(num_circles)]

    # If the function 'fctn' is decreasing, we reverse the order of 'fctn_vals' so that the values are
    # listed in increasing order
    if monotonicity == "decreasing":
        fctn_vals.reverse()

    ratio = largest_radius / fctn_vals[-1]
    radii = [fctn_vals[n] * ratio for n in range(num_circles)]

    return radii
