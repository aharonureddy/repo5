# example customer order table, there is online and offline users stored into another list
tab_order=[
    [101,'Rice',1500,'offline','12/12/2018',1],
    [102,'Oil',1200,'online','10/3/2018',2],
    [103,'Fruits',900,'offline','15/8/2018',1],
    [104,'Cloths',2100,'online','30/12/2018',3],
    [105,'Samsung TV',1800,'offline','16/12/2018',1],
    [106,'Cosmotic',1400,'online','5/9/2018',2],
    [107,'Sofa',2000,'online','12/10/2018',1],
    [108,'Fruits',900,'offline','19/11/2018',3],
    [109,'Rice',1500,'online','12/12/2018',2],
]
online_list = []     # create empty list for storing online users
offline_list = []    # create empty list for storing offline users
for i in range(len(tab_order)):
    empty_list = []    # storing for sublist elements
    if tab_order[i][3] == 'offline':
        for j in range(len(tab_order[i])):
            '''append data offline user sublist'''
            empty_list.append(tab_order[i][j])
        offline_list.append(empty_list)  # append one sublist
    else:
        for j in range(len(tab_order[i])):
            '''append data online user sublist'''
            empty_list.append(tab_order[i][j])
        online_list.append(empty_list)    # append one sublist
print("order_id     pro_name    proprice   pay_mode   pur_date  cut_id")
print("--------     ---------   ---------  ---------   -------  -------")
for i in range(len(online_list)):
    print(online_list[i])

print("order_id     pro_name    proprice   pay_mode   pur_date  cut_id")
print("--------     ---------   ---------  ---------   -------  -------")
for i in range(len(offline_list)):
    print(offline_list[i])
