#!/bin/python

"""
Halo gan ?
sedang liat liat Apa?
record ya? wkwwk ga tau malu
+ buta program
"""
#   Import Module   #
import random , os , sys , marshal , time

#   Warna   #
b = '\033[1;34m'
r = '\033[31m'
g = '\033[32m'
w = '\033[0m'
y = '\033[33;5m'
p = '\x1b[0m'

def ketik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)

def banner():
	print
	print (r+" ......				  ......")
	print ("(      )"+g+"  Compile Marshal Python"+r+" (	)")
	print (" (    ) "+b+"Author : Zeerx7"+r+"           (    )")
	print ("  |  | "+b+" Team   : Rao Cyber Team "+r+"   |  |")
	print ("  |  | "+b+" Created: 28-07-2019"+r+"	   |  |")
	print ("  ^^^^				   ^^^^"+w)

try:
    os.system("clear")
    banner()
    print ("Contoh: /sdcard/file.py")
    files = raw_input("#=> ")
    ah = files.replace('.py', '')
except KeyboardInterrupt:
    print("[Detect] Ctrl + C ")
    exit()
else:
    try:
        strng = open(files, 'r').read()
    except IOError:
        print ""
        print (r+' ['+y+'!'+r+']['+g+files+r+'][ '+b+'No such file or directory '+r+']'+r+'['+y+'!'+r+']'+w)
        sys.exit()

code = compile(strng, '<daffa>', 'exec')
co = marshal.dumps(code)
fileout = open(ah + 'enc.py', 'wb')
fileout.write('#Compiled By Zeerx7\n')
fileout.write('#Rao Cyber Team\n\n')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads(' + repr(co) + '))')
fileout.close()
time.sleep(2)
print
print (g+"<\>:"+b+" File baerhasil di compile"+r+' ['+y+'!'+r+']['+g+ah+'enc.py'+r+']'+w)
