Check the preprint for a theoretical discussion on the i.i.d. model.\
\
Here is a *very* minimal benchmark (for what it is worth).\
I ran `/code/sparse_dp_k.py` with `k` such that `k in Theta(log(nm))`, and compared it against a suffix tree implementation\
(credits to https://github.com/cceh/suffix-tree). \
Check the files `/benchmarks/tester.py` and `/benchmarks/plotter.py` to run your own tests.\
\
Benchmarks on meaningful scenarios would be welcome, you can find my email in the github page (js enabled).

![suffix_tree_vs_sparse_dp_k](/benchmarks/pic.png)
