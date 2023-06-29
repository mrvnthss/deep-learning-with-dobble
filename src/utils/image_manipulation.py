import numpy as np
from PIL import Image, ImageDraw


def create_empty_card(image_size, return_pil=True):
    """
    Create a square image of a white circle against a transparent background.

    Args:
        image_size (int): The size of the square image in pixels.
        return_pil (bool, optional): Whether to return a PIL Image (True) or a NumPy array (False).  Defaults to True.

    Returns:
        PIL.Image.Image or np.ndarray: The generated image of a white circle against a transparent background.
    """
    # Create a new transparent image with RGBA mode
    image = Image.new("RGBA", (image_size, image_size), (0, 0, 0, 0))

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
    """
    Draw a circle on the given PIL image.

    Args:
        image (PIL.Image.Image): The image on which to draw the circle.
        center (tuple): The center coordinates of the circle in the form (x, y).
        diameter (int): The diameter of the circle.
        filled (bool, optional): Whether the circle should be filled (True) or just have an outline (False).
            Defaults to False.
        fill_color (tuple, optional): The fill color of the circle in RGB format.  Used when 'filled' is True.
            Defaults to 0.
        return_pil (bool, optional): Whether to return a PIL Image (True) or a NumPy array (False).  Defaults to True.

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
        draw.ellipse((circle_x - radius, circle_y - radius,
                      circle_x + radius, circle_y + radius),
                     fill=fill_color)
    else:
        # Draw the outline of the circle
        draw.ellipse((circle_x - radius, circle_y - radius,
                      circle_x + radius, circle_y + radius),
                     outline=(0, 0, 0))

    if return_pil:
        return image
    else:
        # Convert the image to a NumPy array
        image_array = np.array(image)
        return image_array
