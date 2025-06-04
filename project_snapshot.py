import os

# Settings
output_file = "project_snapshot.txt"
include_extensions = {".html", ".htm", ".js", ".css", ".py", ".json", ".txt"}
exclude_dirs = {".git", "__pycache__", "node_modules", "venv", ".venv", ".idea", ".DS_Store"}

def is_valid_file(file_name):
    return any(file_name.endswith(ext) for ext in include_extensions)

def should_exclude_dir(dir_name):
    return any(part in exclude_dirs for part in dir_name.split(os.sep))

def generate_snapshot(root_dir="."):
    with open(output_file, "w", encoding="utf-8") as f:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # Skip excluded directories
            if should_exclude_dir(dirpath):
                continue

            depth = dirpath.count(os.sep)
            indent = "  " * depth
            f.write(f"{indent}{os.path.basename(dirpath)}/\n")

            for filename in sorted(filenames):
                file_path = os.path.join(dirpath, filename)
                if is_valid_file(filename):
                    file_indent = "  " * (depth + 1)
                    f.write(f"{file_indent}{filename}\n")
                    try:
                        with open(file_path, "r", encoding="utf-8") as code_file:
                            content = code_file.read()
                            for line in content.splitlines():
                                f.write(f"{file_indent}  {line}\n")
                    except Exception as e:
                        f.write(f"{file_indent}  [Error reading file: {e}]\n")
                else:
                    file_indent = "  " * (depth + 1)
                    f.write(f"{file_indent}{filename} [skipped]\n")

if __name__ == "__main__":
    generate_snapshot()
    print(f"Snapshot saved to {output_file}")