import cv2
import numpy as np
from typing import List, Tuple
from tqdm import tqdm
import pickle


def video_to_bitmaps(
    video_path: str, target_width: int, target_fps: float
) -> Tuple[float, List[np.ndarray]]:
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"无法打开视频文件：{video_path}")

    # 获取视频信息
    original_fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    aspect_ratio = original_width / original_height
    target_height = int(target_width / aspect_ratio)

    print(
        f"分辨率：{original_width}x{original_height} → {target_width}x{target_height}"
    )
    print(f"每秒帧数：{original_fps} → {target_fps}")

    bitmaps = []
    frame_interval = original_fps / target_fps
    accumulator = 0.0
    current_frame = 0

    with tqdm(total=total_frames, desc="已转换", unit="帧") as pbar:
        while True:
            ret, frame = cap.read()
            if not ret:
                break  # 视频结束

            accumulator += target_fps / original_fps

            if accumulator >= 1.0:
                # 缩放
                resized = cv2.resize(
                    frame, (target_width, target_height), interpolation=cv2.INTER_AREA
                )

                # 灰度化 & 二值化
                binary = cv2.adaptiveThreshold(
                    cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY),
                    1,
                    cv2.ADAPTIVE_THRESH_MEAN_C,
                    cv2.THRESH_BINARY,
                    11,
                    2,
                ).astype(bool)

                bitmaps.append(binary)
                accumulator -= 1.0

            current_frame += 1
            pbar.update(1)

    cap.release()

    actual_fps = original_fps / frame_interval
    print(f"转换结果：{len(bitmaps)} 帧，实际 {actual_fps:.2f} fps")

    return actual_fps, bitmaps


if __name__ == "__main__":
    video_path = "bad_apple.mp4"
    target_width = 16
    target_fps = 24.0

    try:
        fps, bitmaps = video_to_bitmaps(video_path, target_width, target_fps)

        with open("bitmaps.pkl", "wb") as f:
            pickle.dump((fps, bitmaps), f)
        print("已保存转换结果为 'bitmaps.pkl'")

    except IOError as e:
        print(e)
