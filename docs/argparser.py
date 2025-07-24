import argparse
import os
from pathlib import Path

def get_cwd():
    return Path(os.getcwd())

def argument_parser(parser):
    parser.add_argument("-v", "--verbose", action="store_true", help="Add verbosity to the program")

    subparsers = parser.add_subparsers(dest="command", required=True)

    #ls
    parser_ls = subparsers.add_parser("ls", help="List the directories of the current working directory")

    #chdir
    parser_chdir = subparsers.add_parser("chdir", help="Change the current working directory")
    parser_chdir.add_argument("DIRECTORY")

    #mkdir
    parser_mkdir = subparsers.add_parser("mkdir", help="Create a directory for the current working directory")
    parser_mkdir.add_argument("NAME")
    parser_mkdir.add_argument("LOCATION", nargs="?" ,default=get_cwd())

    #init
    parser_init = subparsers.add_parser("init", help="Create a writable file")
    parser_init.add_argument("NAME")
    parser_init.add_argument("LOCATION", nargs="?", default=get_cwd())
    
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
    parser_find.add_argument("DIRECTORY", nargs="?" , default=get_cwd())

    parser_find.add_argument("-t", "--type", help="Find a file by type")
    parser_find.add_argument("-n", "--name", help="Find a file by name")
    parser_find.add_argument("-s", "--size", help="Find a file by size")

    #copy
    parser_copy = subparsers.add_parser("copy", help="Copy a file or folder to another")
    parser_copy.add_argument("PATH")
    parser_copy.add_argument("LOCATION",  nargs="?", default=get_cwd())
    parser_copy.add_argument("NEW_NAME",  nargs="?", default=None)

    #rename
    parser_rename = subparsers.add_parser("rename", help="Rename a file/directory")
    parser_rename.add_argument("PATH")
    parser_rename.add_argument("NEW_NAME")

    args = parser.parse_args()
    return args