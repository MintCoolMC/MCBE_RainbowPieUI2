import demjson
import os
import zipfile

# Read the json file
data = demjson.decode_file("ui/_global_variables.json")

# Get the values
name = data.get("$mintui_pack_name")
version = data.get("$mintui_pack_version")

# Create the zip file name
zip_file_name = f"{name}_{version}.zip"

# Run the zip command
os.system(f"zip -r {zip_file_name} . -x '.github/*' -x '.git/*' -x 'zipmcproject.py'")