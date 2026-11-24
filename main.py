
import os
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".ts", ".html", ".css", ".java", ".cpp"]
}


def organize_files(folder_path):
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print("Invalid folder path!")
        return

    moved = 0

    for file in folder.iterdir():
        if not file.is_file():
            continue

        category = next(
            (name for name, extensions in CATEGORIES.items()
             if file.suffix.lower() in extensions),
            "Others"
        )

        destination = folder / category
        destination.mkdir(exist_ok=True)

        target = destination / file.name

        if target.exists():
            target = destination / f"{file.stem}_copy{file.suffix}"

        shutil.move(str(file), str(target))
        print(f"Moved: {file.name} -> {category}/")
        moved += 1

    print(f"\nOrganization completed! {moved} files moved.")


if __name__ == "__main__":
    path = input("Enter folder path: ")
    organize_files(path)
