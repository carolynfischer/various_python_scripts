"""
Find duplicate IDs in /etc/passwd
"""

def find_duplicates(file):
    try:
        users = []
        duplicate = False
        with open(file, 'r') as f:
            lines = f.read().splitlines()
            users = [x.split(":") for x in lines]

        print lines
        uids = []
        for i in users:
            if i[2] not in uids:
                uids.append(i[2])
            else:
                print "There was a duplicate uid {} for user {}".format(i[2], i[0])
                duplicate = True
        if not duplicate:
            print "There were no duplicate users"

    except IOError as e:
        print "Could not open file", file

if __name__ == "__main__":
    find_duplicates("/home/carry/Documents/python/passwd")
    find_duplicates("/etc/passwd")