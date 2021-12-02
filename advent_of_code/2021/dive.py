if __name__ == '__main__':
    aim = 0
    forward = 0
    depth = 0
    with open('dive.txt') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("forward"):
                forward += int(line.split()[1])
                depth += aim * int(line.split()[1])
            elif line.startswith("up"):
                aim -= int(line.split()[1])
            elif line.startswith("down"):
                aim += int(line.split()[1])
    print(depth * forward)