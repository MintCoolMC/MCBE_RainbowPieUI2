import demjson
import os
import zipfile

# Get the current commit id
commit_id = os.popen("git rev-parse HEAD").read().strip()

# Read the json file
data = demjson.decode_file("ui/_global_variables.json")

data["$rainbowpieui_commit_id"] = commit_id

# Write back to the json file
with open("ui/_global_variables.json", "w") as f:
  demjson.encode(data, f, indent=4, compactly=False)

# Get the values
name = data.get("$mintui_pack_name").replace(" ","")
version = data.get("$mintui_pack_version")
branch = data.get("$rainbowpieui_branch_name")
mcversion = data.get("$rainbowpieui_version_minecraft_target")

# Create the zip file name
zip_file_name = f"{name}-v{version}.{branch}_{mcversion}.mcpack"

# Run the zip command
os.system(f"zip -r \"{zip_file_name}\" . -x '.github/*' -x '.git/*' -x 'zipmcproject.py'")