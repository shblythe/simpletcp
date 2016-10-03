import Queue
from simpletcp.tcpserver import TCPServer

def echoreverse(ip, queue, data):
    # Reverse the data.
    # result = reversed(data)
    # Convert each byte to a character.
    # result = [chr(b) for b in reversed(data)]
    # Turn the list of characters into a string with "" in between each char.
    # result = "".join([chr(b) for b in reversed(data)])
    # Turn the whole thing back into bytes with UTF-8 encoding.
    # result = bytes("".join([chr(b) for b in reversed(data)]), "UTF-8")
    # Put the result back into the queue of data to be sent back:
    """ No UTF-8 support in this version
    queue.put(bytes("".join([chr(b) for b in reversed(data)]), "UTF-8"))
    """
    queue.put(data[::-1])

server = TCPServer("localhost", 5000, echoreverse)
server.run()
