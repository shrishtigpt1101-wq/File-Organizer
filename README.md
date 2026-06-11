# File Organizer

A simple Python script that organizes image files by moving `.png` files into an `images` folder.

## Description

This script scans the current directory and moves all files with the `.png` extension into a new `images` directory. It renames moved files using the pattern `photo-1.png`, `photo-2.png`, and so on.

## Features

- Detects `.png` files in the current working directory
- Creates an `images` folder if it does not already exist
- Moves and renames `.png` files into the `images` folder

## Requirements

- Python 3.x

## Usage

1. Place `FileOrganizer.py` in the folder where you want to organize files.
2. Open a terminal in that folder.
3. Run:

```bash
python "File Organizer/FileOrganizer.py"
```

The script will:

- create an `images` folder if needed
- move `.png` files into that folder
- rename moved files as `photo-1.png`, `photo-2.png`, etc.

## Notes

- The script currently only handles `.png` files.
- You can extend the `arrange_files` function to support additional extensions and categories.
- Be careful running this in directories with important files, since files will be renamed and moved.

## Project Structure

- `File Organizer/FileOrganizer.py` - main Python script
- `File Organizer/images/` - target folder for sorted `.png` files
