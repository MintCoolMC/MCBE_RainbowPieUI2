import demjson
import os
import zipfile
import re

# Get the current commit id
commit_id = os.popen("git rev-parse --short HEAD").read().strip()

with open("ui/_global_variables.json", "r+", encoding="utf-8") as f:
    text = f.read()
    pattern = r'\$rainbowpieui_commit_id": ".*?"'
    text = re.sub(pattern, f'$rainbowpieui_commit_id": "{commit_id}"', text)
    f.seek(0)
    f.write(text)
    f.close()

# Read the json file
data = demjson.decode_file("ui/_global_variables.json")

# Get the values
name = data.get("$mintui_pack_name").replace(" ","")
version = data.get("$mintui_pack_version")
branch = data.get("$rainbowpieui_branch_name")
mcversion = data.get("$rainbowpieui_version_minecraft_target")

# Create the zip file name
zip_file_name = f"{name}-v{version}.{branch}_{mcversion}.mcpack"

# Run the zip command
os.system(f"zip -r \"{zip_file_name}\" . -x '.github/*' -x '.git/*' -x 'zipmcproject.py'")