# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.23.1",
#     "matplotlib==3.10.8",
#     "moviepy==2.2.1",
#     "numpy==2.4.4",
#     "opencv-python==4.13.0.92",
#     "pandas==3.0.2",
#     "pygame==2.6.1",
#     "tqdm==4.67.3",
# ]
# ///

import marimo

__generated_with = "0.23.1"
app = marimo.App(width="full")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # === Video Processing === #
    """)
    return


@app.cell
def _():
    # working with driving video data
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## === EDIT: Marimo Specific Modification === ##
    """)
    return


@app.cell
def _():
    # create pyproject.toml
    # paste the following code
    # increases the output max bytes limit from 10,000,000 to 100,000,000 bytes

    '''
    [tool.marimo.runtime]
    output_max_bytes = 100_000_000
    '''
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## === Install Modules === ##
    """)
    return


@app.cell
def _():
    """
    EDIT: pip3 install marimo
    pip3 install pandas
    pip3 install opencv-python
    pip3 install matplotlib
    # convert videos files
    brew install ffmpeg
    EDIT: not using pip3 install ipython
    EDIT: pip3 install moviepy
    EDIT: pip3 install pygame 
    pip3 install tqdm
    """
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## === Loading Modules === ##
    """)
    return


@app.cell
def _():
    # using built-in marimo functions
    import marimo as mo
    # manage csv and tables
    import pandas as pd
    # math and matrix
    import numpy as np
    # image and video manipulation
    import cv2
    # create charts and view images
    import matplotlib.pyplot as plt
    # find file paths
    from glob import glob
    # EDIT: replacing 
    # import IPython.display as ipd
    # watching video and listen to audio playback
    from moviepy import VideoFileClip
    # see progross during long tasks
    from tqdm import tqdm
    # run system-level commands
    import subprocess

    # set visual style for matplotlib
    plt.style.use('ggplot')
    return VideoFileClip, cv2, mo, pd, plt, subprocess, tqdm


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## === Convert Video Type === ##
    """)
    return


@app.cell
def _(subprocess):
    # Use ffmpeg to convert mov to mp4
    # locate file you want to convert
    input_file = '/Volumes/DataBase/opencv_video_data/training/driving/026c7465-309f6d33.mov'
    # convert will be produce at the same directory as python file
    output_file = '026c7465-309f6d33.mp4'
    print(f"Converting {input_file} to {output_file}...")
    subprocess.run([
        'ffmpeg',
        '-i', 
        input_file,
        '-qscale', 
        '0',
        output_file,
        '-loglevel', 
        'quiet'
    ])

    # command terminal
    # !ls -GFlash --color
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## === Display Video === ##
    """)
    return


@app.cell
def _(mo):
    # EDIT: replacing
    # ipd.Video("00a0f008-3c67908e.mp4", width = 700)
    """ Option 1: marimo only """
    mo.video(src="026c7465-309f6d33.mp4", width="700", controls=True, autoplay=False)
    return


@app.cell
def _(VideoFileClip):
    """ Option 2: moviepy (more universal) """
    clip = VideoFileClip("026c7465-309f6d33.mp4")
    new_clip = (
            clip
            .subclipped(0,5)
            .resized(width=700)
            .with_fps(30)
            .with_duration(2)
               )
    # apply audio=False to use play/pause function
    # otherwise it will autoplay until completion
    new_clip.preview(audio=False)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## === Open Video and Read Metadata === ##
    """)
    return


@app.cell
def _(cv2):
    # Load in video capture
    cap = cv2.VideoCapture('026c7465-309f6d33.mp4')
    # Total number of frames in video
    frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print(f'Total Frames in Video {frame}')
    # Height and width of video
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    print(f'Height = {height} \nWidth = {width}')
    # Frames per second
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f'FPS = {fps:0.2f}')
    # Unload video capture
    cap.release()
    # EDIT: actual FPS = 30, TUTORIAL FPS = 60
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## === Pull in Image from Video === ##
    """)
    return


@app.cell
def _(cv2):
    # Load in video capture
    cap1 = cv2.VideoCapture('026c7465-309f6d33.mp4')
    # Return return result and image
    ret1, img1 = cap1.read()
    print(f'Returned {ret1} and Img of Shape {img1.shape}')
    return cap1, img1


