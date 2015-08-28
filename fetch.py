import DGStorage as DG
import subprocess;
import os;
import time;
a=DG.DGStorage()
def checkout(web):
	subprocess.check_output('wget --user-agent="Links (2.8; Linux 2.6.32-504.30.3.el6.x86_64 x86_64; GNU C 4.4.7; text)" --output-document=tmp -q "'+str(web)+'"',shell=True);
a.create('yuwenpoint')
a.select('yuwenpoint')
i=1;
while i<=184:
	checkout('http://www.mofangge.com/qlist/yuwen/'+str(i));
	print(i);
	with open('tmp') as cont:
		a.add(i,cont.read());
	i+=1;
	os.remove('tmp');
	time.sleep(3);
print('done');

b=DG.DGStorage()
b.create('yingyupoint')
b.select('yingyupoint')
i=1;
while i<=333:
	checkout('http://www.mofangge.com/qlist/yingyu/'+str(i));
	print(i);
	with open('tmp') as cont:
		b.add(i,cont.read());
	i+=1;
	os.remove('tmp');
	time.sleep(3);
print('done');

c=DG.DGStorage()
c.create('hxpoint')
c.select('hxpoint')
i=1;
while i<=595:
	checkout('http://www.mofangge.com/qlist/huaxue/'+str(i));
	print(i);
	with open('tmp') as cont:
		c.add(i,cont.read());
	i+=1;
	os.remove('tmp');
	time.sleep(3);
print('done');

d=DG.DGStorage()
d.create('swpoint')
d.select('swpoint')
i=1;
while i<=482:
	checkout('http://www.mofangge.com/qlist/shengwu/'+str(i));
	print(i);
	with open('tmp') as cont:
		d.add(i,cont.read());
	i+=1;
	os.remove('tmp');
	time.sleep(3);
print('done');
