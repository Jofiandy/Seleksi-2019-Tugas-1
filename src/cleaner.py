import os
import glob

def erase_images_in_screenshot_directory():
    # Erasing All Files in the Screenshot Directory
    files_screenshot = glob.glob('screenshots/*')
    for f in files_screenshot:
        os.remove(f)
    file_data = glob.glob('data/result.json')
    os.remove(file_data[0])

if __name__ == '__main__':
    try:
        erase_images_in_screenshot_directory()
    except Exception:
        raise Exception('Directory not found')
