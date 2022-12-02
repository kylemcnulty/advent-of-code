input_filename = "input.txt"
import numpy as np
import pprint

def get_neighbors(_in, y, x, run, alg):
    ''' Returns indices of all neighboring elements'''
    y_max, x_max = _in.shape
    iy_max, ix_max = y_max-1, x_max-1
    neighbors = []
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for offset in offsets:
        iy, ix = y + offset[0], x + offset[1]
        if (iy < 0) or (iy > iy_max) or (ix < 0) or (ix > ix_max):
            if (run % 2 == 0):
                neighbors.append(str(alg[-1]))
            else:
                neighbors.append(str(alg[0]))
        else:
            neighbors.append(str(_in[iy, ix]))
    return neighbors

def print_sheet(sheet):
    sheet_print = sheet.tolist()
    for row in sheet_print:
        row = list(map(int, row))
        row = list(map(str, row))
        s = ''.join(row)
        print(s)
    print()

def part1(alg, _in, out):
    # Answer is somewhere between 5206 and 5592
    runs = 50
    iy_max, ix_max = out.shape[0]-1, out.shape[1]-1
    print_sheet(_in)
    
    for run in range(runs):
        for iy,ix in np.ndindex(out.shape):
            window = get_neighbors(_in, iy, ix, run, alg)
            window = ''.join(window)
            ind = int(window, 2)
            out_pixel = alg[ind]
            out[iy,ix] = out_pixel

        _in = out.copy()

        print('After {0} enhancement'.format(run+1))
        on_cnt = np.count_nonzero(out == 1)
        print(on_cnt)
        # print_sheet(out)

    print('Final')
    # out[:,0] = 0
    # out[:,ix_max] = 0
    print_sheet(out)
    on_cnt = np.count_nonzero(out == 1)
    print(on_cnt)

def main():
    alg, _in, out  = load_input_file()
    
    print("\n---Part 1---")
    part1(alg, _in, out)
    
    # print("\n---Part 2---")
    # part2(rhm, lows)
  
def load_input_file():
    alg_raw= None
    lines = []

    with open(input_filename) as f:
        alg_raw = list(f.readline().strip())
        for line in f.readlines():
            line = line.strip()
            if line != '':
                line = list(line)
                lines.append(line)

    # Convert the alg
    alg = np.array(alg_raw)
    alg[alg == '#'] = 1
    alg[alg == '.'] = 0
    alg = alg.astype(int)

    in_img_raw = np.array(lines)
    in_img_raw[in_img_raw == '#'] = 1
    in_img_raw[in_img_raw == '.'] = 0
    in_img_raw = in_img_raw.astype(int)
    # in_img = in_img_raw.copy()

    # Ring the input image in lots of dark pixels (zeros)
    ring = 50
    print("Ring size: {0}".format(ring))
    in_img = np.zeros(in_img_raw.shape + np.array(2*ring), in_img_raw.dtype)
    in_img[ring:-ring,ring:-ring] = in_img_raw

    # Make the output image
    out_img = np.zeros(in_img.shape, in_img.dtype)

    return alg, in_img, out_img

if __name__=="__main__":
    main()