
class Model:

    def __init__(self):
        self.d = {}
        self.ref = []

    def getNear(self, n):
        self.ref.sort()
        left = self.ref[0]
        right = self.ref[1]
        for i in range(len(self.ref)):
            if self.ref[i] < n and self.ref[i] > left:
                left = self.ref[i]
                try :
                    right = self.ref[i+1]
                except IndexError:
                    right = self.ref[i]
        return (left,right)
                
    def predict(self, n):
        if n in self.ref:
            return self.d[n]
        if n > max(self.ref):
            return self.d[max(self.ref)]
        x1 = self.getNear(n)[0]
        x2 = self.getNear(n)[1]
        y1 = self.d[x1]
        y2 = self.d[x2]
        return "%.2f" % ((((n-x1+1)*(y2-y1+1))/(x2-x1+1)) + y1 - 1)

    def train(self, file_name):
        obj = open(file_name)
        data = obj.read()
        obj.close()

        data = data.split('\n')

        for e in data:
            t = e.split(',')
            self.ref.append(eval(t[0]))
            self.d[eval(t[0])] = eval(t[1])


if __name__ == "__main__":
    model = Model()
    model.train("trainingdata.txt")
    while True:
        i = float(raw_input("Enter the no. of Hours charged > "))
        print model.predict(i)
