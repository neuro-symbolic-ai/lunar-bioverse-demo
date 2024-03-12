import os
import sys
import json

WF_BASE_DIR = "workflows"

def index():
    index = dict()
    for wf_dir in os.listdir(WF_BASE_DIR):
        if (os.path.isdir(os.path.join(WF_BASE_DIR, wf_dir))):
            with open(os.path.join(WF_BASE_DIR, wf_dir, f"{wf_dir}.json")) as wf_descr_file:
                wf_info = json.load(wf_descr_file)
                index[wf_dir] = {
                    "description": wf_info["description"],
                    "path": os.path.join(WF_BASE_DIR, wf_dir, f"{wf_dir}.json")
                }

    return index


def paths():
    for wf in index().values():
        print(wf["path"])


def main(argv):
    if (len(argv) > 1 and argv[1] == "paths"):
        paths()
    else:
        print(json.dumps(index(), indent=2))


if __name__ == "__main__":
    main(sys.argv)
