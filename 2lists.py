l1 = [1, 2, 3, 4, 5]
l2 = ["apple", "mango", "kiwi", "x", "y"]

if len(l1) == len(l2):
    greatest = max(l1)
    indexGreatest = l1.index(greatest)
    print(f"{greatest}:{l2[indexGreatest]}")
