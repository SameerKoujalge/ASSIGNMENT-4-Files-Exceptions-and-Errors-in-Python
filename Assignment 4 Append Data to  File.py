# Task 2: Write and Append Data to a File

file_name = "output.txt"

text = input("Enter text to write to the file: ")
with open(file_name, "w") as file:
    file.write(text + "\n")
print(f"Data successfully written to {file_name}.")

additional_text = input("Enter additional text to append: ")
with open(file_name, "a") as file:
    file.write(additional_text + "\n")
print("Data successfully appended.")

print(f"\nFinal content of {file_name}:")
with open(file_name, "r") as file:
    print(file.read())
