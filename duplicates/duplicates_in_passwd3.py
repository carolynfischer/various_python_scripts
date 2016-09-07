def main():
    filename = "/home/carry/passwd_duplicate"
    open_file(filename)

def open_file(filename):
    with open(filename) as file:
        all_values = {}

        for line in file:
            if line.strip() == "":
                continue

            split = line.split(":")
            # if already found, just add new values, otherwise create a list
            if split[2] in all_values.keys():
                all_values[split[2]].append(split[0])
            else:
                all_values[split[2]] = []
                all_values[split[2]].append(split[0])

        for k, v in all_values.iteritems():
            if len(all_values[k]) > 1:
                users = ", ".join(all_values[k])
                print "Found duplicate ID {} with usernames {}".format(k, users)

    file.close()

if __name__ == "__main__":
    main()