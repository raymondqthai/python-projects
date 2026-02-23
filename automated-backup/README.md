# Automated File Backup

A Python script that backs up a folder to a destination directory on a daily schedule. Each backup creates a new subfolder named with the current date. Built as a learning project to practice file operations, scheduling, and automation.

---

## Features

- Copies a source folder to a destination directory daily
- Names each backup folder with the current date
- Skips the backup if a folder for that date already exists
- Runs on a schedule in the background using a continuous loop

---

## Requirements

- Python 3.x

Install the required library:

```
pip install schedule
```

---

## Setup

1. Clone the repository
   ```
   git clone https://github.com/yourusername/automated-file-backup.git
   ```
2. Navigate to the folder
   ```
   cd automated-file-backup
   ```
3. Open `3_automated_file_backup.py` and update these two lines with your own paths:
   ```python
   source_dir = "/your/source/folder"
   destination_dir = "/your/destination/folder"
   ```
4. Set your preferred backup time on this line:
   ```python
   schedule.every().day.at("00:00").do(...)
   ```
5. Run the script
   ```
   python 3_automated_file_backup.py
   ```

Keep the terminal open. The script runs continuously and checks the schedule every 60 seconds.

---

## Usage

```
$ python 3_automated_file_backup.py
Folder copied to: /your/destination/folder/2025-12-25
```

If a backup for that date already exists:

```
Folder already exists in /your/destination/folder
```

---

## What I Learned

- How to copy a directory tree using `shutil.copytree`
- How to build a dated folder path using `os.path.join` and `datetime`
- How to schedule a recurring task with the `schedule` library
- How to use a `while True` loop to keep a script running in the background
- How to use a lambda function to pass arguments into a scheduled job

---

## Credits

Based on Project 3 of 3 from "3 Python Automation Projects - For Beginners" by Tech With Tim.
Tutorial: [https://www.youtube.com/watch?v=zT7niRUOs9o](https://www.youtube.com/watch?v=zT7niRUOs9o)