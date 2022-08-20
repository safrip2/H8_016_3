number = {1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five"}
user = int(input("masukkan angka: "))
print(number.get(user, "tidak ada"))
# print(number[user])