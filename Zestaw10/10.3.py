class Stack:
    def __init__(self, size = 1024):
        self.size = size
        self.items = size * [None]
        self.matrix = {}
        for j in range(size):
            self.matrix[j] = 0
        self.n = 0
        self.top = -1

    def isEmpty(self):
        return True if(self.top == -1) else False

    def sizeof(self):
        return self.n if self.n > 0 else 0

    def pop(self): 
        if(not self.isEmpty()): 
            output = self.items[self.top]
            
            self.items[self.top] = None
            self.matrix[output] = 0

            self.top -= 1
            self.n -= 1
        else: 
            print(f'Stack is empty!\n')

    def push(self, value):
        if (self.size >= value and value >= 0):
            if(self.top + 1 <= self.size):
                if(self.matrix[value] == 0):
                    self.top += 1
                    self.items[self.top] = value

                    self.matrix[value] = 1

                    self.n += 1
                else: print(f'Value {value} is already in stack!\n')
            else: print('Stack Overflow!\n')
        else: print(f'Value {value} is not in [0, {self.size}] \n')

    def peek(self):
        if(not self.isEmpty()):
            return self.data[self.top]
        else: 
            print(f'Stack is empty!\n')
            return None

    def str(self):
        output = ''

        if not self.isEmpty(): 
            for j in range(self.top + 1): 
                output += str(self.items[j]) + ', '

            output = output[:-2]
            out = output[::-1]

            return 'Stack: ' + out + '\n'
        else: return 'Stack is empty!\n'

if __name__ == '__main__':
    stos = Stack()

    print(stos.isEmpty())
    stos.push(0)
    stos.push(1)
    print(stos.str())
    stos.push(3)
    stos.push(0)
    print(stos.str())
    stos.pop()
    print(stos.str())
    print(stos.isEmpty())