class CRUD:
    def __init__(self):
        self.records = []
    
    def create(self,data):
        record = data
        self.records.append(record)
    
    def read(self):
        return self.records
 
    def update(self,index,data):
        self.records[index] = data
 
    def delete(self,index):
        self.records.pop(index)