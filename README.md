# Folder Utils

A simple Python library for folder and file manipulation using an object-oriented approach.

## Installation

You can install this library locally by running the following command in the root directory (`my_folder_lib/`):

```
pip install -e .
```

## Usage

```python
from folder_utils import FolderManager

# Create an instance of FolderManager
fm = FolderManager()

# Create a folder
fm.create_folder("my_directory")

# List files in the folder (optionally filter by extension)
files = fm.list_files("my_directory", extension_filter=".txt")
print(files)

# Copy a file
fm.copy_file("source.txt", "destination.txt")

# Move a file
fm.move_file("destination.txt", "new_location.txt")

# Delete a folder
fm.delete_folder("my_directory")
```

## Features

- Create folders
- Delete folders
- List files in a folder with optional extension filtering
- Copy files
- Move files

## Requirements

- Python 3.6 or higher
