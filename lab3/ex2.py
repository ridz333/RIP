import ex1

class Iterator:
    def __init__(self, list, ignore_case=True):
        self.list = get_unique_list(list,ignore_case)
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < len(self.list):
            res = self.list[self.num]
            self.num += 1
            return res
        else:
            raise StopIteration()


def get_unique_list(list, ignore_case):
    uList = []

    if ignore_case:
        try:
            list = [el.lower() for el in list]
        except:
            list = [el for el in list]

    for el in list:
        if el not in uList:
            uList.append(el)
    return uList

def main():
    data = ['a', 'A', 'b', 'B']
    list = ex1.gen_random(1,3,10)

    obj1 = Iterator(data)
    obj2 = Iterator(list)

    print([el for el in obj1])
    print([el for el in obj2])

if __name__ == '__main__':
    main()