class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
  

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''

    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        if self.data[index] is None:
            self.data[index] = Node(key, Contact(key, value))
        else:
            current = self.data[index]

            while current is not None:
                if current.key == key:
                    current.value.number = value
                    return

                if current.next is None:
                    break

                current = current.next

            current.next = Node(key, Contact(key, value))

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current is not None:
            if current.key == key:
                return current.value

            current = current.next

        return None

    def print_table(self):
        for index in range(self.size):
            print(f"Index {index}:", end = " ")

            current = self.data[index]

            if current is None:
                print("Empty")
            else:
                while current is not None:
                    print(f"- {current.value}", end=" ")
                    current = current.next

                print()
  

# Test your hash table implementation here.  
"""
contact_1 = Contact("Riley", "123-456-7890")
node_1 = Node(contact_1.name, contact_1)

print(node_1.key)
print(node_1.value)
print(node_1.next)
"""
table = HashTable(10)

table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")

table.print_table()

contact = table.search("John")
print("\nSearch result:", contact)

table.insert("Rebecca", "999-444-9999")
print(table.search("Rebecca"))

print(table.search("Chris"))

table.insert("Amy", "111-222-3333")
table.insert("May", "222-333-1111")

table.print_table()

"""
DESIGN MEMO
Why is a hash table the right structure for fast lookups?
A hash table lets the user find information quickly without having to seach trhough each item individually. A hash table uses a hash function to index a key, allowing the program to know where to look for the data. Naturally this makes searching a lot faster than going through a normal list.
How did you handle collisions?
Collisions were handled by using separate chaining with a linked list. If and when 2 contacts get assigned to the same index, the program makes a new node and connects it to the already existing one. This makes it so several contacts can be stored in the same index without a problem. I made sure that if a contact with the same name is added again, the contact's phone number is updated instead of making a duplicate which would clutter everything.
When might an engineer choose a hash table over a list or tree?
A hash table can be better than a list or a tree for a lot of things. Some examples include: contact lists (haha), online shopping, school databases, and inventory systems. A list would take longer to search because it could have to check every single item. A tree can be useful, but a hash table is probably better when you're trying to look up an item quickly. 
"""