#%% Import nocur.py and noccur_nodes.py
#!/usr/bin/python3
import types
import itemize
import itemize_nodes

#%% Read input file and remove all line breaks
with open("itemize.tex") as f:
    input = f.read().replace("\n", "")

#%% Parse input
tree = itemize.parse(input, types=itemize_nodes)
with open("itemize.txt", "w") as f:
    f.write(tree.compute())

# %%
