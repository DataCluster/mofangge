import DGStorage as DG;
import urllib.parse;
a=DG.DGStorage();
type='biology';
a.select(type);
b=DG.DGStorage();
b.select('knowledgebase');
ok=False;
i=0;
while ok==False:
	res=a.fetch(20,(i-1)*20);
	i+=1;
	if len(res)==0:
		ok=True;
	content=[];
	for item in res:
		split=item["content"].split('\n');
		split=split[38].split('●');
		#print(len(split));
		if len(split)==31: #超过一页了，最后一项是分页
			split=split[1:-1];
			split=split[0:4]; #要不然题太多了
			for element in split:
				element=element.split('</a>')[0];
				#print(element.find('.html">'));
				url=element[element.find('<a href=')+9:element.find('.html">')+5];
				element=element[element.find('.html">')+7:element.find('</a>')-1];
				#print(element);
				content.append(element);
				b.add(url,'',{"content":element,"type":type,"kbname":item["prop"]["name"],"kb":item["uid"]});
				print('add '+item["uid"]);
		else:
			split=split[1:];
			split=split[0:4]; #要不然题太多了
			for element in split:
				element=element.split('</a>')[0];
				#print(element.find('.html">'));
				url=element[element.find('<a href=')+9:element.find('.html">')+5];
				element=element[element.find('.html">')+7:element.find('</a>')-1];
				#print(element);
				content.append(element);
				b.add(url,'',{"content":element,"type":type,"kbname":item["prop"]["name"],"kb":item["uid"]});
				print('add '+item["uid"]);
		string='';
		for element in content:
			element=urllib.parse.quote_plus(element);
			if string!='':
				string=string+','+str(element);
			else:
				string=str(element);
		#a.setprop(item["uid"],"content",string);
		#print('set content '+item["uid"]);
