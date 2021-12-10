input_filename = "input.txt"
import statistics as stats

PT1_POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
PT2_POINTS = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

def part1(lines):
    first_illegal_chars = []
    incomplete_lines = []

    for line in lines:
        stack = []
        line_corrupt = False
        
        for char in line:
            if char in ('(', '[', '{', '<'):
                stack.append(char)
            elif char in (')', ']', '}', '>'):
                last = stack.pop()
                merge = last + char
                
                if merge in ('()', '[]', '{}', '<>'):
                    continue
                else:
                    line_corrupt = True
                    first_illegal_chars.append(char)
                    break

        if line_corrupt == False:
            incomplete_lines.append(line)
    
    error_score = 0
    for char in first_illegal_chars:
        error_score += PT1_POINTS[char]
    
    print('Ans: {0}'.format(error_score))
    return incomplete_lines

def part2(incomplete_lines):
    incomplete_stacks = []
    
    for line in incomplete_lines:
        stack = []
        fix_stack = []
        for char in line:
            if char in ('(', '[', '{', '<'):
                stack.append(char)
            elif char in (')', ']', '}', '>'):
                char = stack.pop()
        incomplete_stacks.append(stack)   

    scores = []
    for s in incomplete_stacks:
        score = 0
        for i in range(len(s)):
            char = s.pop()
            score = (score * 5) + PT2_POINTS[char]

        scores.append(score)

    ans = stats.median(scores)
    print('Ans: {0}'.format(ans))

def main():
    lines = load_input_file()
    
    print("\n---Part 1---")
    incomplete_lines = part1(lines)
    
    print("\n---Part 2---")
    part2(incomplete_lines)
  
def load_input_file():
    lines = []    

    with open(input_filename) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            line = list(line)
            lines.append(line)

    return lines

if __name__=="__main__":
    main()