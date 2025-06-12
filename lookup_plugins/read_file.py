import sys

def read_file(file_path):
    with open (file_path, 'r') as file:
        return file.read()

if __name__ == "__main__":
    file_path = "/home/paroscale/myapp/hello.txt"
    content = read_file(file_path)
    print(content)