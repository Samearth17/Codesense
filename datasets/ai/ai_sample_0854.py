class MergeTwoLists():
    def merge(self, left_list, right_list):
        """Merge two sorted lists"""
        i = 0
        j = 0
        merged_list = []
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                merged_list.append(left_list[i])
                i += 1
            else:
                merged_list.append(right_list[j])
                j += 1

        merged_list += left_list[i:]
        merged_list += right_list[j:]
        return merged_list