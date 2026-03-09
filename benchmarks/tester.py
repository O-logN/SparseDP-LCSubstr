import gc
import os
import time
import random

from suffix_tree import Tree
from suffix_tree.mccreight import Builder as McCreightBuilder
from sparse_dp_k import sparse_dp_k
from collections import Counter
from math import log, ceil


def generate_string(length):
    alphabet = ['A', 'C', 'G', 'T']
    res_list = random.choices(alphabet, weights=[0.1, 0.65, 0.2, 0.05], k=length) # a not too favorable distribution
    return ''.join(res_list)

def len_lcs_suffix_tree(x, y):
    tree = Tree({'A':x, 'B':y}, builder=McCreightBuilder)
    return tree.common_substrings()[0][1]

def len_lcs_sparse_dp_k(x, y):
    # an appropriate choice of k
    n = len(x)
    m = len(y)
    symb_counts = Counter(x)
    symb_counts.update(y)
    phi_d = sum((v/(n+m))**2 for v in symb_counts.values())
    k = ceil(log((n+m)/(n*m))/log(phi_d))
    return len(sparse_dp_k(x, y, k))

if __name__ == "__main__":
    # generate lengths
    lengths = []
    start = 5*10**3
    end = 3*10**5
    mul = 1.5
    while start <= end:
        lengths.append(start)
        start = round(start*mul)
    # run tests
    reps = 5
    tree_times = []
    sparse_dp_k_times = []
    print(f'lengths: {lengths}')
    print(f'repetitions per length (gets average): {reps}')
    print(':'*15)
    for l in lengths:
        print(f'cur_len: {l}')
        tree_tmp = []
        sparse_dp_k_tmp = []
        for _ in range(reps):
            # generate strings
            x = generate_string(l)
            y = generate_string(l)
            # run suffix tree
            gc.collect() 
            tm = time.perf_counter()
            ans_tree = len_lcs_suffix_tree(x, y)
            tree_tmp.append(time.perf_counter() - tm)
            # run sparse_dp_k
            gc.collect()
            tm = time.perf_counter()
            ans_sparse_dp_k = len_lcs_sparse_dp_k(x, y)
            sparse_dp_k_tmp.append(time.perf_counter() - tm)
            # check
            if ans_tree != ans_sparse_dp_k:
                print("Who is to blame?")
                raise Exception("Informative Exception Message")
        tree_times.append(sum(tree_tmp)/reps)
        sparse_dp_k_times.append(sum(sparse_dp_k_tmp)/reps)
    # save data
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "benchmarks_suffix_tree_vs_sparse_dp_k.txt")
    with open(file_path,mode='w',encoding="utf-8") as file:
        for a, b, c in zip(lengths, tree_times, sparse_dp_k_times):
            file.write(f"{a} {b} {c}\n")



