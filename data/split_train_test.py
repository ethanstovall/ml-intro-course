import os
import sys
import numpy as np

def numlines(filename) :
  with open(filename) as fi:
    for cnt, line in enumerate(fi):
      n = cnt
      n += 1
  return n

def split_random_p_from_n(p, n) :
  permutation = np.random.permutation(n)
  k = int(p*n + 0.5)
  train_split = permutation[:k]
  test_split = permutation[k:]
  return train_split, test_split

def select_random_p(p, filename) :
  n = numlines(filename)
  permutation = np.random.permutation(n)
  k = int(p*n + 0.5)
  firstk = permutation[:k]
  return firstk

def select_from_file(f_in, f_out, split) :
    fo = open(f_out, "w");
    with open(f_in) as fi:
        for cnt, line in enumerate(fi):
            if(cnt in split or cnt == 0):
                fo.write(line)
    fo.close()

def train_out_name(in_name,p,seed) :
    s = str(seed) if seed >= 0 else ""
    r = str(int(p*100))
    basename = os.path.basename(in_name);
    name, extension = os.path.splitext(basename)
    return(name + "_train_" + s + "_" + r + extension)

def test_out_name(in_name,p,seed) :
    s = str(seed) if seed >= 0 else ""
    r = str(int(p*100))
    basename = os.path.basename(in_name);
    name, extension = os.path.splitext(basename)
    return(name + "_test_" + s + "_" + r + extension)

# insist on 3 arguments
if len(sys.argv) != 4:
  print(sys.argv[0], "takes 3 arguments. Not ", len(sys.argv)-1)
  print("Arguments: full_data_file fraction [seed]. Example:",
        sys.argv[0], "breast_cancer.csv 0.7 7")
  sys.exit()

full = sys.argv[1]
p = float(sys.argv[2])
seed = -1
if(len(sys.argv) == 4) :
    seed = int(sys.argv[3])
    np.random.seed(seed)

lines_full = numlines(full)
assert p < 1, "Train split must give a fraction less than 1."
train_split, test_split = split_random_p_from_n(p, lines_full)

train_out = train_out_name(full, p, seed)
test_out = test_out_name(full, 1 - p, seed)

select_from_file(full, train_out, train_split)
select_from_file(full, test_out, test_split)
