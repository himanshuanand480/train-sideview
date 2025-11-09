# 🚆 Train Side-View | Automatic Wagon Split, Coverage Selection & HTML Report

An **end-to-end Python project** that automatically processes *side-view train videos* to identify wagons, extract frames, select best coverage images, and generate a detailed **HTML report**.  
Built to meet **AI-based visual inspection and coverage analysis assignment** requirements.

---

## 🧩 Project Overview

This project performs a **complete automated video-to-report pipeline** for train inspection:

1. 🎞 **Video to Frames** – Extracts image frames from each wagon video.  
2. 🧠 **Component Detection (YOLOv8)** – (optional) Detects parts like wheels, windows, couplers, etc.  
3. 🖼 **Coverage Frame Selection** – Selects top representative frames using visual diversity logic.  
4. 📑 **HTML Report Generation** – Creates a clean report showing total wagons, selected frames, and detected engines.  
5. 🎥 **Coach Video Creation** – Combines per-wagon frames back into MP4 clips for visual reference.

---

## 📸 Example Output Summary

After successful execution, a **report.html** is generated in  
📂 `DHN-wagon/Processed_Video/`

### Example Report Output:
Train Sideview Report
Generated: 2025-11-09 19:19:35
Total Wagons: 47
Total Frames Selected: 120
Engines Found: wagon1, wagon2
Each wagon section shows coverage frames such as:
wagon1 (3 frames)
frame_010.jpg  frame_075.jpg  frame_403.jpg
wagon2 (2 frames)
frame_022.jpg  frame_180.jpg
...

---

## ⚙️ Folder Structure


train-sideview/
├── src/
│   ├── 04_extract_frames.py
│   ├── 04b_make_coach_videos.py
│   ├── 05_detect_components.py
│   ├── 06_select_coverage.py
│   ├── 07_build_report.py
│   └── quick_report.py
│
├── DHN-wagon/
│   ├── Raw_Video/
│   ├── Processed_Video/
│   │   ├── wagon*/frame_###.jpg
│   │   ├── coverage/
│   │   └── report.html
│   └── models/
│       └── head_detection/weights/best.pt
│
├── requirements.txt
└── README.md

---

## 💻 How to Run (Step-by-Step)

### 🧱 1. Install Dependencies
Open PowerShell or Terminal:
```bash
pip install -r requirements.txt

🎬 2. Prepare Input Videos
Place your train side-view videos (.mp4) inside:
DHN-wagon/Raw_Video/

🧩 3. Run Scripts Sequentially
Run these in order:
# Step 1: Extract frames from video
python src/04_extract_frames.py

# Step 2: (Optional) Detect components using YOLO model
python src/05_detect_components.py

# Step 3: Select top coverage frames per wagon
python src/06_select_coverage.py

# Step 4: Create per-wagon MP4 clips
python src/04b_make_coach_videos.py

# Step 5: Generate HTML report
python src/07_build_report.py

Finally, open:
start DHN-wagon/Processed_Video/report.html

✅ This will display the final train side-view coverage report in your browser.

🔍 Concepts & Technologies Used
ConceptDescriptionPythonCore programming languageOpenCVFrame extraction and video creationUltralytics YOLOv8Used for object/component detectionMoviePyFor creating MP4 coach videosJinja2Dynamic HTML report generationPathlib, OS, GlobDirectory and file handlingPandas & NumpyData management and statisticsPowerShell AutomationUsed for file copying and report generation

🧠 Key Features


Automatically detects and splits train wagons


Generates optimized coverage frames (best visual summary per wagon)


Produces HTML reports showing each wagon’s top frames


Supports YOLO-based component detection (optional)


Completely Python-based pipeline, modular and reusable


No manual labeling required after setup



🧾 Example Assignment Output Alignment
Expected OutputAchieved in Project✅ HTML Report GeneratedYes (report.html)✅ Shows Total Wagons47✅ Shows Total Frames70–120 (depends on selection)✅ Side-view frame selectionCompleted✅ Optional head detectionMissing only best.pt weights✅ Final Output FolderDHN-wagon/Processed_Video/

🧰 Requirements
Python 3.10+
opencv-python
ultralytics
moviepy
jinja2
pandas
numpy


👤 Author Information
Name: Himanshu Anand
Email: himanshuanandece@gmail.com | himanshuanand480@gmail.com
LinkedIn: www.linkedin.com/in/himanshu-anand-684656253
Google Drive : https://drive.google.com/drive/folders/1kwdW34hN-PwAemmFrJ3bWrWdCyRp--S5?usp=sharing

💬 Feedback
If you find this project interesting or useful,
⭐ Star this repository on GitHub to show support!

🏁 Summary
This project demonstrates strong skills in:


Python programming


Computer vision


File automation & report generation


Model integration (YOLO)


Data organization for AI-based tasks


It’s a solid end-to-end ML pipeline project, ideal for internship or entry-level AI/ML engineer profile showcase.

--- ✅ 🚀

