#%% Import bin_digit.py and bin_digit_nodes.py
#!/usr/bin/python3
import bin_digit
import bin_digit_nodes

#%% Parse word 10001
bin_str = "1001"
tree = bin_digit.parse(bin_str, types=bin_digit_nodes)

#%% Print root childs
print("String:", bin_str)
for node in tree.elements:
    print("Offset=", node.offset, "Text=", node.text)

#%% Print childs of the right children of root
for node in tree.elements[1].elements:
    print("Offset=", node.offset, "Text=", node.text)

#%% Calculate attributes
tree.compute()
print("String:", bin_str)
print("val attribute:", tree.val)
print("ord attribute:", tree.ord)

# %%
