class BallTracker:
    def __init__(self, detection_model):
        self.detection_model = detection_model

    def track_ball(self, frame):
        """
        Track the ball in the given frame using the detection model.
        
        Parameters:
        frame (numpy.ndarray): The video frame in which to track the ball.

        Returns:
        tuple: Coordinates of the detected ball (x, y) or None if not detected.
        """
        detections = self.detection_model.detect(frame)
        ball_coordinates = self._extract_ball_coordinates(detections)
        return ball_coordinates

    def _extract_ball_coordinates(self, detections):
        """
        Extract the ball coordinates from the detections.

        Parameters:
        detections (list): List of detected objects.

        Returns:
        tuple: Coordinates of the ball (x, y) or None if not detected.
        """
        for detection in detections:
            if detection['class'] == 'ball':
                return detection['coordinates']
        return None

    def update_tracker(self, frame):
        """
        Update the tracker with the new frame and return the ball's position.

        Parameters:
        frame (numpy.ndarray): The new video frame.

        Returns:
        tuple: Updated coordinates of the ball (x, y) or None if not detected.
        """
        return self.track_ball(frame)