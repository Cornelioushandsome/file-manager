import os
import argparse
from pathlib import Path

from datetime import datetime
import time
from urllib.parse import *

from commands import *
from argparser import *
import json
#import colorama

def save_cwd(DIRECTORY: Path|str):
    with CONFIG_PATH.open("w") as f:
        json.dump({"cwd": str(DIRECTORY.resolve())}, f)

def change_directory(DIRECTORY: Path|str): #change so it gets relative path
    target = Path(DIRECTORY).expanduser().resolve()

    if not isValidDir(target):
        print(f"Directory does not exist")
        return

    os.chdir(target)
    save_cwd(target)
    print(f"Changed current path to {target}")
    print(f"Current path is now: {get_cwd()}")

COMMANDS = {
        "ls": lambda args: list_dir(get_cwd()),
        "chdir": lambda args: change_directory(args.DIRECTORY),
        "mkdir": lambda args: make_dir(args.NAME, args.LOCATION),
        "init": lambda args: init_file(args.NAME, args.LOCATION),
        "rm": lambda args: remove(args.PATH, args.recursive, args.force),
        "org": lambda args: organize(args.DIRECTORY),
        "unorg": lambda args: unorganize(args.DIRECTORY),
        "find": lambda args: find(args.DIRECTORY, args.type, args.name, args.size),
        "copy": lambda args: copy(args.PATH, args.LOCATION, args.NEW_NAME),
        "rename": lambda args: rename(args.PATH, args.NEW_NAME),

    }

def main():
    parser = argparse.ArgumentParser(description="File Manager CLI")
    args = argument_parser(parser)

    print(args, "\n")
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

    print(f"\n[Finished in {(time.perf_counter()-START):.5f}s]")

