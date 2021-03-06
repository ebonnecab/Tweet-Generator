#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
    #Return a list of all keys in this hash table.
    #Running time: O(???) Why and under what conditions?

        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
    # Running time: O(l) because we are looping through all the buckets and their items
    #Return a list of all values in this hash table. 
      
        all_values = []

        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values
       

    def items(self):
    #Return a list of all items (key-value pairs) in this hash table.
    #Running time: O(l) because you loop through each bucket
 
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
    #Return the number of key-value entries by traversing its buckets.
    #Running time: O(b * l) --> O(n) b/c for each bucket you go to every node
        length = 0

        #Loop through all buckets
        for bucket in self.buckets: #b iterations of a loop
            length += bucket.length()#O(l)
            
        return length
        
    def contains(self, key):
        #Return True if this hash table contains the given key, or False.
        #Running time: O(l) because you loop through all the buckets

        #Find bucket where given key belongs
        for bucket in self.buckets:
            for current_key, value in bucket.items():
        #Check if key-value entry exists in bucket
                if current_key is key: #constant run time
                    return True
        return False

    def get(self, key):
        #Return the value associated with the given key, or raise KeyError.
        #Running time: O(l) because it depends on the length of hash table

        #Find bucket where given key belongs
        index = self._bucket_index #constant time to calculate index
        bucket = self.buckets[index(key)] #constant time to index an array

        #Check if key-value entry exists in bucket
        key_matcher = lambda key_val: key_val[0] == key
        entry_found = bucket.find(key_matcher) # 0(l) with l = bucket.length()

        #If found, return value associated with given key
        if entry_found is not None:
            return entry_found[1] #entry = (key, value)
        #Otherwise, raise error to tell user get failed
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        #Insert or update the given key with its associated value.
        #Running time: best case is O(1) or worst case is O(l)

        # Find bucket where given key belongs
        index = self._bucket_index # O(1) to calculate index
        bucket = self.buckets[index(key)] # constant time to index array

        # Check if key-value entry exists in bucket
        entry_found = bucket.find(lambda key_val: key_val[0] == key ) #O(l)

        # If found, update value associated with given key
        if entry_found is not None: #constant time
            bucket.delete(entry_found) #get rid of old key,val pair

        #Otherwise, insert given key-value entry into bucket
        entry_found = (key, value)
        bucket.append((key, value))

    def delete(self, key):
        #Delete the given key from this hash table, or raise KeyError.
        #Running time: O(l) where l = buckets.length()

        # Find bucket where given key belongs
        index = self._bucket_index #constant time to assign variable(s)
        bucket = self.buckets[index(key)]

        #Check if key-value entry exists in bucket
        key_matcher = lambda key_val: key_val[0] == key
        entry_found = bucket.find(key_matcher)#O(l) where l = bucket.length()

        #If found, delete entry associated with given key
        if entry_found is not None: #constant time to check for entry found
            bucket.delete(entry_found) #0(l) where l = buckets.length()

        #Otherwise, raise error to tell user delete failed
        else:
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
