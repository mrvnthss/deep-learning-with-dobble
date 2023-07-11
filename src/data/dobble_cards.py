import numpy as np
from PIL import Image, ImageDraw

import os
import random

import src.utils.circle_packings as cp


def create_empty_card(image_size, return_pil=True):
    """Create a square image of a white circle against a transparent background.

    Params:
        image_size (int): The size of the square image in pixels.
        return_pil (bool): Whether to return a PIL Image ('True') or a NumPy array ('False').  Defaults to 'True'.

    Returns:
        PIL.Image.Image or np.ndarray: The generated image of a white circle against a transparent background.
    """
    # Create a new transparent image with RGBA mode
    image = Image.new('RGBA', (image_size, image_size), (0, 0, 0, 0))

    # Create a new draw object
    draw = ImageDraw.Draw(image)

    # Calculate the coordinates of the circle to maximize its size within the square image
    circle_x = image_size // 2
    circle_y = image_size // 2
    radius = image_size // 2

    # Draw a white circle on the image
    draw.ellipse((circle_x - radius, circle_y - radius,
                  circle_x + radius, circle_y + radius),
                 fill=(255, 255, 255, 255))

    if return_pil:
        return image
    else:
        # Convert the image to a numpy array
        image_array = np.array(image)
        return image_array


def draw_circle(image, center, diameter, filled=False, fill_color=0, return_pil=True):
    """Draw a circle on the given PIL image.

    Params:
        image (PIL.Image.Image): The image on which to draw the circle.
        center (tuple): The center coordinates of the circle in the form (x, y).
        diameter (int): The diameter of the circle.
        filled (bool): Whether the circle should be filled ('True') or just have an outline ('False').
            Defaults to 'False'.
        fill_color (tuple): The fill color of the circle in RGB format. Used when 'filled' is 'True'.  Defaults to '0'.
        return_pil (bool): Whether to return a PIL Image ('True') or a NumPy array ('False').  Defaults to 'True'.

    Returns:
        PIL.Image.Image or np.ndarray: The modified image with the circle drawn onto it.
    """
    # Create a new draw object
    draw = ImageDraw.Draw(image)

    # Get x- and y-coordinates of the circle and compute radius
    circle_x, circle_y = center
    radius = diameter // 2

    if filled:
        # Draw a filled circle
        draw.ellipse(
            (circle_x - radius, circle_y - radius, circle_x + radius, circle_y + radius), fill=fill_color
        )
    else:
        # Draw the outline of the circle
        draw.ellipse(
            (circle_x - radius, circle_y - radius, circle_x + radius, circle_y + radius), outline=(0, 0, 0)
        )

    if return_pil:
        return image
    else:
        # Convert the image to a NumPy array
        image_array = np.array(image)
        return image_array


def load_emoji(emoji_set, emoji_name, emojis_dir_path, outline_only=False):
    """Load an emoji from the specified set of emojis.

    Params:
        emoji_set (str): The name of the set of emojis (e.g., 'classic-dobble').
        emoji_name (str): The name of the emoji to load.
        emojis_dir_path (str): The path to the directory containing the emoji images.
        outline_only (bool): Whether to load the outline-only version of the emoji.  Defaults to 'False'.

    Returns:
        PIL.Image.Image: The loaded emoji image in RGBA mode.

    Raises:
        ValueError: If the specified emoji file is not found or does not have a valid PNG extension.
    """
    # Create the filepath pointing to the emoji that we want to load
    if outline_only:
        which_type = 'outline'
    else:
        which_type = 'color'

    filepath = os.path.join(emojis_dir_path, emoji_set, which_type, emoji_name + '.png')

    # Check if the file exists and if it has the correct extension
    if os.path.isfile(filepath) and filepath.lower().endswith('.png'):
        emoji_image = Image.open(filepath)

        # Convert the image to RGBA mode if it's not already
        if emoji_image.mode != 'RGBA':
            emoji_image = emoji_image.convert('RGBA')

        return emoji_image
    else:
        raise ValueError(f'Failed to load emoji: {filepath} is not a valid PNG file.')