@app.cell
def _(img1, plt):
    # Display image
    plt.imshow(img1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## === Helper Function for Plotting OpenCV Images in Notebookf === ##
    """)
    return


@app.cell
def _(cap1, cv2, img1, plt):
    def display_cv2_img(img1, figsize = (10, 10)):
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        fig1, ax1 = plt.subplots(figsize=figsize)
        ax1.imshow(img1)
        ax1.axis("off")
        plt.show()

    display_cv2_img(img1)
    cap1.release()
    return (display_cv2_img,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## === Display Multiple Fromes from this Video === ##
    """)
    return


@app.cell
def _(cv2, plt):
    fig2, axs2 = plt.subplots(5, 5, figsize=(30,20))
    axs2 = axs2.flatten()

    cap2 = cv2.VideoCapture('026c7465-309f6d33.mp4')
    n_frames2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

    img_idx2 = 0
    for  frame2 in range(n_frames2):
        ret2, img2 = cap2.read()
        if ret2 == False:
            break
        # EDIT: TUTORIAL used 100 because 60 FPS
        if frame2 % 50 == 0:
            axs2[img_idx2].imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
            axs2[img_idx2].set_title(f'Frame: {frame2}')
            axs2[img_idx2].axis('off')
            img_idx2 += 1

    plt.tight_layout()
    plt.show()
    cap2.release()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## === Add Annotations to Video Images === ##
    """)
    return


@app.cell
def _(pd):
    labels = pd.read_csv('/Users/rthai/Library/CloudStorage/Nextcloud-thaicloud@100․96․128․47:8080/Documents/Self_Study/Python-Projects/project_4/opencv/mot_labels.csv', low_memory=False)

    labels.head()
    return (labels,)


@app.cell
def _(cv2, labels):
    video_labels = (labels.query('videoName == "026c7465-309f6d33"').reset_index(drop=True).copy())

    # EDIT: Read actual FPS from your video
    cap_temp = cv2.VideoCapture('026c7465-309f6d33.mp4')
    video_fps = cap_temp.get(cv2.CAP_PROP_FPS)
    cap_temp.release()

    # EDIT: labels were annotated at 5Hz — this is fixed in the dataset
    label_hz = 5
    # EDIT: calculate the multiplier from actual FPS from your video
    # EDIT 30 FPS / 5 Hz = 6 Frame Multipler
    frame_multiplier = video_fps / label_hz
    # EDIT: NOT using TUTORIAL's fixed 11.9 as frame multiplier
    video_labels["video_frame"] = (video_labels["frameIndex"] * frame_multiplier).round().astype("int")

    video_labels["category"].value_counts()
    return (video_labels,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## === Pull Frame 516 === ##
    """)
    return


@app.cell
def _(cv2, display_cv2_img):
    # EDIT: TUTORIAL Pull Frame 1035 because of 60 FPS
    # EDIT: Used 516 Because it is a Multiplier of 6 and Closest Image and Timeline to TUTORIAL
    cap3 = cv2.VideoCapture('026c7465-309f6d33.mp4')
    n_frames3 = int(cap3.get(cv2.CAP_PROP_FRAME_COUNT))

    img_idx3 = 0
    for frame3 in range(n_frames3):
        ret3, img3 = cap3.read()
        if ret3 == False:
            break
        if frame3 == 510:
            break

    cap3.release()
    display_cv2_img(img3)
    return (img3,)


@app.cell
def _(video_labels):
    video_labels
    return


@app.cell
def _(video_labels):
    frame_labels = video_labels.query('video_frame == 516')
    for i, d in frame_labels.iterrows():
        break
    print(d)
    return


@app.cell
def _(cv2, display_cv2_img, img3, video_labels):
    img_example4 = img3.copy()
    frame_labels4 = video_labels.query('video_frame == 516')
    for i4, d4 in frame_labels4.iterrows():
        pt1 = int(d4['box2d.x1']), int(d4['box2d.y1'])
        pt2 = int(d4['box2d.x2']), int(d4['box2d.y2'])
        cv2.rectangle(img_example4, pt1, pt2, (0,0,255), 3)

    display_cv2_img(img_example4)
    return


@app.cell
def _(video_labels):
    video_labels["category"].unique()
    return


