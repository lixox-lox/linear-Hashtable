from typing import TypeVar
"""
Module implementing a simple Linear Hashing table with open addressing and linear probing.
Functions:
    data_to_key(data: D) -> K:
        Extracts the key from the given data object. If the object has a 'key' attribute, it is used as the key; otherwise, the object itself is used as the key.
Classes:
    LinearHashing:
        Implements a hash table with linear probing for collision resolution.
        Methods:
            __init__(self, l: int) -> None:
                Initializes the hash table with a fixed size 'l'.
            insert(self, data: object) -> bool:
                Inserts the given data into the hash table. Returns True if the data was inserted, or False if the table is full or the key already exists.
            delete(self, data: D) -> bool:
                Deletes the given data from the hash table. Returns True if the data was found and deleted, otherwise False.
            fill_empty(self, index: int) -> None:
                Internal method to maintain the hash table after a deletion by filling empty slots to preserve probe sequences.
            locate(self, key: K) -> D:
                Returns the data associated with the given key. Raises KeyError if the key is not found.
            search(self, key: K) -> bool:
                Returns True if the key exists in the hash table, otherwise False.
"""

D = TypeVar('D')
K = TypeVar('K')
def data_to_key(data : D) -> K:
    if hasattr(data, 'key'):
        return data.key
    else:
        return data

class LinearHashing:

    def __init__(self, l: int) -> None:
        self.l = l
        self.liste = [None] * l  
        self.k = len(self.liste)
        
    def insert(self, data: object) -> bool:  
        key = data_to_key(data)
        if not isinstance(key, int):
            raise TypeError("Der Datentyp muss int sein.")
        index = key % self.k
        for i in range(self.k):
            probeIndex = (index + i) % self.k
            if self.liste[probeIndex] is None:
                break
            if data_to_key(self.liste[probeIndex]) == key:
                return False 
        for i in range(self.k):
            probeIndex = (index + i) % self.k
            if self.liste[probeIndex] is None:
                self.liste[probeIndex] = data
                return True
        return False
                    
           

    def delete(self, data : D) -> bool:  
        key = data_to_key(data)
        if not isinstance(key, int):
            raise TypeError("Der Datentyp muss int sein.")
        index = key % self.k
        for i in range(self.k):
            probeIndex = (index + i) % self.k
            if self.liste[probeIndex] == data:
                break
        else:
            return False
        self.liste[probeIndex] = None
        self.fill_empty(probeIndex)
        return True
        

    def fill_empty(self, index : int) -> None:
        for i in range(1,self.k):
            probeIndex = (index +i) % self.k
            if self.liste[probeIndex] is None:
                continue
            key = data_to_key(self.liste[probeIndex])
            home = key % self.k
            if (home <= index < probeIndex) or (probeIndex < home <= index) or (index < probeIndex < home):
                self.liste[index] = self.liste[probeIndex]
                self.liste[probeIndex] = None
                self.fill_empty(probeIndex)
                break

    def locate(self, key: K) -> D:
        if not isinstance(key, int):
            raise TypeError("Der Schlüssel muss int sein.")
        for i in range(self.k):
            index = (key + i) % self.k
            eintrag = self.liste[index]
            if eintrag is None:
                continue
            if data_to_key(eintrag) == key:
                return eintrag
        raise KeyError(f"Schlüssel {key} wurde nicht gefunden.")

    def search(self, key : K) -> bool:
        if not isinstance(key, int):
            raise TypeError("Der Schlüssel muss int sein.")
        for i in range(self.k):
            index = (key + i) % self.k
            eintrag = self.liste[index]
            if eintrag is None:
                continue
            if data_to_key(eintrag) == key:
                return True
        return False
    
