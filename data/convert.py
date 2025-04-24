import pandas as pd
import os
import glob

def convertFile(json, csv):
  df = pd.read_json(json)

  # Ensure the 'csv' folder exists within the function
  os.makedirs('csv', exist_ok=True)

  # Keep only the specified columns
  df = df[["group", "participant", "date", "thisTrialN", "id", 
           "condition", "scale_type", "scale_term", "respSI_RT.rt", "respSI_RT.implicature","respSI_RT.corr", 
           "word", "status", "respLDT.corr", "respLDT.rt"]]

  # Save the final CSV to the 'csv' folder
  csv_filename = os.path.splitext(csv)[0] + '.csv'
  csv_path = os.path.join("csv", csv_filename)
  df.to_csv(csv_path, index=False, encoding='utf-8-sig')

if __name__ == "__main__":
  # Convert all JSON files in the 'json' folder to CSV
  json_files = glob.glob('json/*.json')
  for json_file in json_files:
    convertFile(json_file, os.path.basename(json_file))
  
  print("All files were converted successfully. Press Enter to close the terminal.")
  input()
