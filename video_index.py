import os
import json
import math

# --- CONFIG ---
video_dir = r"C:\Users\Jeffr\OneDrive\Documents\GitHub\lego_typology_video_website\video"
output_json = r"C:\Users\Jeffr\OneDrive\Documents\GitHub\lego_typology_video_website\video_grid.json"
video_exts = {".mp4", ".mov", ".avi", ".mkv"}  # adjust as needed

# 1) Gather video files
videos = sorted(
    fname for fname in os.listdir(video_dir)
    if os.path.splitext(fname)[1].lower() in video_exts
)

n = len(videos)
if n == 0:
    raise RuntimeError(f"No videos found in {video_dir!r}")

# 2) Compute a near-square grid
nx = math.ceil(math.sqrt(n))
ny = math.ceil(n / nx)

# 3) Build positions dict
positions = {}
for idx, fname in enumerate(videos):
    row = idx // nx + 1   # 1-based
    col = idx % nx + 1
    positions[fname] = {"col": col, "row": row}

# 4) Assemble output structure
out = {
    "grid_size": {"nx": nx, "ny": ny},
    "positions": positions
}

# 5) Write JSON
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2)

print(f"Written grid JSON for {n} videos to {output_json}")
