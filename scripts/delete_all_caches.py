import os
import subprocess

os.chdir('..')


def check_directories(path):
    if path not in ['env', 'venv']:
        if os.path.isdir(path):
            name = os.path.basename(path)
            if name == '__pycache__':
                subprocess.run(['rm', '-rf', path])
                return
            items = os.listdir(path)
            for item in items:
                item_path = os.path.join(path, item)
                check_directories(item_path)


dirs = os.listdir()


def main():
    for _ in dirs:
        check_directories(_)


if __name__ == '__main__':
    main()
