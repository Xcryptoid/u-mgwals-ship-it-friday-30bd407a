import os
import shutil

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile("entry.txt", os.path.join(out_dir, "entry.txt"))

# This little script does nothing clever on purpose. The joke was already
# written and saved before the program ever runs, so all it has to do is
# hand that finished line over to the folder the grader points at. It
# creates the folder first when it is missing, then copies the file
# exactly as it stands, character for character, and exits.
