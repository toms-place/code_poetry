def fromFile(filepath):
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