from pystyle import *
import speedtest
print(Box.Lines('[+] Learn python with Rakwan'))
Write.Print('[+]this program for spead test\n',Colors.blue_to_purple,interval=0.1)
print(Box.DoubleCube('Example 5'))

st=speedtest.Speedtest()
#download  - upload
dst=st.download()
d = round(dst/ (10**6),2)
ust=st.upload()
y= round(ust/ (10**6),2)
Write.Print('[-]net download spead   is : \n',Colors.blue_to_purple,interval=0.1)
print(d ,"MB")
Write.Print('[-]net upload spead   is :\n',Colors.blue_to_purple,interval=0.1)
print(y ,"MB")
input('press any key to exit ....')