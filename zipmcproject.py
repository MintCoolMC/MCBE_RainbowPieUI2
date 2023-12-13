import demjson
import os
import zipfile

# Read the json file
with open("ui/_global_variables.json", "r") as f:
  data = demjson.load(f)

# Get the name and version values
name = data.get("$mintui_pack_name")
version = data.get("$mintui_pack_version")

# Create the zip file name
zip_file_name = f"{name}_{version}.zip"

# Zip the project files
with zipfile.ZipFile(zip_file_name, "w") as z:
  for file in os.listdir("."):
    if file != "ui/_global_variables.json" and file != zip_file_name:
      z.write(file)

# Upload the zip file
# You can use the same upload action as before
