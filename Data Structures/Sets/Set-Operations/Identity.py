# As we know that Identify operator is used to find whether two sets equal or not. If they  are identical it return Ture else or False

hyd_tr_set = {12437,12723}
ban_tr_set = {12493,12647}
print(hyd_tr_set is ban_tr_set)
print({12493,12647} is ban_tr_set)
hyd_tr_set = {12493,12647}
print(hyd_tr_set is ban_tr_set)   # false

# Note: Always returns false because set is an unordered format of elements

# the following example to copy another object and check "is" operator it return true?
hyd_tr_set = {12437,12723}
ban_tr_set = hyd_tr_set
print(hyd_tr_set is ban_tr_set)   # true
print(hyd_tr_set is not ban_tr_set)  # false
