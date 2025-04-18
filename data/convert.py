import pandas as pd
import os
import glob

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