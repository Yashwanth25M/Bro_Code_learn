# (04:02:50) 

# default arguments
# default value for certain arguments

# def net_price(list_price , discount =0.99 , tax = 0.50):
#     return (list_price * ( 1 - discount ) * (1 + tax))
# print(net_price(500,0,0.5))#passing all arguement
# print(f"{net_price(500):.2f}")#passing a single arguement
# print(f"{net_price(500,0.1):.2f}")#passing only 2 arguements

# import time
# def count( end ,start=0):#dont pass default arguments first(throws a error)
#     for x in range (start , end+1):
#         print(x)
#         time.sleep(1)
#     print("Done")
# count(20)