import os, shutil, time
from PIL import Image

FRAMES_DIR = "frames"
TARGET_DIR = "/dev/shm/bad_apple"
GRID_W, GRID_H = 48, 24
FPS = 10
THRESHOLD = 128

os.makedirs(TARGET_DIR, exist_ok=True)
frames = sorted(f for f in os.listdir(FRAMES_DIR) if f.lower().endswith(".png"))
print(f"{len(frames)} frames. starting in 3s...")
time.sleep(3)

delay = 1.0 / FPS
next_t = time.perf_counter()
for frame_name in frames:
    shutil.rmtree(TARGET_DIR)
    os.makedirs(TARGET_DIR)

    img = Image.open(os.path.join(FRAMES_DIR, frame_name)).convert("L")
    img = img.resize((GRID_W, GRID_H), Image.Resampling.LANCZOS)

    for y in range(GRID_H):
        for x in range(GRID_W):
            if img.getpixel((x, y)) < THRESHOLD:
                fn = f"{y:02d}_{x:02d}_x.txt"
                open(os.path.join(TARGET_DIR, fn), "a").close()

    next_t += delay
    s = next_t - time.perf_counter()
    if s > 0:
        time.sleep(s)
    else:
        next_t = time.perf_counter()

shutil.rmtree(TARGET_DIR, ignore_errors=True)
print("done.")