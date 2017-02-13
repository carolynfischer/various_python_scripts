def write_to_file():
    for i in range(5):
        with open("temp", "w") as f:
            f.write("This is iteration {}\n".format(i))

    # checking the file contents
    with open("temp", "r") as f:
        print f.read()

if __name__ == "__main__":
    write_to_file()