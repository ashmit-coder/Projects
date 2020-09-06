class tp(object):
  def __init__(self):
    pass
  def true(self, n):
    num = 1
    if(n == 4):
      for i in range(5):
        print("*"*num)
        num += 1
    else:
        num = 4
        for i in range(5):
            print("*"*num)
            num -= 1
"""
*
**
***
****
"""
         


a = input("Give me a number my son(b/w 1 and 0) ")
while(a != "Q"):
    triangle = tp()
    if(a == "1"):
        triangle.true(4)
    else:
        triangle.true(1)
    a = input("Give me a number my son(b/w 1 and 0) or just quit by \"Q\" ")