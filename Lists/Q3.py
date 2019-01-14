# Generate  a  list  of  100  numbers,  1  to  100,  without  using  a  traditional  looping  technique  (investigate  list  comprehensions).  Shuffle  the  list  up  so  the  numbers  are  not  in  order.  (Ms.  Healey)

import random

print("\nQ3.")

a3 = [x for x in range(1, 101)]

random.shuffle(a3)  # https://stackoverflow.com/questions/34862378/randomizing-a-list-in-python (9.27.18)

print(a3) 