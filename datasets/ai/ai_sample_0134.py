def hanoi(n, source, spare, target):
    if n == 1:
        disk = source.pop(0)
        print("Moving disk {0} from {1} to {2}".format(disk[0], disk[1], target[1]))
        target.insert(0, disk)
    else:
        hanoi(n-1, source, target, spare)
        disk = source.pop(0)
        print("Moving disk {0} from {1} to {2}".format(disk[0], disk[1], target[1]))
        target.insert(0, disk)
        hanoi(n-1, spare, source, target)

n = 8
source = [(i, "A") for i in range(1, n+1)]
target = []
spare = []

hanoi(n, source, spare, target)