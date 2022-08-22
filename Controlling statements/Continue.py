# this example, it uses continue to skip odd numbers
x = 10
while x:
    x= x-1
    if x % 2 != 0:    # print only even numbers
        continue      #odd?  ok then -- skip print and continue loop
    print(x, end=' ')