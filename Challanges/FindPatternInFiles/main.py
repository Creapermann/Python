import os
import re

path = r"C:\Users\Creap\Desktop\extracted_content"
for folder, subfolders, files in os.walk(path):
    for file in files:
        with open(folder + "\\" + file, "r") as f:
            file_content = f.readlines()
            for text in file_content:
                match = re.search(r"\d{3}-\d{3}-\d{4}", text)
                if match is not None:
                    print(match.group())
