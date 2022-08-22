
tr_num_set = {12235,12301,12302,12305,12305}
print(12301 in tr_num_set)  # true
print(12236 in tr_num_set)   # false

print(12304 not in tr_num_set)  # true


# the following example to check two set
tr_num_set = {12235,12301,12302,12305,12305}
print({12304} in tr_num_set)   # false
print({12235} in tr_num_set)  # false

# Note: checking two sets always return false because set is unordered


# the following example checking the multiple variables to check set operator.
tr_num_set = {12235,12301,12723,12737,12305}
hyd_dl_tr = {12437,12723,12721}
print(hyd_dl_tr in tr_num_set)
print((12723,12721) in tr_num_set)  # false
print((12723,12437) in tr_num_set)  # false
print({12723,12437} in tr_num_set)  # false
print({12723,12437} not in tr_num_set)   # true

# Note: multiple variables comparison returns always False becaues set is an unordered format ( index and slice) can not check.









