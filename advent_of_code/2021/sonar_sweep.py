if __name__ == '__main__':
    current = 0
    res = 0
    with open("sonar_sweep.txt") as f:
        lines = f.readlines()
        current = int(lines[0]) + int(lines[1]) + int(lines[2])
        for i in range(1, len(lines) - 2):
            sum = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
            if sum > current:
                res += 1
            current = sum
    print(res)
