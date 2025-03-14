import os
import subprocess
def zip_with_7z(input_folder, output_archive, password, split_size_mb):
    seven_zip_path = "./7-Zip/7z.exe"
    if not os.path.exists(seven_zip_path):
        print("❌ 7-Zip is not installed or not found in the default location.")
        return

    command = [
        seven_zip_path,
        "a",
        f"{output_archive}.7z",
        input_folder,
        f"-p{password}",
        "-mhe=on",
        "-mx9",
        f"-v{split_size_mb}m",
    ]
    try:
        subprocess.run(command, check=True)
        print(f"✅ Archive created successfully: {output_archive}.7z.*")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating archive: {e}")
