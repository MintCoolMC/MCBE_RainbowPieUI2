import demjson
import os
import zipfile
import re

def writeGlobalVarStr(key,value):
  with open("ui/_global_variables.json", "r+", encoding="utf-8") as f:
    text = f.read()
    pattern = r'"\$'+key+'": ".*?"'
    text = re.sub(pattern, f'"$'+key+'": "'+value+'"', text)
    f.seek(0)
    f.truncate(0)
    f.write(text)

commit_id = os.popen("git rev-parse --short HEAD").read().strip()
branch = os.popen("git rev-parse --abbrev-ref HEAD").read().strip()

writeGlobalVarStr("rainbowpieui_commit_id",commit_id)
writeGlobalVarStr("rainbowpieui_branch_name",branch)

# Read the json file
data = demjson.decode_file("ui/_global_variables.json")

# Get the values
name = data.get("$mintui_pack_name").replace(" ","")
version = data.get("$mintui_pack_version")
branch = data.get("$rainbowpieui_branch_name")
mcversion = data.get("$rainbowpieui_version_minecraft_target")
engineversion = data.get("$rainbowpieui_engine_version_name")

writeGlobalVarStr("rainbowpieui_full_version_name",version+"."+branch)

# Create the zip file name
zip_file_name = f"{name}-v{version}.{branch}-{commit_id}.mcpack"
if data.get("$rainbowpieui_branch_type") == "release":
  zip_file_name = f"{name}-v{engineversion}_{mcversion}.mcpack" 

# Run the zip command
os.system(f"zip -r \"{zip_file_name}\" . -x '.github/*' -x '.git/*' -x 'zipmcproject.py' -x 'README.md'")
