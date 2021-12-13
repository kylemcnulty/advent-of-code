import numpy as np
input_filename = 'input.txt'

def print_sheet(sheet):
    sheet_print = sheet.tolist()
    for row in sheet_print:
        row = list(map(int, row))
        row = list(map(str, row))
        s = ''.join(row)
        print(s)
    print()

def part12(sheet, inst):
    part1_ans = None
    
    for i,fold in enumerate(inst):
        axis, point = fold

        if axis == 'x':
            base = sheet[:,0:point]
            fold = sheet[:,point+1:]
            folded = np.fliplr(fold)
            diff = base.shape[1] - folded.shape[1]
            if diff > 0:
                filler = np.zeros((folded.shape[0],diff))
                folded = np.hstack([filler, folded])
        elif axis == 'y':
            base = sheet[0:point,:]
            fold = sheet[point+1:,:]
            folded = np.flipud(fold)
            diff = base.shape[0] - folded.shape[0]
            if diff > 0:
                filler = np.zeros((diff, folded.shape[1]))
                folded = np.vstack([filler, folded])

        new_sheet = base+folded
        new_sheet[new_sheet > 1] = 1
        num_dots = np.count_nonzero(new_sheet==1)
        sheet = new_sheet

        if i == 0:
            part1_ans = num_dots

    print('\nPart 1: {0}'.format(part1_ans))
    
    print('\nPart 2:')
    print_sheet(sheet)

def main():
    sheet, inst = load_input_file()
    
    print("\n---Part 1 and 2---")
    part12(sheet, inst)
  
def load_input_file():
    sheet = None
    dots_x = []
    dots_y = []
    inst = [] 
    
    with open(input_filename) as f:
        lines = f.readlines()   
        for line in lines:
            line = line.strip()
            if not line:
                continue
            elif line.startswith('fold'):
                i = line.replace('fold along ', '')
                axis,point = i.split('=')
                inst.append([axis, int(point)])
            else:
                dot_x, dot_y = tuple(map(int, line.split(',')))
                dots_x.append(dot_x)
                dots_y.append(dot_y)

    # Create numpy matrix
    x_dim = max(dots_x) + 1
    y_dim = max(dots_y) + 1
    sheet = np.zeros([y_dim, x_dim])
    sheet[dots_y,dots_x] = 1
    
    return sheet, inst

if __name__=="__main__":
    main()