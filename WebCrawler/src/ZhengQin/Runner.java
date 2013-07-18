package ZhengQin;

//import ZhengQin.*;
 
public class Runner {
 
    public static void main(String args[]){
 
        String [] urls = new String[3];
 
        urls[0] = "http://news.xinhuanet.com/english2010/business/2011-01/25/c_13705297.htm";
        urls[1] = "http://news.xinhuanet.com/english2010/business/2011-01/25/c_13705819.htm";
        urls[2] = "http://news.xinhuanet.com/english2010/china/2011-01/25/c_13705900.htm";
 
        WebCrawler crawler = new WebCrawler();
 
        for(String url : urls)
        {
            crawler.Start(url);
            System.out.println(url);
            System.out.println(crawler.NewsTitle);
            System.out.println(crawler.NewsContent);
            System.out.println();
 
        }
    }
}

