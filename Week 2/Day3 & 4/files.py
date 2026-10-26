import os

print("Python is looking in:")
print(os.getcwd())

print("\nFiles Python can see:")
print(os.listdir())

file = open("more_names.txt", "r")

content = file.read()

print("\nFile contents:")
print(content)

file.close()
