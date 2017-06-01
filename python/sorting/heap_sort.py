
def sort(input):
    min_pq = MinPQ.buildFromList(input)
    for i in range(0, len(input)):
        input[i] = min_pq.delMin()



class MinPQ:
    def __init__(self):
        self.data = [0]

    @classmethod
    def buildFromList(cls, list):
        min_pq = cls()

        for item in list:
            min_pq.insert(item)

        return min_pq


    def insert(self, val):
        self.data.append(val)
        self.__swim_up()


    def delMin(self):
        if len(self.data) < 2:
            return None

        min_val = self.data[1]

        if len(self.data) > 2:
            self.data[1] = self.data.pop()
            self.__sink()

        return min_val


    def __swim_up(self):
        pos = len(self.data) - 1
        val = self.data[pos]

        while pos > 1:
            parent_pos = pos // 2
            if val < self.data[parent_pos]:
                self.data[pos] = self.data[parent_pos]
                pos = parent_pos
            else:
                break

        self.data[pos] = val


    def __sink(self):
        if len(self.data) < 2:
            return
        data = self.data
        pos = 1
        val = data[pos]

        while True:
            child_pos_l = pos * 2
            if child_pos_l >= len(data):
                break
            if child_pos_l + 1 >= len(data):
                min_child_pos = child_pos_l
            else:
                min_child_pos = child_pos_l if data[child_pos_l] <= data[child_pos_l + 1] else child_pos_l + 1

            if val > data[min_child_pos]:
                data[pos] = data[min_child_pos]
                pos = min_child_pos
            else:
                break
            
        data[pos] = val
            

