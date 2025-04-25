import os
from osfclient import OSF
import configparser


# Read the .osfcli.config file
config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), '.osfcli.config')
print(f"Config file path: {config_path}")
config.read(config_path)

def fetch_data_from_osf():
  # Connect to OSF with authorization for private projects
  osf = OSF(token = config['osf']['token'])
  project = osf.project(config['osf']['project'])
  storage = project.storage(config['osf']['storage'])

  # Check if there are any JSON files to fetch
  json_files = [file for file in storage.files if file.name.endswith('.json')]

  if json_files:
    os.makedirs('json', exist_ok=True)

    # Fetch all JSON files from the storage
    for file in json_files:
      file_path = os.path.join("json", file.name)
      with open(file_path, 'wb') as f:
        file.write_to(f)
    return True
  return False

if __name__ == "__main__":
  # Fetch data from OSF
  try:
    data_fetched = fetch_data_from_osf()
    print("Fetching finished!")
  except:
    print("No JSON files found to fetch.")