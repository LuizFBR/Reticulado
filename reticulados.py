import random

class Reticulado():
    def __init__(self, pairs):
        self.adj_list = {}
        for pair in pairs:
            if pair[0] not in self.adj_list:
                self.adj_list[pair[0]] = [pair[1]]
            else:
                self.adj_list[pair[0]].append(pair[1])

    def generate(self, start, n):
        if n == 0: return Reticulado([])
        if start == n: return Reticulado([[n,n]])
        new_start = random.randint(start,n)
        upper_layer = self.generate(self, new_start, n)
        reti = {}
        for i in range(start,new_start):
            flag = 0
            for j in upper_layer.adj_list:
                print(i,j)
                if random.randint(0,1) == 1:
                    if i not in reti:
                        reti[i] = [j]
                    else:
                        reti[i].append(j)
                    flag = 1
                if not flag:
                    reti[i] = [j]
        upper_layer.adj_list.update(reti)
        return upper_layer

Reticulado.generate = staticmethod(Reticulado.generate)

reti = Reticulado.generate(Reticulado,1,4)
print(reti.adj_list)