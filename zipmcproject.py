import demjson
import os
import zipfile
import re

def writeGlobalVarStr(key,value):
  with open("ui/_global_variables.json", "w", encoding="utf-8") as f:
    text = f.read()
    pattern = r'"\$'+key+'": ".*?"'
    text = re.sub(pattern, f'"$'+key+'": "'+value+'"', text)
    print("[writeVar] "+text)
    # f.seek(0)
    f.write(text)
    # f.close()

commit_id = os.popen("git rev-parse --short HEAD").read().strip()
branch = os.popen("git rev-parse --abbrev-ref HEAD").read().strip()

writeGlobalVarStr("rainbowpieui_commit_id",commit_id)
writeGlobalVarStr("rainbowpieui_branch_name",branch)
os.system(f"zip -r \"test.mcpack\" . -x '.github/*' -x '.git/*' -x 'zipmcproject.py'")

# # Read the json file
# data = demjson.decode_file("ui/_global_variables.json")

# # Get the values
# name = data.get("$mintui_pack_name").replace(" ","")
# version = data.get("$mintui_pack_version")
# branch = data.get("$rainbowpieui_branch_name")
# mcversion = data.get("$rainbowpieui_version_minecraft_target")

# # Create the zip file name
# zip_file_name = f"{name}-v{version}.{branch}_{mcversion}.mcpack"

# # Run the zip command
# os.system(f"zip -r \"{zip_file_name}\" . -x '.github/*' -x '.git/*' -x 'zipmcproject.py'")
