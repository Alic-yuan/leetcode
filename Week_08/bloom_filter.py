from bitarray import bitarray
import mmh3


class BloomFliter:

    def __init__(self, capacity, hash_num):
        self.size = capacity
        self.hash_num = hash_num
        self.array = bitarray(self.size)
        self.array.setall(0)

    def add(self, s):
        for seed in range(self.hash_num):
            hash_index = mmh3.hash(s, seed) % self.size
            self.array[hash_index] = 1

    def find(self, s):
        for seed in range(self.hash_num):
            hash_index = mmh3.hash(s, seed) % self.size
            if self.array[hash_index] == 0:
                return 'no'
        return 'probably'


