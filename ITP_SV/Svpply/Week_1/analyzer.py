import urlparse
   
class Analyzer:
    #url ����
   def domain_url(url):
       result =urlparse.urlparse(url)
       domain_url = result.scheme +'://'+result.netloc
     # eg: www.manufactum.com
       return domain_url
    
    def query_url(url):
        result =urlparse.urlparse(url)
        query_url = result.scheme +'://' + result.netloc + result.path
       # �õ� starts��_url
        return query_url
    def domain_name(url):
        result = urlparese.urlparse(url)
        domain = result.netloc
        doman_name = domain[4:-4]
        # �õ�profile name�� eg: manufactum
        return domain_name
#��profile ��·��
f1_path = f1_path = "d:\ITPcode"+'\\'+dmain_name(url)+".py"
f1 = open(f1_path,'r+')
lines = f1.readlines()
#�޸�url
lines[14] = '''    start_urls = ["'''+querl_url+'''"]\n'''
f1.seek(0)
#product url���� profile
for line in lines:
   f1.write(line)
