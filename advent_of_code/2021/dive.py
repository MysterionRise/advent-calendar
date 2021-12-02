if __name__ == '__main__':
    aim = 0
    forward = 0
    depth = 0
    with open('dive.txt') as f:
        lines = f.readlines()
        x = int(line.split()[1])
        for line in lines:
            if line.startswith("forward"):
                forward += x
                depth += aim * x
            elif line.startswith("up"):
                aim -= x
            elif line.startswith("down"):
                aim += x
    print(depth * forward)
