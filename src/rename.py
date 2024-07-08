import os

def rename_images(folder_path):
    files = os.listdir(folder_path)
    
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]
    
    for i, filename in enumerate(image_files):
        new_name = f"frame{i + 1}.jpg"
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_name)
        
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {old_file_path} to {new_file_path}")

folder_path = '/Users/soorhansalia/Lab/Stake'
rename_images(folder_path)
