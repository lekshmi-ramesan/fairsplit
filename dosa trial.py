total_bill =0
store = {}
for i in range(5):
    name = input("enter your name: ")
    num = int(input("how many dosa did u eat?"))
    bill_each = 60*num
    print(f"{name} owes {bill_each} rupees")   
    store[name] = bill_each
    total_bill += bill_each
print(total_bill)
most = max(store, key = store.get)
print(most,store[most])