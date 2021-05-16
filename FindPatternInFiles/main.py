import os
import re

path = r"C:\Users\Creap\Desktop\extracted_content"
for folder, subfolders, files in os.walk(path):
    for file in files:
        with open(folder + "\\" + file, "r") as f:
            file_content = f.readlines()
            pattern = r"\d{3}-\d{3}-\d{4}"
            for text in file_content:
                match = re.search(pattern, text)
                if match is not None:
                    print(match.group())
            pass
