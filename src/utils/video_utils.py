def load_video(video_path):
    import cv2
    video_capture = cv2.VideoCapture(video_path)
    if not video_capture.isOpened():
        raise ValueError(f"Error opening video file: {video_path}")
    return video_capture

def save_video(output_path, frames, fps=30):
    import cv2
    height, width, _ = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for frame in frames:
        video_writer.write(frame)

    video_writer.release()

def extract_frames(video_capture, frame_interval=1):
    frames = []
    frame_count = 0

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        if frame_count % frame_interval == 0:
            frames.append(frame)
        frame_count += 1

    return frames

def release_video_capture(video_capture):
    video_capture.release()