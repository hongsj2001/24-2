class bitskey:
    def __init__(self, x):
        self.x = x

    def get(self):
        return self.x

    def bits(self, k, j): #k번 비트가 0인지 1인지 판별한다.
        return (self.x >> k) & ~(~0 << j)

a = int(input('입력 : '))
while a != 999:
    v = bitskey(a)
    print('키값 :',  v.get())
    print(v.bits(4, 1)) #4번 비트가 0인지 1인지 판별
    print(v.bits(3, 1))
    print(v.bits(2, 1))
    print(v.bits(1, 1))
    print(v.bits(0, 1))
    a = int(input('a = '))