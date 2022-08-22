# tuple within creation is called a nested tuple
# the following example to access an elements nested tuple
cust_data = (('Joe','2/22/2022','Cosmotic', 2000),
                ('John','7/3/2022','rice',1200),
                ('Aharonu','7/3/2022','oil',1000),
                ('Sridhar','1/12/2022','Fruits',500)
                )
print("cust_name",    "pur_date",  "prod_name",   "price")
print("--------",      "---------", "----------",  "-------")
for i in range(len(cust_data)):
    for j in range(len(cust_data[i])):
        print(cust_data[i][j],end=" ")
    print(end="\n")
