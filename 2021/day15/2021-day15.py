input_filename = "testinput.txt"
import numpy as np
from queue import PriorityQueue

def part1(rmap):

	start = (0,0)
	end = (rmap.shape[0], rmap.shape[1])

	q = PriorityQueue()



	while True:



   

def main():
    rmap = load_input_file()
    
    print("\n---Part 1---")
    part1(rmap)
    
def load_input_file():
    lines = []

    with open(input_filename) as f:
        for line in f.readlines():
        	line = list(line.strip())
        	line = list(map(int, line))
        	lines.append(line)

    rmap = np.array(lines)
    print(rmap)
    return rmap

if __name__=="__main__":
    main()