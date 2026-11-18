
import os

# Get the current project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create notes folder path
NOTES_DIR = os.path.join(BASE_DIR, "notes")   #d:\notes
# Create notes folder if it does not exist
if not os.path.exists(NOTES_DIR):
    os.mkdir(NOTES_DIR)


# Function to get file path
def get_file_path():
    filename = input("Enter filename (e.g. diary.txt): ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    return os.path.join(NOTES_DIR, filename) #d:\notes\abc.txt

# Function to accept multiple lines
def get_content():
    print("\nEnter your content (Type END to finish):")

    lines = []

    while True:
        line = input()

        if line == "END":
            break

        lines.append(line)

    return "\n".join(lines)


# Task 1: Create New File
def create_file():

    filepath = get_file_path()

    try:
        with open(filepath, "x") as file:
            print("File created successfully!")

    except FileExistsError:
        print("Error: File already exists!")

    except OSError as e:
        print("File creation error:", e)


# Task 2: Write Content into File
def write_file():

    filepath = get_file_path()

    try:
        content = get_content()

        with open(filepath, "w") as file:
            file.write(content)

        print("Content saved successfully!")

    except OSError as e:
        print("Error:", e)


# Task 3: Read File
def read_file():

    filepath = get_file_path()

    try:
        with open(filepath, "r") as file:
            content = file.read()

        print("\n========== FILE CONTENT ==========")
        print(content)
        print("=================================")

    except FileNotFoundError:
        print("Error: File does not exist!")

    except OSError as e:
        print("Error:", e)


# Task 4: Append Content
def append_file():

    filepath = get_file_path()

    try:
        content = get_content()

        with open(filepath, "a") as file:
            file.write("\n" + content)

        print("Content appended successfully!")

    except OSError as e:
        print("Error:", e)


# Task 5: Search Text in File
def search_file():

    filepath = get_file_path()
    try:
        search_text = input("Enter word or phrase to search: ")
        if search_text == "":
            print("Search text cannot be empty!")
            return
        with open(filepath, "r") as file:
            lines = file.readlines()

        found = False

        for i, line in enumerate(lines, start=1):
            if search_text.lower() in line.lower():
                print(f"Found at line number: {i}")
                print("Line:", line.strip())
                found = True

        if not found:
            print("Text not found in the file!")

    except FileNotFoundError:
        print("Error: File does not exist!")
    except OSError as e:
        print("Error:", e)


# Task 6: Count Words and Characters
def count_file_data():

    filepath = get_file_path()

    try:
        with open(filepath, "r") as file:
            content = file.read()

        total_lines = len(content.splitlines())
        total_words = len(content.split())
        total_characters = len(content)
        total_spaces = content.count(" ")

        print("\n========== FILE STATISTICS ==========")
        print("Total Lines      :", total_lines)
        print("Total Words      :", total_words)
        print("Total Characters :", total_characters)
        print("Total Spaces     :", total_spaces)
        print("=====================================")

    except FileNotFoundError:
        print("Error: File does not exist!")

    except OSError as e:
        print("Error:", e)


# Task 7: Replace Text
def replace_text():

    filepath = get_file_path()

    try:
        with open(filepath, "r") as file:
            content = file.read()

        old_text = input("Enter text to replace: ")

        if old_text == "":
            print("Search text cannot be empty!")
            return

        new_text = input("Enter replacement text: ")

        if old_text not in content:
            print("Text not found in the file!")
            return

        updated_content = content.replace(old_text, new_text)

        with open(filepath, "w") as file:
            file.write(updated_content)

        print("Text replaced successfully!")

    except FileNotFoundError:
        print("Error: File does not exist!")

    except OSError as e:
        print("Error:", e)


# Task 8: Delete File
def delete_file():

    filepath = get_file_path()

    try:
        if not os.path.exists(filepath):
            print("Error: File does not exist!")
            return

        confirm = input("Are you sure you want to delete this file? (Y/N): ")

        if confirm.lower() == "y":
            os.remove(filepath)
            print("File deleted successfully!")

        else:
            print("File deletion cancelled!")

    except OSError as e:
        print("Error:", e)


# Task 9: Display All Files
def display_files():

    print("\n========== AVAILABLE TEXT FILES ==========")

    files = os.listdir(NOTES_DIR)

    txt_files = [
        filename for filename in files
        if filename.lower().endswith(".txt")
        and os.path.isfile(os.path.join(NOTES_DIR, filename))
    ]

    if len(txt_files) == 0:
        print("No text files available!")

    else:
        for i, filename in enumerate(txt_files, start=1):
            print(f"{i}. {filename}")

    print("==========================================")


# Task 10: Rename File
def rename_file():

    old_path = get_file_path()

    try:
        if not os.path.exists(old_path):
            print("Error: File does not exist!")
            return

        new_name = input("Enter new filename: ")

        if not new_name.endswith(".txt"):
            new_name += ".txt"

        new_path = os.path.join(NOTES_DIR, new_name)

        if os.path.exists(new_path):
            print("Error: A file with this name already exists!")
            return

        os.rename(old_path, new_path)

        print("File renamed successfully!")

    except OSError as e:
        print("Error:", e)


# Main Menu
def main():

    while True:

        print("\n========================================")
        print("          MY CONSOLE NOTEPAD")
        print("========================================")
        print("1. Create New File")
        print("2. Write Content into File")
        print("3. Read File")
        print("4. Append Content")
        print("5. Search Text in File")
        print("6. Replace Text in File")
        print("7. Count Words and Characters")
        print("8. Delete File")
        print("9. Display All Files")
        print("10. Rename File")
        print("11. Exit")
        print("========================================")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                create_file()

            elif choice == 2:
                write_file()

            elif choice == 3:
                read_file()

            elif choice == 4:
                append_file()

            elif choice == 5:
                search_file()

            elif choice == 6:
                replace_text()

            elif choice == 7:
                count_file_data()

            elif choice == 8:
                delete_file()

            elif choice == 9:
                display_files()

            elif choice == 10:
                rename_file()

            elif choice == 11:
                print("Thank you for using My Console Notepad!")
                break

            else:
                print("Invalid choice! Please enter 1 to 11.")

        except ValueError:
            print("Please enter a valid numeric choice!")


# Program execution starts here
if __name__ == "__main__":
    main()
