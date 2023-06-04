
def main():
    filepath = "/Users/tiffanylee/Downloads/Personal Projects/Advent_of_Code/2022/InputFiles_2022/Day06_Input.txt"
    info = open(filepath).read()
    part1 = False
    part2 = False
    for i in range(len(info)):
        if not part1 and len(set([info[i-j] for j in range(4)])) == 4:
            print("Part One: How many characters need to be processed "
                  + "before the first start-of-packet marker is detected? "
                  + "(4 distinct characters)"
                  + "\nANSWER: " + str(i+1))
            part1 = True
        if not part2 and len(set([info[i-j] for j in range(14)])) == 14:
            print("\nPart Two: How many characters need to be processed before "
                  + "the first start-of-message marker is detected?"
                  + "(14 distinct characters)"
                  + "\nANSWER: " + str(i+1))
            part2 = True
main()