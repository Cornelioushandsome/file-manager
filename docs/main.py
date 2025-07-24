import os
import argparse
from pathlib import Path

from datetime import datetime
import time
from urllib.parse import *

from commands import *
from argparser import *
#import colorama


os.chdir(r"C:/Users/jackr/OneDrive/Desktop")

COMMANDS = {
        "ls": lambda args: list_dir(get_cwd()),
        "chdir": lambda args: change_dir(args.DIRECTORY),
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

