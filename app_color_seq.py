import sys
import logging
logging.basicConfig(level=logging.DEBUG)


def main():
    # run_test("test_4")
    for test_file in sys.argv[1:]:
        run_test(test_file)


def run_test(test_file):
    logging.debug("Starting test: %s", test_file)
    global rows, cols, colors

    # read test data
    f = open("tests/" + test_file, "r")
    lines = f.readlines()
    f.close()

    # parse first line
    line1 = lines[0].split()
    rows = int(line1[0])
    cols = int(line1[1])
    logging.debug("Rows=%s, Colls=%s", rows, cols)

    # parse matrix
    colors = []
    for line in lines[1:rows+1]:
        colors.append(line.split())

    # for line in colors:
        # logging.debug(line)

    # init matrix of flags whether a cell is visited
    global visited
    visited = []
    for r in range(rows):
        line = []
        for c in range(cols):
            line.append(False)
        visited.append(line)

    # walk the matrix
    max_len = 0
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                seq_len = get_sequence_len(r, c)
                if max_len < seq_len:
                    max_len = seq_len
    print(max_len)


def get_sequence_len(r, c):
    global visited, rows, cols

    # accumulate here planned cells to visit
    to_visit = {(r, c)}
    seq_len = 0

    while len(to_visit) > 0:
        # visit a cell
        (r1, c1) = to_visit.pop()
        visited[r1][c1] = True        
        seq_len += 1

        # check the 4 neighbours
        offsets = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for (ro, co) in offsets:
            # neighbour cell
            r2 = r1 + ro
            c2 = c1 + co

            in_bounds = r2 >= 0 and r2 < rows and c2 >= 0 and c2 < cols
            if not in_bounds:
                continue

            if visited[r2][c2]:
                continue
            
            if colors[r2][c2] != colors[r1][c1]:
                continue

            # neighbour is need to add
            to_visit.add((r2, c2))
    return seq_len


main()
