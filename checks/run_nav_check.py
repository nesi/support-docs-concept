#!/usr/bin/env python3

"""
Runs checks on article meta block and outputs in github action readable format
"""

__author__ = "cal w"

import re
import sys
import yaml
import os
import time
from pathlib import Path

MKDOCS_CONF = "mkdocs.yml"

def main():


    # mkdocs_config = yaml.safe_load(open(MKDOCS_CONF))
    # overkill

    # List of all parent paths.
    inputs = set()

    for d in sys.argv[1:]:
        p = Path(d).parent
        while p != Path("."):
            inputs.add(p)
            p = p.parent


    for input_path in inputs:
        # Get .pages.yml if exists.
        # navfile = mkdocs_config["plugins"] ["awesome-pages"]["filename"]  or ".pages"
        navfile = ".pages.yml"

        try:
            with open(Path(input_path, navfile), "r") as f:
                nav = yaml.safe_load(f.read())
            files = [ os.listdir() ]
        except Exception as e:
            print("no .pages.yml pages will be ordered alphabetically")
            print(e)
        
        over_constrain = "nav" in nav and "..." not in nav["nav"]
        if "nav" in nav and "..." not in nav["nav"]:
            print("message, nav set. no catch")

        files.pop(".pages.yml")

        if len(files) > pages_accounted:
            print("some pages in '' will not be visible in nav")

        pages_accounted = 0

        for e in nav["nav"]:
            pages_accounted += sum(re.match(e, file) for file in files)

        catchall = files.pop("...")



    def _nav_check():
        doc_root = Path(DOC_ROOT).resolve()
        rel_path = input_path.resolve().relative_to(doc_root)
        for i in range(1, len(rel_path.parts)):
            num_siblings = 0
            for file_name in os.listdir(doc_root.joinpath(Path(*rel_path.parts[:i]))):
                if not any(re.match(pattern, file_name) for pattern in EXCLUDED_FROM_CHECKS):
                    num_siblings += 1
            if num_siblings < RANGE_SIBLING[0]:
                print(
                    f"::warning file={input_path},title=meta.siblings,col=0,endColumn=99,line=1::Parent category \
                    '{rel_path.parts[i-1]}' has too few children ({num_siblings}). Try to nest '{RANGE_SIBLING[0]}'\
                    or more items here to justify it's existence."
                )
            elif num_siblings > RANGE_SIBLING[1]:
                print(
                    f"::warning file={input_path},title=meta.siblings,col=0,endColumn=99,line=1::Parent category \
                    '{rel_path.parts[i-1]}' has too many children ({num_siblings}). Try to keep number of items in\
                    a category under '{RANGE_SIBLING[1]}', maybe add some new categories?"
                )



if __name__ == "__main__":
    main()

    # FIXME terrible hack to make VSCode in codespace capture the error messages
    # see https://github.com/microsoft/vscode/issues/92868 as a tentative explanation
    time.sleep(5)
