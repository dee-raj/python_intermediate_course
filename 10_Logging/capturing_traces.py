import logging

# if you knnow what type of error should be except in exception
try:
   a = [1, 3, 5, 7]
   val = a[4]
except IndexError as e:
   # logging.error(e)
   logging.error(e, exc_info=True)

#let's say you don't now what exception should be excepted
import traceback 
try:
   price = 82
   cost = price + 'k'
except:
   logging.error("This error is:\n%s", traceback.format_exc())