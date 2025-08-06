import os
from datetime import datetime
from .magic_tools import ensure_dir, clean_filename  # relative import

def save_text_to_folder(folder: str, content: str, prefix: str = "entry") -> str:
    """
    Save plain text content to a file in the specified folder.
    The filename will be prefixed with a label and timestamp.
    """
    ensure_dir(folder)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{prefix}_{timestamp}.txt"
    full_path = os.path.join(folder, clean_filename(filename))

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip())

    return full_path
