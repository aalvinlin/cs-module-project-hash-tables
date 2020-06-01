class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.items_stored = 0
        self.storage = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.items_stored / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # 64-bit prime used for calculations
        FNV_PRIME = 1099511628211

        # 64-bit offset basis used for calculations
        OFFSET_BASIS = 14695981039346656037

        hash_index = OFFSET_BASIS

        bytes_to_process = key.encode()

        for byte in bytes_to_process:

            hash_index *= FNV_PRIME
            hash_index ^= byte

        return hash_index

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        
        # initialize hash_index as 5381
        # 5381 is only used for historical purposes
        hash_index = 5381

        bytes_to_process = key.encode()

        for byte in bytes_to_process:

            # 33 is only used for historical purposes
            hash_index *= 33
            hash_index += byte

        return hash_index

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # increment counter if not replacing an existing value
        hash_index = self.hash_index(key)

        # insert into an empty spot
        if not self.storage[hash_index]:
            self.storage[hash_index] = HashTableEntry(key, value)

        # collision detected: find end of linked list and add item there
        else:
            current_node = HashTableEntry

            while current_node.next:
                current_node = current_node.next

            current_node.next = HashTableEntry(key, value)
        
        self.items_stored += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        if self.storage[index]:
            self.storage[index] = None
            self.items_stored -= 1

        else:
            print("Key not found.")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        if self.storage[index]:
            current_node = self.storage[index]
            
            # move to the next node if the key doesn't match, and if there is a next node
            while current_node.key != key and current_node.next:
                current_node = current_node.next

            # end of list reached without finding a key
            if not current_node.next:
                return None
            
            # otherwise, stopped at the correct node. Return its value.
            else:
                return current_node.value

        # no linked list at this location. Return None.
        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
