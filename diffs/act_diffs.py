# Diffs between CFGs and PEGs



#%% Diff #1: Order in a1 / a2 / a3 matters!
import diffs_1

#%% Parsing word "aa" in PEG S <- "a" / "aa" will fail
tree = diffs_1.parse("aa")

# %% But parsing word "a" in PEG S <- "a" / "aa" will succeed 
tree = diffs_1.parse("a")
print(tree.text)
# But PEG <- "aa" / "a" will parse both "a" and "aa"!



# %% Diff #2: Concatenation is ordered!
import diffs_2

# %% "aaaa" cannot be parsed in PEG diffs_2_1 because A will take all 4 "a"s
tree = diffs_2.parse("aaaa")
# But if we will change order of A and B (diffs_2_2) "aaaa" will be parsed!
# Because first 2 "a"s will go into B and 2 last "a"s will go into A



# %% Diff #3: "!" operator checks that we don't have something
# B can produce any word, but (!A) ensures that this word
# do not start with a^n b^n
import diffs_3

# %% aab is parsing because it do not starts with a^n b^n
tree = diffs_3.parse("aab")
# Note that (!A) consumes no characters: left child of root is empty
for node in tree.elements:
    print("Offset=", node.offset, "Text=", node.text)

# %% "aabba" cannot be parsed as it starts with a^2 b^2
tree = diffs_3.parse("aabba")



# %% Diff #4: "&" operator checks that we have something
import diffs_4

# %% A produces a^m b^m, "a"+ produce at least one "a"
# B produces b^n c^n 
#  &(A 'c') ensures that we have "a^m b^m c" at the start of the word
# To sum up, PEG produces words like a+ b^n c^n that starts with a^m b^m c 
# It is a^n b^n c^n!
# aabbcc should be parsed:
tree = diffs_4.parse("aabbcc")
for node in tree.elements:
    print("Offset=", node.offset, "Text=", node.text)

# %% abcc is not parsed!
tree = diffs_4.parse("abcc")
# %%
