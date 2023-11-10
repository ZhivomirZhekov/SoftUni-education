file_path = input().split("\\")
file_extension = file_path[-1]
file , extension = file_extension.split(".")
print(f"File name: {file}")
print(f"File extension: {extension}")
