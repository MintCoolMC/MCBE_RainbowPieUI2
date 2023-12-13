import demjson
import os
import zipfile

# Read the json file
data = demjson.decode_file("ui/_global_variables.json")

# Get the values
name = data.get("$mintui_pack_name").replace(" ","")
version = data.get("$mintui_pack_version")
branch = data.get("$rainbowpieui_branch_name")
mcversion = data.get("$rainbowpieui_version_minecraft_target")

# Create the zip file name
zip_file_name = f"{name}-v{version}.{branch}_{mcversion}.zip"

# Run the zip command
os.system(f"zip -r \"{zip_file_name}\" . -x '.github/*' -x '.git/*' -x 'zipmcproject.py'")