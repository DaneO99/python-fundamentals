import time

# def net_price(list_price, discount = 0 , tax = .0825):
#     return list_price * (1 - discount) * (1 + tax)

# # no additional arguments
# # print(net_price(500))

# # one additional argument
# # print(net_price(500,.10))

# # 2 additional arguments
# # print(net_price(500,.1,0))

def count(end, start = 0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(10)
