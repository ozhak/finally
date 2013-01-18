#!/usr/bin/env python
# finally: a decent file browser

# import libraries
from tkinter import *
from glob import glob
import os, sys, time
from os.path import expanduser as expand

# global variables
config = {'show_hidden':False, 'sort':'alpha', 'line_height':12}
current = {'sort':config['sort'], 'mp':None, 'dirlist':[], 'dir':'~', 'glob':'*', 'status':None}
colors = {}

# define functions
def parseArgs(args):
 for i in args[1:]:
  if i[:1] == '-':
   f = i[1:].split('=')
   if len(f) == 1:
    print("invalid argument format: %s (must have '=' to specify value)" % f[0])
   elif len(f) == 2:
    print("argument %s set to %s." % (f[0], f[1]))
  else:
   print("assuming %s is meant as file/directory to open" % i)
   current['dir'] = i

def parseConfig(file):
 """Parses a config file, returning a hash of the parsed options.  This should probably be called before parseArgs, so command-line arguments would override config file arguments."""
 file = open(file, 'r')
 hash = {}
 for i in file.readlines():
  i = i.rstrip()
  if i[:1] == '#':
   continue
  if i == '':
   continue
  spl = i.split(':', 1)
  hash[spl[0].lower()] = spl[1]
 file.close()
 return hash

### USER COMMANDS ###

def cd(directory='~', ret=False):
 global current
 if ret:
  if directory[0] == '/':
   current['dir'] = directory
  else:
   current['dir'] += '/' + directory
 print('dir: ' + current['dir'])
 showFiles(current['dir'], current['glob'])

### INTERNAL FUNCTIONS ###

def mglob(directory=current['dir'], glob_a=current['glob']):
 dironly = False
 if glob_a[-1] == '/' and len(glob_a) > 1:
  glob_a = glob_a[:-1]
  dironly = True
 lst = glob(directory + '/' + glob_a)
 ret = []
 for i in lst:
  if dironly:
   if os.path.isdir(i):
    ret.append(i.split('/')[-1])
  else:
   ret.append(i.split('/')[-1])
 return ret

### GUI FUNCTIONS ###

def convertToCommand(input, returned):
 si = input.split()
 cmd = si[0] + '(' + input[len(si[0])+1:]
 return cmd + ', ret=' + str(returned) + ')'

def mlRet(event):
 input = event.widget.get("1.0", END).rstrip()
 if len(input) == 0:
  return
 f = convertToCommand(input, True)
 print(f)
 eval(f)
 ml.delete("1.0", END)

def mlKey(event):
 pass
 #input = ml.get("1.0", END).rstrip()
 #if len(input) == 0:
 # return
 #eval(convertToCommand(input, False))
 
def status(text, timer=2500):
 mp.move('statuses', 0, -13)
 t = mp.create_text(0, mp.winfo_height(), anchor=SW, text=text, tags=('statuses', ), fill='#fff')
 mp.after(timer, lambda: mp.delete(t))
 
def showFiles(directory=current['dir'], glb=current['glob']):
 listing = mglob(directory, glb)
 if current['sort'] == 'alpha':
  listing.sort()
 for i in listing:
  print(i)

# program
if __name__ == '__main__':
 colors = parseConfig('/home/modula/.finally_colors')
 if current['dir'] == '~':
  current['dir'] = os.environ['HOME']
 os.chdir(current['dir'])
 root = Tk()
 root.title('finally')
 ml = Text(root, height=1, undo=100)
 ml.bind('<KeyRelease>', mlKey)
 ml.bind('<Key-Return>', mlRet)
 ml.focus_set()
 ml.pack(fill=X, side=BOTTOM)
 mp = Canvas(root, bd=0, bg='#000000')
 mp.pack(fill=BOTH, expand=1, side=TOP)
 current['mp'] = mp
 root.mainloop()
