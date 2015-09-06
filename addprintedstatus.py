import DGStorage as DGS
a=DGS.DGStorage();
a.select('biology');
ok=False;
i=0
while ok==False:
	res=a.fetch(20,(i-1)*20);
	i+=1;
	if len(res)==0:
		ok=True;
	for item in res:
		a.setprop(item["uid"],"printed","no");
		print('set '+item["prop"]["name"]);
