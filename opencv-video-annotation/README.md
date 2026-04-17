# Driving Video Annotation with OpenCV

![Python](https://img.shields.io/badge/Python-3.14%2B-blue) ![Marimo](https://img.shields.io/badge/Notebook-Marimo-orange) ![No API Key Required](https://img.shields.io/badge/API%20Key-Not%20Required-green)

---

A Marimo notebook for processing dashcam footage and overlaying bounding box annotations onto objects in the video — cars, trucks, pedestrians, cyclists, and more. Built using OpenCV, MoviePy, and a MOT-format CSV label file.

Designed as a learning project to practice computer vision fundamentals including video I/O, frame extraction, object annotation, and annotated video export.

No API keys or external services required. Everything runs locally on your machine.

---

## Features

- Converts `.mov` dashcam footage to `.mp4` using FFmpeg
- Displays video playback inside the Marimo notebook (two options: native Marimo widget and MoviePy preview)
- Reads and prints video metadata: total frames, resolution, and frames per second
- Extracts individual frames from a video for quick visual inspection
- Displays a 5×5 grid of sampled frames across the full video timeline
- Loads a MOT-format CSV label file and filters annotations by video name
- Calculates the correct frame index for each annotation by syncing label frequency (5 Hz) with actual video FPS
- Draws color-coded bounding boxes per object category (car, truck, pedestrian, bicycle, etc.)
- Adds text labels above each bounding box
- Exports a fully annotated video as `out_test.mp4`
- Compresses the output video using FFmpeg's H.264 encoder for smaller file size
- Plays back the final annotated video inside the notebook

---

## Requirements

This project uses the following libraries. All of them can be installed with `pip`.

```
marimo>=0.23.1
matplotlib==3.10.8
moviepy==2.2.1
numpy==2.4.4
opencv-python==4.13.0.92
pandas==3.0.2
pygame==2.6.1
tqdm==4.67.3
```

You also need **FFmpeg** installed on your system for video conversion and compression.

Install FFmpeg on macOS:

```bash
brew install ffmpeg
```

Install FFmpeg on Ubuntu/Debian:

```bash
sudo apt install ffmpeg
```

---

## How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Install Marimo**

   ```bash
   pip3 install marimo
   ```

3. **Install all Python dependencies**

   ```bash
   pip3 install pandas opencv-python matplotlib moviepy pygame tqdm
   ```

   Or, if a `requirements.txt` is provided:

   ```bash
   pip install -r requirements.txt
   ```

4. **Install FFmpeg** (see Requirements section above)

5. **Create the Marimo configuration file**

   In the same folder as `my_video_processing_nb.py`, create a file named `pyproject.toml` and paste the following:

   ```toml
   [tool.marimo.runtime]
   output_max_bytes = 100_000_000
   ```

   This increases Marimo's output limit so the video can render inside the notebook.

6. **Add your video and label files**

   Place your `.mov` or `.mp4` dashcam file and your `mot_labels.csv` annotation file in the project folder. Update the file paths inside the notebook to match your local setup.

7. **Launch the notebook**

   ```bash
   marimo run my_video_processing_nb.py
   ```

   Or open it in edit mode:

   ```bash
   marimo edit my_video_processing_nb.py
   ```

---

## Usage

Once the notebook is running, you will see the following outputs in order:

```
Converting 026c7465-309f6d33.mov to 026c7465-309f6d33.mp4...

Total Frames in Video: 907.0
Height = 720.0
Width = 1280.0
FPS = 30.00
```

The notebook then renders:

- A single frame from the video
- A 5×5 grid of sampled frames across the timeline
- An annotated frame with color-coded bounding boxes and category labels
- A full annotated video exported to `out_test_compressed.mp4`
- Playback of the final annotated video inside the notebook

---

## File Structure

```
project/
├── my_video_processing_nb.py     # Main Marimo notebook
├── pyproject.toml                # Marimo output size config
├── mot_labels.csv                # Object annotation labels (MOT format)
├── 026c7465-309f6d33.mp4         # Input video (you provide this)
├── out_test.mp4                  # Raw annotated output (auto-generated)
└── out_test_compressed.mp4       # Compressed final output (auto-generated)
```

---

## What I Learned

- How to use OpenCV to open video files, read frame metadata, and extract individual frames
- How to sync annotation labels (recorded at 5 Hz) with video frames (recorded at 30 FPS) using a frame multiplier
- How to draw bounding boxes and add text overlays to frames using `cv2.rectangle` and `cv2.putText`
- How to write an annotated video frame-by-frame using `cv2.VideoWriter`
- How to call FFmpeg from Python using `subprocess` for video conversion and compression
- How Marimo notebooks differ from Jupyter: reactive cells, built-in video widgets, and the need for an increased output byte limit

---

## Credits

Based on a tutorial by Rob Mulla - VIdeo Data Processing with Python and OpenCV  
Video: [https:x//www.youtube.com/watch?v=AxIc-vGaHQ0](https://www.youtube.com/watch?v=AxIc-vGaHQ0)
