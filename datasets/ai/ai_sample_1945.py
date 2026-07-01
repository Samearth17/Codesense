class MinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, item):
        self.heap_list.append(item)
        self.current_size += 1
        self.fix_new_item()

    def fix_new_item(self):
        idx = self.current_size
        while idx // 2 > 0:
            if self.heap_list[idx] < self.heap_list[idx // 2]:
                temp = self.heap_list[idx // 2]
                self.heap_list[idx // 2] = self.heap_list[idx]
                self.heap_list[idx] = temp
            idx = idx // 2