class MyIterator:

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if self.x <= 50:
            y = self.x
            self.x += 1
            return y
        else:
            raise StopIteration


it = MyIterator()
myiter = iter(it)

print(myiter)

for x in myiter:
    print(x)