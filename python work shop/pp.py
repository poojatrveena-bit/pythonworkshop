

data={"name":"pooja T R","age":100}
print(data)

data["age"]=25
print(data)

print(data.values())

print(data.keys())



products=["soap","shampoo","brush"]
print(products)
products.append("toothpaste")
print(products)
products.insert(1,"facewash")
print(products)
products.remove("brush")
print(products)
products.sort()
products.reverse()
print(products)

print("-------------")

products = (
    "Laptop",
    "Smartphone",
    "Headphones",
    "Keyboard",
    "Mouse",
    "Monitor",
    "USB Cable",
    "External Hard Drive",
    "Webcam",
    "Printer"
)


print(products)


print("First product:", products[0])


print("List of products:")
for product in products:
    print(f"- {product}")

