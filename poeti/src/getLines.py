import csv
import yaml

#returns an array of lines with 
def fromTXT(filepath):
        para = []

        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                para.append(line.strip())
                line = fp.readline()
                cnt += 1

        lines = []
        for line in para:
            if line != "":
                words = line.split(" ")
                lines.append(words)
            else:
                lines.append("ABSATZ")

        return(lines)

def fromCSV(filepath):
    lines = []
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            lines.append(row)
    return lines

def fromYAML(filepath):
    lines = []
    with open(filepath, 'r') as stream:
        try:
            data = yaml.load(stream, Loader=yaml.FullLoader)
            for word in data:
                lines.append(word)
        except yaml.YAMLError as exc:
            print(exc)
    return lines