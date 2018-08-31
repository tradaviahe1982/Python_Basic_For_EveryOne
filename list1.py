l1 = [1951, 1952, 1953]
l2 = ["Hello", "Nguyễn Việt Anh", "Trần Đình Chiến"]
print(l1)
print(l2)
l1.append(1958)
print(l1)
item = 1952
if item in l1:
    print(l1.index(item))
else:
    print(-1)