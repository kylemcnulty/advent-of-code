import pprint
input_filename = "input.txt"

def count_overlapped_points(vmap):
    # Count number of points where at least two lines overlap (e.g. val > 2)
    cnt = 0
    for key,val in vmap.items():
        if val >= 2:
            cnt += 1
    return cnt

def part1(lines):
    vmap = {}

    # Read throught the lines and build the vent map (vmap)
    for line in lines:
        x1, y1 = line[0][0], line[0][1]
        x2, y2 = line[1][0], line[1][1]

        if (x1 == x2): 
            # Vertical line
            incr = 1
            if y2 < y1: incr = -1
            
            for y in range(y1, y2+incr, incr):
                point = (x1, y)
                if point in vmap:
                    vmap[point] += 1
                else:
                    vmap[point] = 1
        elif (y1 == y2):
            # Horizontal line
            incr = 1
            if x2 < x1: incr = -1

            for x in range(x1, x2+incr, incr):
                point = (x, y1)
                if point in vmap:
                    vmap[point] += 1
                else:
                    vmap[point] = 1
        else:
            # Not a horizontal or vertical line. So ignore for part one
            pass
 
    # Count number of points where at least two lines overlap (e.g. val > 2)
    cnt = count_overlapped_points(vmap)
    print('Ans: {0} points have overlapping vents'.format(cnt))

def part2(lines):
    vmap = {}

    # Read throught the lines and build the vent map (vmap)
    for line in lines:
        x1, y1 = line[0][0], line[0][1]
        x2, y2 = line[1][0], line[1][1]

        if (x1 == x2): 
            # Vertical line
            incr = 1
            if y2 < y1: incr = -1
            
            for y in range(y1, y2+incr, incr):
                point = (x1, y)
                if point in vmap:
                    vmap[point] += 1
                else:
                    vmap[point] = 1
        elif (y1 == y2):
            # Horizontal line
            incr = 1
            if x2 < x1: incr = -1

            for x in range(x1, x2+incr, incr):
                point = (x, y1)
                if point in vmap:
                    vmap[point] += 1
                else:
                    vmap[point] = 1
        else:
            # Don't ignore diagonal lines
            x_incr = 1
            if x2 < x1: x_incr = -1
            y_incr = 1
            if y2 < y1: y_incr = -1
            
            x_vals = range(x1, x2 + x_incr, x_incr)
            y_vals = range(y1, y2 + y_incr, y_incr)
            num_points = len(x_vals)

            i = 0
            while i < num_points:
                point = (x_vals[i], y_vals[i])
                if point in vmap:
                    vmap[point] += 1
                else:
                    vmap[point] = 1
                i += 1

    # Count number of points where at least two lines overlap (e.g. val > 2)
    cnt = count_overlapped_points(vmap)
    print('Ans: {0} points have overlapping vents'.format(cnt))

def main():
    lines = load_input_file()
    
    print("\n---Part 1---")
    part1(lines)
    
    print("\n---Part 2---")
    part2(lines)
  
def load_input_file():
    lines = []
    
    with open(input_filename) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            else:
                line = line.split(' -> ')
                line_clean = []
                for point in line:
                    point = point.split(',')
                    point = ( int(point[0]), int(point[1]) )
                    line_clean.append(point)
                
                lines.append(line_clean)

    return lines

if __name__=="__main__":
    main()