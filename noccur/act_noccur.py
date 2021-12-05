#%% Import nocur.py and noccur_nodes.py
#!/usr/bin/python3
import noccur
import noccur_nodes

#%% Parse word aabaabb#aabba
str = "aabaabb#aabba"
tree = noccur.parse(str, types=noccur_nodes)

#%% Print root childs
print("String:", str)
for node in tree.elements:
    print("Offset=", node.offset, "Text=", node.text)

# %% Calculate attributes
tree.compute()
print("String:", str)
print("res attribute", tree.res)

# %% Print attributes of root childs
print("Nab in left part:", tree.elements[0].nab)
print("Nba in right part:", tree.elements[2].nba)

# %%
