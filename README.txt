#
# zEquals :)
#

Because it starts with a z.
Because I've heard about it via 'Numberphile'.
Because it's awesome.

Basic usage:

    >>> from zequals import *
    >>> zMul(1345,653)
    589100

If you are thinking : Now what's the use, 1345 times 653 should be 589680....

Please take a look here : http://www.youtube.com/watch?v=aOJOfh2_4PE

But it get's better!

After installing zequals one could do this :

from zequals import z

@z
def myAwesomeMathFunctions(x,y,z):
  d = someWickedCalculus(x,y)
  f = someOtherWeirdThing(z,x)
  return d/f

The 'deocration' of your function with the @z decorator will make sure all
arguments passed to your function will be 'zequalized'.

Real World Example:

import math

def myFunc(a,b):
  return math.sqrt((a*a) + (b*b))

myFunc(1253,3543)
# will yield : 3758.03911634778

now once we go

@z
def myFunc(a,b):
  return math.sqrt((a*a) + (b*b))

myFunc(1253,3543)
# will yield 3754.210969031975


GitHub Repo : https://github.com/zdevops/zequals
