"""
Parse and continuously monitor a log file for errors 
"""
import time 

def parse_log(logfile, outfile):
    with open(logfile) as f:
        with open(outfile, 'w') as o:
            while True:
                where = f.tell()
                line = f.readline()
                if not line:
                    time.sleep(1)
                    f.seek(where)
                else:
                    line = line.split(" ")
                    o.write(line[5] + " " +  " ".join(line[6:]))


if __name__ == "__main__":
    parse_log("/home/carry/Desktop/messages", "/home/carry/Desktop/out")