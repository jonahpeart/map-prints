from pathlib import Path
import shutil

def stage_maps_for_github():
    # 1. Your source map folder
    source_base = Path.home() / "Desktop" / "Maps" / "Cities"
    
    # 2. UPDATE THIS to the path of your local GitHub repository folder 
    # (Where GitHub Desktop saved your repo on your computer)
    local_repo_path = Path.home() / "Documents" / "GitHub" / "YOUR_REPO_NAME"
    
    maps_dest_dir = local_repo_path / "maps"
    
    if not source_base.exists():
        print(f"Source folder not found: {source_base}")
        return
        
    if not local_repo_path.exists():
        print(f"GitHub repository folder not found at: {local_repo_path}")
        print("Please update 'local_repo_path' in the script to match your actual local repo location.")
        return

    # Create destination 'maps' folder inside the repo
    maps_dest_dir.mkdir(parents=True, exist_ok=True)

    print("Copying map files into your local GitHub repository...")
    copied_count = 0

    # Loop through each city folder and copy its exports
    for city_folder in source_base.iterdir():
        if city_folder.is_dir():
            exports_path = city_folder / "exports"
            if exports_path.exists() and exports_path.is_dir():
                dest_city_exports = maps_dest_dir / city_folder.name / "exports"
                dest_city_exports.mkdir(parents=True, exist_ok=True)
                
                for img in exports_path.glob("*.*"):
                    if img.suffix.lower() in [".png", ".jpg", ".jpeg"]:
                        dest_file = dest_city_exports / img.name
                        shutil.copy2(img, dest_file)
                        copied_count += 1

    print(f"\nDone! Successfully copied {copied_count} files into your local repo.")
    print(f"Now, open your GitHub Desktop app—it will show all the new files ready to commit and push!")

if __name__ == "__main__":
    stage_maps_for_github()