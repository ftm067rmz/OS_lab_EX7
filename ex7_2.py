class fraction:
    def __init__(self,s1=0,s2=0,m1=0,m2=0):
        self.s1 = s1
        self.s2 = s2
        self.m1 = m1
        self.m2 = m2

    def Sum(a):
        a.soorat = a.s1 + a.s2
        a.makhraj = a.m1 + a.m2
        print('Sum is : ' , a.soorat , '/' , a.makhraj)

    def Sub(self):
        if self.s1 > self.s2:
            self.soorat = self.s1 - self.s2
        else:
            self.soorat = self.s2 - self.s1

        if self.m1 > self.m2:
            self.makhraj = self.m1 - self.m2
        else:
            self.makhraj = self.m2 - self.m1

        print('Sub is : ' , self.soorat , '/',  self.makhraj)

    def Mul(self):
        self.soorat = self.s1 * self.s2
        self.makhraj = self.m1 * self.m2
        print('Mul is : ' , self.soorat , '/' , self.makhraj)

    def Div(self):
        self.soorat = self.s1 * self.m2
        self.makhraj = self.m1 * self.s2
        print('Div is : ' , self.soorat , '/' , self.makhraj)


print('Please enter two fractions:')
s1=int(input('soorat 1 : '))
m1=int(input('makhraj 1 : '))
s2=int(input('soorat 2 : '))
m2=int(input('makhraj 2 : '))

userInp = fraction(s1 , s2 , m1 , m2)

userInp.Sum()
userInp.Sub()
userInp.Mul()
userInp.Div()