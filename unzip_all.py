Script : unzip_all.py

import zipfile import os

Liste des fichiers ZIP à décompresser
zip_files = [ "suivi_production_backend.zip", "suivi_production_frontend.zip" ]

for zip_file in zip_files: if os.path.isfile(zip_file): print(f"Décompression de {zip_file}...") with zipfile.ZipFile(zip_file, 'r') as zip_ref: extract_folder = zip_file.replace(".zip", "") # Crée un dossier pour chaque archive os.makedirs(extract_folder, exist_ok=True) zip_ref.extractall(extract_folder) print(f"{zip_file} décompressé dans {extract_folder}/") else: print(f"Fichier {zip_file} non trouvé.")
