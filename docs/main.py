import os
import argparse
import sys
from pathlib import Path
import shutil
from datetime import datetime
import time
#import colorama
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
CURRENT_WORKING_DIRECTORY = Path(os.getcwd())

COMMANDS = {
        "ls": lambda args: list_dir(CURRENT_WORKING_DIRECTORY),
        "mkdir": lambda args: make_dir(args.NAME, args.LOCATION),
        "init": lambda args: init_file(args.NAME, args.LOCATION),
        "rm": lambda args: remove(args.PATH, args.recursive, args.force),
        "org": lambda args: organize(args.DIRECTORY),
        "unorg": lambda args: unorganize(args.DIRECTORY),
        "find": lambda args: find(args.DIRECTORY, args.type, args.name, args.size),
        "copy": lambda args: copy(args.PATH, args.LOCATION, args.NEW_NAME),
        "rename": lambda args: rename(args.PATH, args.NEW_NAME),

    }



def list_dir(PATH: Path|str):
    print(f"Listing all directories in: {PATH}")

def make_dir(NAME: str, LOCATION: Path | str):
    # NAME = Path(NAME)
    LOCATION = Path(LOCATION)
    print(f"Creating {NAME} directory in: {LOCATION}")

def init_file(NAME: str, LOCATION: Path | str):
    
    LOCATION = Path(LOCATION)
    print(f"Creating {NAME} file in: {LOCATION}")

def remove(PATH: Path | str, IsRecursive: bool, IsForced: bool):
    PATH = Path(PATH)
    print(f"{"Forcefully" if IsForced else ""} {"Recursively" if IsRecursive else ""} removing: {PATH}")

def organize(DIRECTORY: Path | str):
    DIRECTORY = Path(DIRECTORY)
    print(f"Organizing: {DIRECTORY}")

def unorganize(DIRECTORY: Path | str):
    DIRECTORY = Path(DIRECTORY)
    print(f"Unorganizing: {DIRECTORY}")

def find(DIRECTORY: Path|str, TYPE : str, NAME : str, SIZE : str):
    DIRECTORY = Path(DIRECTORY)
    print(f"Searching for file in: {DIRECTORY} {f"with type of: {TYPE}" if TYPE else ""} {f"with name of: {NAME}" if NAME else ""} {f"with size of: {SIZE}" if SIZE else ""}")

def copy(PATH: Path|str, LOCATION: Path|str, NEW_NAME: str):
    PATH = Path(PATH)
    LOCATION = Path(LOCATION)
    if not NEW_NAME:
        NEW_NAME = "filler"
    print(f"Copying: {PATH} to {LOCATION} with name of: {NEW_NAME + "_backup"}")

def rename(PATH: Path|str, NEW_NAME: str):
    PATH = Path(PATH)
    print(f"Naming {PATH} to {NEW_NAME}")



def main():
    parser = argparse.ArgumentParser(description="File Manager CLI")
    parser.add_argument("-v", "--verbose", action="store_true", help="Add verbosity to the program")

    subparsers = parser.add_subparsers(dest="command", required=True)

    #ls
    parser_ls = subparsers.add_parser("ls", help="List the directories of the current working directory")

    #mkdir
    parser_mkdir = subparsers.add_parser("mkdir", help="Create a directory for the current working directory")
    parser_mkdir.add_argument("NAME")
    parser_mkdir.add_argument("LOCATION", nargs="?" ,default=CURRENT_WORKING_DIRECTORY)

    #init
    parser_init = subparsers.add_parser("init", help="Create a writable file")
    parser_init.add_argument("NAME")
    parser_init.add_argument("LOCATION", nargs="?", default=CURRENT_WORKING_DIRECTORY)
    
    #rm 
    parser_rm = subparsers.add_parser("rm", help="Remove a file/dir by path")
    parser_rm.add_argument("PATH")
    parser_rm.add_argument("-r", "--recursive",action="store_true" ,help="Recursively remove all files in directory")
    parser_rm.add_argument("-f", "--force", action="store_true", help = "Forcefully remove a file")
    

    #org
    parser_org = subparsers.add_parser("org", help="Organize a directory by type")
    parser_org.add_argument("DIRECTORY")

    #unorg
    parser_unorg = subparsers.add_parser("unorg", help="Unorganize a directory by type")
    parser_unorg.add_argument("DIRECTORY")

    #find 
    parser_find = subparsers.add_parser("find", help="Find a file")
    parser_find.add_argument("DIRECTORY", nargs="?" , default=CURRENT_WORKING_DIRECTORY)

    parser_find.add_argument("-t", "--type", help="Find a file by type")
    parser_find.add_argument("-n", "--name", help="Find a file by name")
    parser_find.add_argument("-s", "--size", help="Find a file by size")

    #copy
    parser_copy = subparsers.add_parser("copy", help="Copy a file or folder to another")
    parser_copy.add_argument("PATH")
    parser_copy.add_argument("LOCATION",  nargs="?", default=CURRENT_WORKING_DIRECTORY)
    parser_copy.add_argument("NEW_NAME",  nargs="?", default=None)

    #rename
    parser_rename = subparsers.add_parser("rename", help="Rename a file/directory")
    parser_rename.add_argument("PATH")
    parser_rename.add_argument("NEW_NAME")

    args = parser.parse_args()

    print(args)
    try:
        if args.command in COMMANDS:
            COMMANDS[args.command](args)
        else:
            parser.print_help()
    except Exception as e:
        print(f"Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    START = time.perf_counter() 
    main()
    print(f"[Finished in {(time.perf_counter()-START):.5f}s]")

