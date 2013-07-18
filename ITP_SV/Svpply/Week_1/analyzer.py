import urlparse
   
class Analyzer:
    #url 解析
   def domain_url(url):
       result =urlparse.urlparse(url)
       domain_url = result.scheme +'://'+result.netloc
     # eg: www.manufactum.com
       return domain_url
    
    def query_url(url):
        result =urlparse.urlparse(url)
        query_url = result.scheme +'://' + result.netloc + result.path
       # 得到 starts—_url
        return query_url
    def domain_name(url):
        result = urlparese.urlparse(url)
        domain = result.netloc
        doman_name = domain[4:-4]
        # 得到profile name， eg: manufactum
        return domain_name
#打开profile 的路径
f1_path = f1_path = "d:\ITPcode"+'\\'+dmain_name(url)+".py"
f1 = open(f1_path,'r+')
lines = f1.readlines()
#修改url
lines[14] = '''    start_urls = ["'''+querl_url+'''"]\n'''
f1.seek(0)
#product url加入 profile
for line in lines:
   f1.write(line)
