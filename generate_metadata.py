import csv
import json
import os

# Create metadata directory
os.makedirs("metadata", exist_ok=True)

# Path to the uploaded csv file
csv_file_path = "blorps.csv"

# Base URI for images hosted on your other repository
base_image_url = "https://raw.githubusercontent.com/blorpsart/blorpsimage/main/images/"

with open(csv_file_path, mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    
    for row in reader:
        # Fetching the ID (0, 1, 2...)
        token_id = row.get("ID")
        if not token_id:
            continue
            
        # Standard NFT Metadata Structure
        metadata = {
            "name": f"Blorps #{token_id}",
            "description": f"Blorps NFT Collection Item #{token_id}",
            "image": f"{base_image_url}{token_id}.webp",
            "attributes": []
        }
        
        # Dynamically adding traits from CSV columns (Type, Eyes, Accessory, Headwear)
        for key, value in row.items():
            if key != "ID" and value.strip():
                metadata["attributes"].append({
                    "trait_type": key,
                    "value": value.strip()
                })
        
        # Save file without any extension (e.g., 0, 1, 2)
        file_path = os.path.join("metadata", token_id)
        with open(file_path, "w", encoding="utf-8") as outfile:
            json.dump(metadata, outfile, indent=4)

print("Metadata generation completed successfully.")
