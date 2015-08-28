import DGStorage as DGS
a=DGS.DGStorage()
a.select('mthpoint');
ok=False;
i=1;
while ok==False:
	res=a.fetch(20,(i-1)*20);
	if len(res)==0:
		ok=True;
	for item in res:
		split=item["content"].split('\n');
		print(split[22][26:split[22].find('>')-1]);
		a.setprop(item["uid"],"type","math");
		a.setprop(item["uid"],"name",split[22][26:split[22].find('>')-1]);
	i+=1;
