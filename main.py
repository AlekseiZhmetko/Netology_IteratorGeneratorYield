nested_list = [
['a', 'b', 'c'],
['d', 'e', 'f', False],
[1, 2, None]
]

class FlattenIterator:

    @classmethod
    def __init__(self, lst):

        self.lst = lst

        def flatten(nested_list):
            tmp_lst = []
            for el in nested_list:
                for item in el:
                    tmp_lst.append(item)
            return tmp_lst

        self.flat_list = flatten(self.lst)
        self.lst = lst
        self.n = 0
        self.limit = len(self.flat_list) - 1

    def __iter__(self):
        self.cursor = self.n - 1
        return self

    def __next__(self):
        if self.cursor < self.limit:
            self.cursor += 1
            return self.flat_list[self.cursor]
        else:
            raise StopIteration

def flatten_generator(nested_list):
    for sub in nested_list:
        for element in sub:
            yield element

if __name__ == "__main__":

    for i in FlattenIterator(nested_list):
        print(i)

    flat_list = [item for item in FlattenIterator(nested_list)]
    print(flat_list)

    for i in flatten_generator(nested_list):
        print(i)