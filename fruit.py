def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list.reverse()
    print(f"Reverse: {fruit_list}")
    fruit_list.append("orange")
    i= fruit_list.index("apple")
    fruit_list.insert(i-1, "cherry")
    print(fruit_list)
    fruit_list.remove("banana")
    fruit_list.pop()
    print(f"pop orange: {fruit_list}")
    fruit_list.sort()
    print(fruit_list)
    fruit_list.clear()
    print(fruit_list)

main()