class VersionControl:
    def __init__(self, lines):
        self.lines = lines
        self.mark = 0
 
    def commit(self):
        self.mark += 1
        log_file = open("log_file.txt", "a+")
        log_file.write(str(self.mark) + ": " + str(self.lines))
        log_file.close()
 
    def restore(self):
        log_file = open("log_file.txt", "r")
        lines = log_file.readlines()
        to_mark = self.mark-1
 
        self.lines = lines[to_mark]
        log_file.close()