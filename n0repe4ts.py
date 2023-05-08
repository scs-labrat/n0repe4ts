import os
import glob
import time
import colorama

def banner():
    colorama.init()

    print(colorama.Fore.RED + " ")
    print("\n \n")
    print("          .d8888b.                                        d8888  888             ")
    print("         d88P  Y88b                                      d8P888  888             ")
    print("         888    888                                     d8P 888  888             ")
    print("88888b.  888    888 888d888 .d88b.  88888b.   .d88b.   d8P  888  888888 .d8888b  ")
    print("888  88b 888    888 888P`  d8P  Y8b 888 `88b d8P  Y8b d88   888  888    88K      ")
    print("888  888 888    888 888    88888888 888  888 88888888 8888888888 888    `Y8888b. ")
    print("888  888 Y88b  d88P 888    Y8b.     888 d88P Y8b.           888  Y88b.       X88 ")
    print("888  888  `Y8888P``  888     `Y8888  88888P`  `Y8888        888   `Y888  88888P' ")
    print("                                    888                                          ")
    print("                                    888                                          ")
    print("                                    888                                          ")
    print(" " + colorama.Style.RESET_ALL)

    print("                                              Password List Optimiser - D8RH8R \n")
    print(colorama.Fore.RED +"[+] This process is destructive and will alter your original files.." + colorama.Style.RESET_ALL)
    input(colorama.Fore.BLUE +"[+] Press ENTER to continue...." + colorama.Style.RESET_ALL)


def read_passwords(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        passwords = set(file.read().splitlines())
    return passwords

def write_passwords(file_path, passwords):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("\n".join(passwords))

def main():
    root_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root_directory)
    txt_files = glob.glob("*.txt")

    # Sort files by size
    txt_files.sort(key=lambda f: os.path.getsize(f))

    for i in range(len(txt_files)):
        # Remove entries from smaller files in progressively larger files
        smaller_file = txt_files[i]
        smaller_passwords = read_passwords(smaller_file)
        for j in range(i + 1, len(txt_files)):
            larger_file = txt_files[j]
            larger_passwords = read_passwords(larger_file)
            larger_passwords -= smaller_passwords  # Remove entries from the smaller file
            write_passwords(larger_file, larger_passwords)

def rename_text_files_by_size():
    # get the root directory of the program
    dir_path = os.path.dirname(os.path.abspath(__file__))
    # get a list of text files in the directory
    file_list = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and f.endswith('.txt')]
    # sort the text files by size (ascending order)
    sorted_files = sorted(file_list, key=lambda f: os.path.getsize(os.path.join(dir_path, f)))
    # rename each text file with a number starting at 1
    for i, filename in enumerate(sorted_files, 1):
        # append the number to the start of the file name
        new_filename = os.path.join(dir_path, str(i) + '_' + filename)
        os.rename(os.path.join(dir_path, filename), new_filename)
        print(f"Renamed file {filename} to {os.path.basename(new_filename)}")


if __name__ == "__main__":
    banner()
    start_time = time.time()
    main()
    rename_text_files_by_size()
    end_time = time.time()
    total_time = end_time - start_time
    print(f"\nTotal elapsed time: {total_time:.2f} seconds")
    print(colorama.Fore.RED + "Done" + colorama.Style.RESET_ALL )