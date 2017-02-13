"""
Parse and continuously monitor a log file for errors 
"""
import time 

def parse_log(logfile, outfile):
    with open(logfile, 'r') as f:
        with open(outfile, 'w') as o:
            while True:
                where = f.tell()
                line = f.readline()
                if not line:
                    time.sleep(1)
                    f.seek(where)
                else:
                    level_index = None
                    line = line.split(" ")
                    if "<error>" in line:
                        level_index = line.index("<error>")
                    elif "<info>" in line:
                        level_index = line.index("<info>")
                    elif "<warning>" in line:                        
                        level_index = line.index("<warning>")
                    if level_index is not None:
                        level = line[level_index].replace("<", "").replace(">", "")
                        message = " ".join(line[level_index+1:])
                        print level, message
                        o.write(level + " " +  message)


if __name__ == "__main__":
    parse_log("/home/carry/Desktop/messages", "/home/carry/Desktop/out")