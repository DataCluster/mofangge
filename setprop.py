import DGStorage as DGS
a=DGS.DGStorage()
a.select('english');
ok=False;
i=0
while ok==False:
	res=a.fetch(20,(i-1)*20);
	i+=1;
	if len(res)==0:
		ok=True;
	for item in res:
		split=item["content"].split('\n');
		#print(split[22][26:split[22].find('>')-1]);
		a.setprop(item["uid"],"type","english");
		a.setprop(item["uid"],"name",split[22][26:split[22].find('>')-1]);
		#print(split[38][split[38].find('right')+8:split[38].find('right')+12]);
		a.setprop(item["uid"],"level",split[38][split[38].find('right')+8:split[38].find('right')+12]);
		print(item["prop"]);
		if item["prop"]["name"]=='':
			a.remove(item["uid"]);
			print('drop '+item["uid"]);