@app.cell
def _(cv2, display_cv2_img, img3, video_labels):
    color_map = {
        "car": (0, 0, 255),
        "truck": (0, 0, 100),
        "pedestrian": (255, 0, 0),
        "other vehicle": (0, 0, 150),
        "rider": (200, 0, 0),
        "bicycle": (0, 255, 0),
        "other person": (200, 0, 0),
        "trailer": (0, 150, 150),
        "motorcycle": (0, 150, 0),
        "bus": (0, 0, 100),
    }
    img_example5 = img3.copy()
    frame_labels5 = video_labels.query('video_frame == 516')
    for i5, d5 in frame_labels5.iterrows():
        pt3 = int(d5['box2d.x1']), int(d5['box2d.y1'])
        pt4 = int(d5['box2d.x2']), int(d5['box2d.y2'])
        color5 = color_map[d5["category"]]
        cv2.rectangle(img_example5, pt3, pt4, color5, 3)

    display_cv2_img(img_example5)
    return (color_map,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## === Adding Text Label === ##
    """)
    return


@app.cell
def _(color_map, cv2, display_cv2_img, img3, video_labels):

    frame_labels6 = video_labels.query("video_frame == 516")
    font6 = cv2.FONT_HERSHEY_COMPLEX
    img_example6 = img3.copy()
    for i6, d6 in frame_labels6.iterrows():
        pt5 = int(d6['box2d.x1']), int(d6['box2d.y1'])
        pt6 = int(d6['box2d.x2']), int(d6['box2d.y2'])
        color6 = color_map[d6["category"]]
        img_example6 = cv2.rectangle(img_example6, pt5, pt6, color6, 3)
        pt_text = int(d6['box2d.x1']) + 5, int(d6['box2d.y1'] + 10)
        cv2.putText(img_example6, d6["category"], pt_text, font6, 0.5, color6)
    display_cv2_img(img_example6)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## === Label and Output Annotated Video === ##
    """)
    return


@app.cell
def _(color_map, cv2):
    def add_annotation(img7, frame7, video_labels):
        max_frame = video_labels.query("video_frame <= @frame7")["video_frame"].max()
        frame_labels = video_labels.query("video_frame == @max_frame")
        for i7, d7 in frame_labels.iterrows():
            pt7 = int(d7['box2d.x1']), int(d7['box2d.y1'])
            pt8 = int(d7['box2d.x2']), int(d7['box2d.y2'])
            color7 = color_map[d7["category"]]
            img7 = cv2.rectangle(img7, pt7, pt8, color7, 3)
        return img7

    return (add_annotation,)


@app.cell
def _(add_annotation, cv2, tqdm, video_labels):
    cap7 = cv2.VideoCapture('026c7465-309f6d33.mp4')
    n_frames7 = int(cap7.get(cv2.CAP_PROP_FRAME_COUNT))

    VIDEO_CODEC = "MP4V"
    fps7 = 30
    width7 = 1280
    height7 = 720 

    out7 = cv2.VideoWriter(
        "out_test.mp4",
        cv2.VideoWriter_fourcc(*VIDEO_CODEC),
        fps7,
        (width7, height7)
    )

    for frame7 in tqdm(range(n_frames7), total = n_frames7):
        ret7, img7 = cap7.read()
        if ret7 == False:
            break
        img7 = add_annotation(img7, frame7, video_labels)
        out7.write(img7)

    out7.release()
    cap7.release()
    return


@app.cell
def _():
    # !ls -GFlash -color
    return


@app.cell
def _(subprocess):
    tmp_output_path = "out_test.mp4"
    output_path = "out_test_compressed.mp4"
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            tmp_output_path,
            "-crf",
            "18",
            "-preset",
            "veryfast",
            "-vcodec",
            "libx264",
            output_path,
            "-loglevel",
            "quiet"
        ]
    )
    return


@app.cell
def _():
    # !ls -GFlash --color
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## === Finalized Display Video === ##
    """)
    return


@app.cell
def _(mo):
    """ Option 1: marimo only """
    mo.video(src="out_test_compressed.mp4", width="600", controls=True, autoplay=False)
    return


@app.cell
def _(VideoFileClip):
    """ Option 2: moviepy (more universal) """
    clip7 = VideoFileClip("out_test_compressed.mp4")
    new_clip7 = (
            clip7
            .subclipped()
            .resized(width=600)
            .with_fps(30)
            .with_duration(6)
               )
    # apply audio=False to use play/pause function
    # otherwise it will autoplay until completion
    new_clip7.preview(audio=False)
    return


if __name__ == "__main__":
    app.run()
