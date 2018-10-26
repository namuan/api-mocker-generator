def write_output(file_path: str, file_content: str):
    with open(file_path, 'w') as f:
        f.write(file_content)
