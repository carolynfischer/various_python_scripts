def main():
    filename = "/home/carry/passwd_duplicate"
    open_file(filename)

def open_file(filename):
    with open(filename) as file:
        all_values = {}
        duplicates = {}

        for line in file:
            if line.strip() == "":
                continue

            split = line.split(":")
            if split[2] not in all_values.keys():
                all_values[split[2]] = split[0]
            else:
                # if it is not in duplicate values yet, add it
                if split[2] not in duplicates.keys():
                    duplicates[split[2]] = []
                    duplicates[split[2]].append(all_values[split[2]])
                    duplicates[split[2]].append(split[0])
                else:
                    duplicates[split[2]].append(split[0])

        for key, values in duplicates.iteritems():
            for value in values:
                print "Found a duplicate ID {} that has username {}".format(key, value)

    file.close()

if __name__ == "__main__":
    main()