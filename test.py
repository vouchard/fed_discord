from fed_module import *
import datetime
import os


rp = dynamo_comms()
print(rp.add_response_on_word('1234', 'test', 'test_responsse2', 'vou'))
