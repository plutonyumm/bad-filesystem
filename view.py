import os, time

TARGET_DIR = "/dev/shm/bad_apple"
GRID_W, GRID_H = 48, 24

try:
    while True:
        present = set(os.listdir(TARGET_DIR)) if os.path.isdir(TARGET_DIR) else set()
        rows = [
            "".join(
                "█" if f"{y:02d}_{x:02d}_x.txt" in present else " "
                for x in range(GRID_W)
            )
            for y in range(GRID_H)
        ]
        print("\033[H\033[J" + "\n".join(rows))
        time.sleep(0.05)
except KeyboardInterrupt:
    pass