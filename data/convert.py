import pandas as pd
import os
import glob
from osfclient import OSF

# Connect to OSF with authorization for private projects
osf = OSF(username='m.e.de.jong.6@student.rug.nl', password='Sup3rfruit')

# Load the project
project = osf.project('29fg4')

# Access the OSF Storage
storage = project.storage('osfstorage')

# Ensure the 'json' folder exists before downloading files
os.makedirs('json', exist_ok=True)

# Loop through all files and download .json files
for file in storage.files:
    if file.name.endswith('.json'):
        print(f"Downloading: {file.name}")
        with open(f'json/{file.name}', 'wb') as f:
            file.write_to(f)

def convertFile(json, csv):
    df = pd.read_json(json)

    # Keep only the specified columns
    df = df[["group", "participant", "date", "practice.thisTrialN", "implicatures.thisTrialN", "lexTALE.thisTrialN", 
             "condition", "id", "scale_type", "scale_term", "respSI_RT.keys", "respSI_RT.rt", 
             "word", "status", "respLDT.corr", "respLDT.rt"]]

    # Ensure the 'csv' folder exists before saving the file
    os.makedirs('csv', exist_ok=True)
    df.to_csv("csv/" + csv, index=False)


# Get all JSON files in the 'json' folder
dataFiles = glob.glob('json/*.json')

for file in dataFiles:
    filename = os.path.splitext(os.path.basename(file))[0] + ".csv"
    print(f"Converting {file} to csv/{filename}")
    convertFile(file, filename)