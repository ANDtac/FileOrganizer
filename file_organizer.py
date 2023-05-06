import os
import shutil
from pathlib import Path

def create_extension_map():
    return {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.ico', '.heif', '.webp', '.svg', '.raw', '.arw', '.cr2', '.nrw', '.k25', '.indd', '.psd', '.ai', '.jfif'],
        'documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.md', '.csv', '.rtf', '.tex', '.log', '.ods', '.odt', '.odp', '.pages', '.key', '.numbers', '.eml', '.msg', '.oft', '.vcf', '.vcs'],
        'audio': ['.mp3', '.wav', '.m4a', '.flac', '.ogg', '.aac', '.aiff', '.wma', '.amr', '.ape', '.au', '.ra', '.voc', '.mid', '.midi'],
        'video': ['.mp4', '.mkv', '.flv', '.avi', '.mov', '.wmv', '.3gp', '.webm', '.m4v', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.asf', '.mts', '.m2ts'],
        'archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.iso', '.cab', '.z', '.lz', '.tlz', '.lzma', '.jar', '.war', '.dmg'],
        'code': ['.py', '.js', '.html', '.css', '.php', '.c', '.cpp', '.h', '.java', '.cs', '.json', '.xml', '.yml', '.ini', '.sh', '.asp', '.aspx', '.jsp', '.go', '.rb', '.swift', '.kt', '.ts', '.tsx', '.jsx', '.pl', '.cgi', '.scala', '.rs', '.lua', '.sql', '.bat', '.cmd'],
        'fonts': ['.ttf', '.otf', '.woff', '.woff2', '.eot', '.fon', '.pfa', '.pfb', '.sfd'],
        'ebooks': ['.epub', '.mobi', '.azw3', '.fb2', '.ibook', '.pdb', '.lit'],
        '3d_models': ['.obj', '.fbx', '.dae', '.3ds', '.blend', '.ply', '.stl'],
        'spreadsheets': ['.ods', '.ots', '.sxc'],
    }

def categorize_file(file_extension, extension_map):
    for category, extensions in extension_map.items():
        if file_extension.lower() in extensions:
            return category
    return 'others'

def organize_files(source_directory, target_directory, extension_map):
    category_directories_created = set()

    for file in os.listdir(source_directory):
        file_path = os.path.join(source_directory, file)

        if os.path.isfile(file_path) and not file.startswith('.'):
            try:
                file_extension = Path(file).suffix
                category = categorize_file(file_extension, extension_map)

                if category not in category_directories_created:
                    category_directory = os.path.join(target_directory, category)
                    os.makedirs(category_directory, exist_ok=True)
                    category_directories_created.add(category)

                destination_path = os.path.join(target_directory, category, file)
                shutil.move(file_path, destination_path)
            except PermissionError:
                print(f"Permission denied for file: {file_path}")
            except Exception as e:
                print(f"Error processing file: {file_path}")
                print(f"Exception: {e}")

def main():
    source_directory = input("Enter the source directory path: ").strip()
    target_directory = input("Enter the target directory path: ").strip()

    source_directory = os.path.abspath(source_directory)
    target_directory = os.path.abspath(target_directory)

    if not os.path.isdir(source_directory):
        print("The source directory does not exist.")
        return

    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    extension_map = create_extension_map()
    organize_files(source_directory, target_directory, extension_map)
    print("Files have been organized successfully.")

if __name__ == "__main__":
    main()

