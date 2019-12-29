#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
import threading
import struct
import random


# In[2]:


c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# In[3]:


pars = ('127.0.0.1', 80) # server IP and server port
c.connect(pars)


# In[4]:


while True:
    
    type_value = 8
    code_value = 255
    unused_value = 0
    identifier = random.randint(0, 2**16-1)
    sequence_value = 1
    message_value = 106306056
    
    # let the client talk firt
    send_data_1 = struct.pack("!BBHHHI", type_value, code_value, 
                              unused_value,  identifier, 
                              sequence_value, message_value)
    c.send(send_data_1)
    print('Data sent by Client: ', struct.unpack("!BBHHHI", send_data_1))
    
    # then wait for server response
    data_recv = c.recv(12)
    unpacked_data = struct.unpack("!BBHHHI", data_recv)
    if unpacked_data:
        print("From server:", unpacked_data)

    # terminate
    #c.send(b'close')
    break
    
# close directly
c.close()


# In[ ]:




