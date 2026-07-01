class DataImportTask:

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    # Method to download the source file to the file system
    def download(self):
        # Implementation here

    # Method to read the content of the source file into a CSV format
    def read(self):
        # Implementation here

    # Method to format the content into the destination format
    def format(self):
        # Implementation here

    # Method to save the destination in the desired location
    def save(self):
        # Implementation here