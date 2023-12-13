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

# Zip the project files
with zipfile.ZipFile(zip_file_name, "w") as z:
  for file in os.listdir("."):
    if file != "ui/_global_variables.json" and file != zip_file_name:
      z.write(file)
