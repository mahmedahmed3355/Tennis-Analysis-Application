def pixels_to_inches(pixels, dpi):
    """Convert pixels to inches based on DPI (dots per inch)."""
    return pixels / dpi

def inches_to_pixels(inches, dpi):
    """Convert inches to pixels based on DPI (dots per inch)."""
    return inches * dpi

def normalize_coordinates(x, y, width, height):
    """Normalize coordinates to a range of [0, 1]."""
    return x / width, y / height

def denormalize_coordinates(norm_x, norm_y, width, height):
    """Denormalize coordinates from a range of [0, 1] to pixel values."""
    return int(norm_x * width), int(norm_y * height)

def convert_bbox_format(bbox, from_format='xywh', to_format='xyxy'):
    """Convert bounding box formats between 'xywh' and 'xyxy'.
    
    Args:
        bbox: A tuple or list representing the bounding box.
        from_format: The format of the input bounding box ('xywh' or 'xyxy').
        to_format: The desired output format ('xywh' or 'xyxy').
    
    Returns:
        A tuple representing the converted bounding box.
    """
    if from_format == 'xywh' and to_format == 'xyxy':
        x, y, w, h = bbox
        return (x, y, x + w, y + h)
    elif from_format == 'xyxy' and to_format == 'xywh':
        x1, y1, x2, y2 = bbox
        return (x1, y1, x2 - x1, y2 - y1)
    else:
        raise ValueError("Unsupported format conversion.")