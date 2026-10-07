# JPG File Organizer

## Task 3 - Task Automation with Python Scripts

This project automates the process of finding JPG files from a
source folder and moving them to a destination folder.

## Objective

The main objective of this project is to automate a repetitive
file management task using Python.

Instead of manually searching for JPG files and moving them,
the Python script performs the task automatically.

## Features

- Finds JPG files automatically
- Moves JPG files to another folder
- Supports `.jpg`, `.JPG`, `.Jpg`, etc.
- Creates the destination folder automatically
- Handles duplicate filenames
- Displays the number of files moved
- Displays useful status messages

## Technologies Used

- Python
- os module
- shutil module
- File handling

## Python Modules

### os

The `os` module is used for:

- Checking whether folders exist
- Reading files from folders
- Creating file paths
- Checking whether an item is a file

### shutil

The `shutil` module is used to move files from one folder
to another.

## Project Structure

JPG File Organizer/

├── file_organizer.py

├── README.md

├── source_folder/

│   ├── photo1.jpg

│   ├── photo2.jpg

│   ├── photo3.JPG

│   ├── document.txt

│   └── image.png

└── destination_folder/

## How to Run

### Step 1

Install Python on your computer.

### Step 2

Open the project folder in VS Code.

### Step 3

Open the VS Code terminal.

### Step 4

Run the following command:

python file_organizer.py

### Step 5

Enter the source folder path.

Example:

C:\Users\YourName\Desktop\JPG File Organizer\source_folder

### Step 6

Enter the destination folder path.

Example:

C:\Users\YourName\Desktop\JPG File Organizer\destination_folder

## Example

Before running the program:

source_folder/

- photo1.jpg
- photo2.jpg
- photo3.JPG
- document.txt
- image.png

destination_folder/

After running the program:

source_folder/

- document.txt
- image.png

destination_folder/

- photo1.jpg
- photo2.jpg
- photo3.JPG

## Expected Output

====================================
       JPG FILE ORGANIZER
====================================

This program moves all JPG files
from one folder to another.

Enter source folder path:
Enter destination folder path:

🔍 Searching for JPG files...

✅ Moved: photo1.jpg
✅ Moved: photo2.jpg
✅ Moved: photo3.JPG

====================================
          TASK COMPLETED
====================================
Total JPG files moved: 3
====================================

## Learning Outcome

This project demonstrates how Python can be used to automate
repetitive file management tasks.

The project provides practical experience with:

- Python functions
- File handling
- Directory handling
- os module
- shutil module
- Conditional statements
- Loops
- Exception prevention
- Automation

## Author

Task 3 - Python Task Automation