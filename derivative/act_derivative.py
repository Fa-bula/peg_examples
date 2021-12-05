#%% Import derivative.py and derivative_nodes.py
#!/usr/bin/python3
import derivative
import derivative_nodes

#%% Parse word f=2x^4+3x^3+1x^2
f = "2x^4+3x^3+1x^2"
tree = derivative.parse(f, types=derivative_nodes)

#%% Compute derivatives
print("f=", f)
dfdx = tree.compute()
print("f'=", dfdx)
tree_2 = derivative.parse(dfdx, types=derivative_nodes)
print("f''=", tree_2.compute())

# %% Known issue[1]: coeffs cannot be negative or fractional
# The following code will produce parse error
g = "-1x^3+2x^2"
tree = derivative.parse(g, types=derivative_nodes)


# %% Known issue[2]: coeffs cannot be omitted
# The following code will produce parse error
h = "x^3"
tree = derivative.parse(h, types=derivative_nodes)

# %% Known issue[3]: spaces cause errors
# The following code will produce parse error
l = "1x^3 + 2x^1"
tree = derivative.parse(l, types=derivative_nodes)

# %%
