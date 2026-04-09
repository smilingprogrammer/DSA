class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        # self.int_stream = []
        self.num_op = 0
        

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.num_op += 1
        else:
            self.num_op = 0

        return self.num_op >= self.k
        # self.int_stream.append(num)

        # print("length of int stream", len(self.int_stream))
        # print("ints in stream", self.int_stream)

        # if len(self.int_stream) < self.k:
        #     return False

        # num_last_k = 0

        # for i in self.int_stream:
        #     if i == self.value:
        #         num_last_k += 1

        # self.int_stream.pop(0)
        
        # if num_last_k == self.k:
        #     return True

        # else:
        #     return False



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)