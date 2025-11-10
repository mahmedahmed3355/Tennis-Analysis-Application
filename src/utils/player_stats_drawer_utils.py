def draw_player_stats(frame, player_stats, position=(10, 30), font_scale=0.5, color=(255, 255, 255), thickness=1):
    """
    Draws player statistics on the given frame.

    Parameters:
    - frame: The image frame on which to draw the statistics.
    - player_stats: A dictionary containing player statistics (e.g., name, score).
    - position: The starting position for drawing the text.
    - font_scale: Scale of the font used for drawing.
    - color: Color of the text in BGR format.
    - thickness: Thickness of the text.

    Returns:
    - frame: The modified frame with player statistics drawn on it.
    """
    for i, (key, value) in enumerate(player_stats.items()):
        text = f"{key}: {value}"
        cv2.putText(frame, text, (position[0], position[1] + i * 20), cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)

    return frame


def format_player_stats(player_name, score, aces, double_faults):
    """
    Formats player statistics into a dictionary.

    Parameters:
    - player_name: The name of the player.
    - score: The current score of the player.
    - aces: The number of aces served by the player.
    - double_faults: The number of double faults made by the player.

    Returns:
    - stats: A dictionary containing formatted player statistics.
    """
    stats = {
        "Player": player_name,
        "Score": score,
        "Aces": aces,
        "Double Faults": double_faults
    }
    return stats