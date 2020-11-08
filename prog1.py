samochody = ["syrena", "polonez"]

print(samochody[0])
print(samochody[1])

for s in samochody:
    print(s)

for idx in range(len(samochody)):
    print(samochody[idx])

print("len: {0}".format(len(samochody)))
print("range: {0}".format(range(2)))

for idx in range(len(samochody)):
    print("{0} {1}".format(idx, samochody[idx]))

print(','.join(samochody))
arr = "a;b;c;d;e"
arr_l = arr.split(';')
print(f"lista - arr_l: {arr_l}")

samochody = ["syrena", "polonez"]
ilosc = [3, 5]

for idx in range(len(samochody)):
    print("idx: " + str(idx) + ": " + samochody[idx])
    print(samochody[idx] + " ma ilosc drzwi " + str(ilosc[idx]))
