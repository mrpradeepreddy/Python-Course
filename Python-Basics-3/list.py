# Open the file in write mode
# with open("my_notes.txt", "w") as file:
#     # Ask for 3 lines from the user
#     for i in range(3):
#         line = input(f"Enter line {i + 1}: ")
#         file.write(line + "\n")  # Write each line followed by a newline
with open("my_notes.txt", "r") as file:
    print(file.read())