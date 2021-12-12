input_filename = "input.txt"
import pprint

currentPath = []
paths = []
numVisits = {}

def part1_traverse(graph, s, e):
    global currentPath, paths
    currentPath.append(s)

    if s == e:
        paths.append(list(currentPath))
    else:
        for neighbor in graph[s]:
            if neighbor.islower() and neighbor not in currentPath:
                part1_traverse(graph, neighbor, e)
            elif neighbor.isupper():
                part1_traverse(graph, neighbor, e)

    currentPath.pop()
    return

def small_node_twice(numVisits):
    # Return true if there is at least one small node that has been visited twice
    # Otherwise, return false
    ans = False
    for node,numVisits in numVisits.items():
        if node.islower() and numVisits == 2:
            ans = True
    return ans

def part2_traverse(graph, s, e):
    # s = starting node, e = ending node
    global currentPath, paths, numVisits
    currentPath.append(s)
    numVisits[s] += 1

    if s == e:
        paths.append(list(currentPath))
    else:
        for neighbor in graph[s]:
            if neighbor in ('start', 'end'):
                if neighbor not in currentPath:
                    part2_traverse(graph, neighbor, e)
            elif neighbor.islower():
                if neighbor in currentPath:
                    if small_node_twice(numVisits) is False:
                        part2_traverse(graph, neighbor, e)
                elif neighbor not in currentPath:
                    part2_traverse(graph, neighbor, e)
            elif neighbor.isupper():
                part2_traverse(graph, neighbor, e)

    currentPath.pop()
    numVisits[s] -= 1
    return

def part1(graph):
    global currentPath, paths
    currentPath, paths = [], []
    part1_traverse(graph, 'start', 'end')
    print('Ans: {0} paths through this cave system'.format(len(paths)))

def part2(graph):
    global currentPath, paths, numVisits
    currentPath, paths = [], []

    # Create a dictionary to keep track of how often we've visited each node
    for node in graph.keys():
        numVisits[node] = 0

    part2_traverse(graph, 'start', 'end')
    print('Ans: {0} paths through this cave system'.format(len(paths)))

def main():
    graph = load_input_file()
    
    print("\n---Part 1---")
    part1(graph)
    
    print("\n---Part 2---")
    part2(graph)
  
def load_input_file():
    cavemap = []
    
    with open(input_filename) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            start, end = line.split('-')
            cavemap.append([start, end])

    # Create the graph as an adjacency list
    graph = {}
    for c in cavemap:
        start_node, end_node = c
        if start_node not in graph:
            graph[start_node] = set()
        if end_node not in graph:
            graph[end_node] = set()

        graph[start_node].add(end_node)
        graph[end_node].add(start_node)
    
    return graph

if __name__=="__main__":
    main()