from pathlib import Path
import shutil

def stage_maps():
    # Source where your city folders live
    source_base = Path.home() / "Desktop" / "Maps" / "Cities"
    
    # Destination inside your newly cloned repo folder
    repo_maps_dir = Path.home() / "Desktop" / "Maps" / "Bulk Import" / "map-prints" / "maps"
    
    if not source_base.exists():
        print(f"Source folder not found: {source_base}")
        return
        
    repo_maps_dir.mkdir(parents=True, exist_ok=True)
    copied_count = 0

    print("Copying map files into your local repository...")

    for city_folder in source_base.iterdir():
        if city_folder.is_dir():
            exports_path = city_folder / "exports"
            if exports_path.exists() and exports_path.is_dir():
                dest_city_exports = repo_maps_dir / city_folder.name / "exports"
                dest_city_exports.mkdir(parents=True, exist_ok=True)
                
                for img in exports_path.glob("*.*"):
                    if img.suffix.lower() in [".png", ".jpg", ".jpeg"]:
                        shutil.copy2(img, dest_city_exports / img.name)
                        copied_count += 1

    print(f"Successfully copied {copied_count} files!")
    print("Now check GitHub Desktop—all your files will be waiting there.")

if __name__ == "__main__":
    stage_maps()