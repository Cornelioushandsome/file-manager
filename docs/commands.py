from pathlib import Path
import os
import shutil
#from argparser import get_cwd

def isValidFile(PATH: Path|str)->bool:
    PATH = Path(PATH)
    return PATH.exists() and PATH.is_file()

def isValidDir(PATH: Path|str)->bool:
    PATH = Path(PATH)
    return PATH.exists() and PATH.is_dir()

def count_files_dirs(path: Path | str):
    path = Path(path)
    files = [p for p in path.iterdir() if p.is_file()]
    dirs = [p for p in path.iterdir() if p.is_dir()]
    return len(files), len(dirs)

def isEmptyDir(path: Path|str)->bool:
    path = Path(path)
    return path.is_dir and not any(path.iterdir())



class FileExtensions:

    videoExtensions = [
    ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".mpg", ".3gp", ".m4v"
    ]
    imageExtensions = [
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".ico", ".heic"
    ]
    audioExtensions = [
    ".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".alac"
    ]
    documentExtensions = [
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".odt", ".ods", ".odp"
    ]   
    archiveExtensions = [
    ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"
    ]
    codeExtensions = [
    ".py", ".c", ".cpp", ".java", ".js", ".html", ".css", ".json", ".xml", ".sh", ".php", ".rb", ".go", ".rs"
    ]
    executableExtensions = [
    ".exe", ".bat", ".cmd", ".msi", ".app", ".deb"
    ]

def list_dir(PATH: Path|str):
    try:
        PATH = Path(PATH)
        dirs = os.listdir(PATH)
        print(f"[Listing all childs under: {PATH}]")

        for directory in dirs:
            print(f"[{directory}]", end=" ")
        print()
        return
    except Exception as e:
        print(f"Error: {e}")
        return


def make_dir(NAME: str, LOCATION: Path | str):
    try:
        LOCATION = Path(LOCATION)
        new_name = LOCATION / NAME
        new_name = Path(new_name)

        os.makedirs(new_name, exist_ok=True)
        print(f"Successfully created: {NAME} in {new_name}")
        return
    
    except Exception as e:
        print(f"Error occured with \"mkdir\": {e}")
        return

def init_file(NAME: Path | str, LOCATION: Path | str): #check file if it already exists
    try:
        NAME = Path(NAME)
        LOCATION = Path(LOCATION)
        DESTINATION = LOCATION / NAME
        stem = NAME.stem
        ext = NAME.suffix

        if any(ext in group for group in [FileExtensions.codeExtensions, FileExtensions.documentExtensions]):
            with open(DESTINATION, "w") as f:
                f.write("")
            print(f"Successfully created \"{stem}\" in {DESTINATION}")
            return
        else:
            print(f"Invalid file type. Only writable files are allowed")
            return

    except Exception as e:
        print(f"Error occured with \"init\": {e}")

def remove(PATH: Path | str, IsRecursive: bool, IsForced: bool): 
    try:
        PATH = Path(PATH)
        if isValidFile(PATH):
            print(f"Removing file: {PATH}")
            PATH.unlink()
            print(f"Removed file")

        elif isValidDir(PATH):
            numFil, numDir = count_files_dirs(PATH)
            if IsRecursive:
                print(f"Removing directory: {PATH}...")
                if not isEmptyDir(PATH):
                    if not IsForced:
                        prompt = input(f"Deleting directory with: {numFil} files, {numDir} directories. Still continue? [Y/n]: ")
                        if prompt.lower() != "y":
                            print("Exiting...")
                            return
                    shutil.rmtree(PATH)
                    print(f"Removed with {numFil} files and {numDir} directories")
                else:
                    PATH.rmdir()
                    print(f"Removed empty dir")
            else:
                raise OSError(f"Cannot delete non-empty dir: {PATH} without recursive mode")
        else:
            raise OSError(f"{PATH} does not exist.")
        
        print(f"Successfully removed: {PATH}"
              f"{" recursively" if IsRecursive else ""}"
              f"{" with force" if IsForced else ""}")

    except Exception as e:
        print(f"Error occured while removing: {PATH}. {e}")
        return

def organize(DIRECTORY: Path | str): #organize this
    DIRECTORY = Path(DIRECTORY)
    print(f"Organizing: {DIRECTORY}")

def unorganize(DIRECTORY: Path | str): #unorganize this
    DIRECTORY = Path(DIRECTORY)
    print(f"Unorganizing: {DIRECTORY}")

def find(DIRECTORY: Path|str, TYPE : str, NAME : str, SIZE : str): #find this
    DIRECTORY = Path(DIRECTORY)
    print(f"Searching for file in: {DIRECTORY} {f"with type of: {TYPE}" if TYPE else ""} {f"with name of: {NAME}" if NAME else ""} {f"with size of: {SIZE}" if SIZE else ""}")

def copy(PATH: Path|str, LOCATION: Path|str, NEW_NAME: str): #copy this
    PATH = Path(PATH)
    LOCATION = Path(LOCATION)
    if not NEW_NAME:
        NEW_NAME = "filler"
    print(f"Copying: {PATH} to {LOCATION} with name of: {NEW_NAME + "_backup"}")

def rename(PATH: Path|str, NEW_NAME: str): #rename this
    PATH = Path(PATH)
    print(f"Naming {PATH} to {NEW_NAME}")
