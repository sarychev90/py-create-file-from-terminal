import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv
    full_path = os.getcwd()
    file_name = ""
    directories = []
    if args[1] == "-d":
        for directory in args[2:]:
            if not directory.startswith("-"):
                directories.append(directory)
            else:
                break
    else:
        for index in range(len(args)):
            if args[index] == "-d":
                for directory in args[index + 1:]:
                    if not directory.startswith("-"):
                        directories.append(directory)
                    else:
                        break
    if directories:
        full_path = os.path.join(full_path, *directories)
        os.makedirs(full_path, exist_ok=True)
    if args[1] == "-f":
        file_name = args[2]
    else:
       for index in range(len(args)):
           if args[index] == "-f":
               file_name = args[index+1]
               break
    file_path = os.path.join(full_path, file_name)
    file_exists = os.path.exists(file_path)
    with open(file_path, "a" if file_exists else "w") as file:
        file.write("\n" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_counter = 1
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            file.write(str(line_counter) + " " + new_line + "\n")
            line_counter += 1

main()
