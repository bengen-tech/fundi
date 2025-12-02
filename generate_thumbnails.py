import cv2
import os

# === SETTINGS ===
VIDEO_DIR = "media/video"
THUMBNAIL_DIR = "media/images"
THUMBNAIL_TIME_SEC = 5  # Capture frame at 5 seconds
THUMB_WIDTH = 320       # Resize width (maintains aspect ratio)

# Ensure thumbnail output folder exists
os.makedirs(THUMBNAIL_DIR, exist_ok=True)

# Loop through all mp4 files
for filename in os.listdir(VIDEO_DIR):
    if filename.lower().endswith(".mp4"):
        video_path = os.path.join(VIDEO_DIR, filename)
        thumb_name = os.path.splitext(filename)[0] + "-thumb.jpg"
        thumb_path = os.path.join(THUMBNAIL_DIR, thumb_name)

        print(f"Processing: {filename}")
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"  ❌ Failed to open {filename}")
            continue

        # Set video to 5 seconds
        cap.set(cv2.CAP_PROP_POS_MSEC, THUMBNAIL_TIME_SEC * 1000)

        success, frame = cap.read()
        if success:
            # Resize to thumb width while keeping aspect ratio
            height, width, _ = frame.shape
            ratio = THUMB_WIDTH / width
            new_size = (THUMB_WIDTH, int(height * ratio))
            resized = cv2.resize(frame, new_size)

            cv2.imwrite(thumb_path, resized)
            print(f"  ✅ Thumbnail saved: {thumb_path}")
        else:
            print(f"  ❌ Could not capture frame from {filename}")
        
        cap.release()

print("\n✔️ Done generating all thumbnails.")