def place_emoji(image, emoji_image, emoji_size, center, rotation_angle=None, return_pil=True):
    """Place an emoji on the given image at the specified coordinates with the specified size.

    Params:
        image (PIL.Image.Image): The original image as a PIL Image.
        emoji_image (PIL.Image.Image): The emoji as a PIL Image.
        emoji_size (int): The desired size of the emoji in pixels when placed on the image.
        center (tuple): The center coordinates of the emoji in the form (x, y).
        rotation_angle (float): The rotation angle in degrees.  Defaults to 'None'.
        return_pil (bool): Whether to return a PIL Image ('True') or a NumPy array ('False').  Defaults to 'True'.

    Returns:
        PIL.Image.Image or np.ndarray:: The modified image with the emoji placed on it.

    Raises:
        ValueError: If the 'rotation_angle' is provided but is outside the valid range of [0, 360).
    """
    x_center, y_center = center

    # Calculate the top-left coordinates of the emoji based on the center coordinates and size
    x_left = x_center - emoji_size // 2
    y_top = y_center - emoji_size // 2

    # Resize the emoji to the specified size
    emoji_image = emoji_image.resize((emoji_size, emoji_size))

    # Check if a rotation angle was specified and validate it
    if rotation_angle is not None:
        if rotation_angle < 0 or rotation_angle >= 360:
            raise ValueError('Invalid rotation angle: must be in the range [0, 360).')

        # Rotate the image if the rotation angle is valid
        emoji_image = emoji_image.rotate(rotation_angle)

    # Paste the emoji onto the original image at the specified coordinates
    image.paste(emoji_image, (x_left, y_top), mask=emoji_image)

    if return_pil:
        return image
    else:
        # Convert the image to a NumPy array
        image_array = np.array(image)
        return image_array


def create_dobble_card(
        card_size, packing_type, packing_types_dict, coords_dir_path, emoji_set, emoji_list, emojis_dir_path,
        outline_only=False, return_pil=True):
    """Create a Dobble card by placing emojis according to the given parameters.

    Params:
        card_size (int): The size of the card in pixels.
        packing_type (str): The type of circle packing.  Must be one of the keys in the 'packing_types' dictionary.
        packing_types_dict (dict[str, tuple[function, str]]): A dictionary mapping packing types to their
            radii functions.
        coords_dir_path (str): The path to the directory containing the coordinates files.
        emoji_set (str): The name of the set of emojis.
        emoji_list (list): The list of names of the emojis to be placed on the card.
        emojis_dir_path (str): The path to the directory containing the emoji images.
        outline_only (bool): Whether to load the outline-only version of the emoji.  Defaults to 'False'.
        return_pil (bool): Whether to return a PIL Image ('True') or a NumPy array ('False').  Defaults to 'True'.

    Returns:
        PIL.Image.Image or np.ndarray:: The generated Dobble card.
    """
    # Create empty Dobble card
    dobble_card = create_empty_card(card_size)
    num_emojis = len(emoji_list)

    # Read relative coordinates from file
    relative_coordinates = cp.read_coordinates_from_file(
        num_emojis, packing_type, packing_types_dict, coords_dir_path
        )

    # Read largest radius from file and compute remaining radii
    largest_radius = cp.read_radius_from_file(num_emojis, packing_type, packing_types_dict, coords_dir_path)
    relative_radii = cp.compute_radii(largest_radius, num_emojis, packing_type, packing_types_dict)

    # Place emojis on card
    for count, emoji_name in enumerate(emoji_list):
        emoji_image = load_emoji(emoji_set, emoji_name, emojis_dir_path, outline_only)
        emoji_size = cp.convert_radius_to_pixels(relative_radii[count], card_size)
        center = cp.convert_coords_to_pixels(relative_coordinates[count], card_size)
        rotation_angle = random.randint(0, 359)
        dobble_card = place_emoji(dobble_card, emoji_image, emoji_size, center, rotation_angle)

    # Randomly rotate the image
    # NOTE: Since the part of the image that we care about is the inscribed circle (i.e., Dobble card),
    # we can leave the 'expand' parameter of the Image.rotate method set to its default value of False!
    rotation_angle = random.randint(0, 359)
    dobble_card = dobble_card.rotate(rotation_angle)

    if return_pil:
        return dobble_card
    else:
        # Convert the image to a NumPy array
        dobble_card_array = np.array(dobble_card)
        return dobble_card_array
