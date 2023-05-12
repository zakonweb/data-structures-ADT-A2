class Dictionary:
    def __init__(self):
        self.dict = {}

    def insert(self, key, value):
        self.dict[key] = value

    def delete(self, key):
        if key in self.dict:
            del self.dict[key]
        else:
            print("Key not found!")

    def search(self, key):
        return self.dict.get(key, "Key not found!")

    def display(self):
        for key, value in self.dict.items():
            print(f"{key} : {value}")


dictionary = Dictionary()

while True:
    print("\n1. Insert\n2. Delete\n3. Search\n4. Display\n5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        key = input("Enter key: ")
        value = input("Enter value: ")
        dictionary.insert(key, value)
    elif choice == 2:
        key = input("Enter key: ")
        dictionary.delete(key)
    elif choice == 3:
        key = input("Enter key: ")
        print(dictionary.search(key))
    elif choice == 4:
        dictionary.display()
    elif choice == 5:
        break
    else:
        print("Invalid choice!")
