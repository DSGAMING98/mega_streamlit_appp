import os

def ensure_dir(path: str):
    """Make sure a directory exists."""
    os.makedirs(path, exist_ok=True)

def clean_filename(filename: str) -> str:
    """Sanitize filenames (remove spaces, weird characters, etc.)."""
    return filename.replace(" ", "_").replace(":", "-")

def list_files(directory: str, extension: str = None):
    """List files in a directory, optionally filtered by extension."""
    files = os.listdir(directory)
    if extension:
        files = [f for f in files if f.lower().endswith(extension)]
    return sorted(files, reverse=True)
