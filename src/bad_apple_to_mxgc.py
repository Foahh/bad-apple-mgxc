from utils.video_to_bitmaps import video_to_bitmaps

TICK_INTERVAL = 5

def bad_apple_to_mxgc():
    pass


if __name__ == "__main__":
    video_path = "res/bad_apple.mp4"
    target_width = 16
    target_fps = 30.0

    fps, bitmaps = video_to_bitmaps(video_path, target_width, target_fps)
