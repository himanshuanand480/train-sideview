# download_raw_videos.py
import subprocess, sys, shutil
from pathlib import Path

FOLDER_ID = "13GaVu0IXX65M0WIsEH9OmkD9DlSyoXL2"  # your Drive folder link

DEST_ROOT = Path("DHN-wagon/Raw_video")           # where we want all MP4s
TMP_DIR = Path("DHN-wagon/_gdown_tmp")            # temporary staging area

DEST_ROOT.mkdir(parents=True, exist_ok=True)
TMP_DIR.mkdir(parents=True, exist_ok=True)

# 1) Download the whole folder tree into a temp directory.
#    --remaining-ok prevents the >50 files warning from stopping the run.
cmd = [
    sys.executable, "-m", "gdown",
    "--folder",
    f"https://drive.google.com/drive/folders/{FOLDER_ID}",
    "-O", str(TMP_DIR),
    "--remaining-ok"
]
print("Running:", " ".join(cmd))
subprocess.run(cmd, check=False)

# 2) Walk the temp directory, move ONLY .mp4 files to DEST_ROOT
moved = 0
for p in TMP_DIR.rglob("*"):
    if p.is_file() and p.suffix.lower() == ".mp4":
        target = DEST_ROOT / p.name
        # if same name exists, make it unique
        if target.exists():
            stem = target.stem
            suffix = target.suffix
            i = 1
            while True:
                alt = DEST_ROOT / f"{stem}__{i}{suffix}"
                if not alt.exists():
                    target = alt
                    break
                i += 1
        shutil.move(str(p), str(target))
        moved += 1

print(f"\n Collected {moved} MP4 files into: {DEST_ROOT}")

# 3) clean the temp directory to save space
try:
    shutil.rmtree(TMP_DIR)
    print(f" Cleaned temp dir: {TMP_DIR}")
except Exception as e:
    print(f"Note: could not delete temp dir ({e}). You can remove it manually later.")
