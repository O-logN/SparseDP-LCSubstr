import matplotlib.pyplot as plt

def plot_benchmark(file_path):
    lengths, time_tree, time_sdpk = [], [], []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            line = line.split(' ')
            length, t_tree, t_sdpk = int(line[0]), float(line[1]), float(line[2])
            lengths.append(length)
            time_tree.append(t_tree)
            time_sdpk.append(t_sdpk)
    
    plt.figure(figsize=(10, 6))
    plt.plot(lengths, time_tree, label='suffix tree', marker='o', color='#1f77b4', linewidth=2, markersize=4)
    plt.plot(lengths, time_sdpk, label='sparse_dp_k', marker='s', color='#ff7f0e', linewidth=2, markersize=4)

    plt.title('i.i.d. generated strings using (0.1, 0.65, 0.2, 0.05) as the distribution', fontsize=14, fontweight='bold')
    plt.xlabel('Length (|x|=|y|)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=11)
    
    plt.ticklabel_format(style='plain', axis='x')
    
    plt.tight_layout()
    plt.show()

plot_benchmark('benchmarks_suffix_tree_vs_sparse_dp_k.txt')
