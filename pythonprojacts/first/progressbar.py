from pystyle import *
import time 
from tqdm import tqdm
print(Box.Lines('[+]Learn python with rakwan[+]'))
Write.Print('This program for progress bar  \n',Colors.blue_to_cyan,interval=0.1)
print(Box.DoubleCube('Example [10]'))

with tqdm(total=100) as pbar:
    for i in range(100):
        time.sleep(0.1)
        pbar.update(1)
    print('Finish')


input( '...........')