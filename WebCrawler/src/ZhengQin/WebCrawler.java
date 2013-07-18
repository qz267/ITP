package ZhengQin;

 
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;

public class WebCrawler {
    private String url;
    public String HtmlContent;
    public String NewsTitle;
    public String NewsContent;
 
    private String NewLine = System.getProperty("line.separator");
    
    public void Start(String url) {
        init();
        this.url = url;
        this.StartCrawling();
        this.ExtractNews();
    }
 
    private void init() {
        this.HtmlContent = null;
        this.NewsTitle = null;
        this.NewsContent = null;
    }
 
    private void ExtractNews() {
        if (this.HtmlContent == null)
            return;
 
        try {
 
            // find news title tag
            int IndexTitleStart = HtmlContent.indexOf("<!-- begin_t -->") + 16;
            int IndexTitleEnd = HtmlContent.indexOf("<!-- end_t -->");
            this.NewsTitle = HtmlContent.substring(IndexTitleStart,
                    IndexTitleEnd);
 
        } catch (StringIndexOutOfBoundsException e) {
            // e.printStackTrace();
        }
 
        try {
 
            // find news content tag
            int IndexContentStart = HtmlContent.indexOf("<!-- begin_ct -->") + 17;
            int IndexContentEnd = HtmlContent.indexOf("<!-- end_ct -->");
            String Content = HtmlContent.substring(IndexContentStart,
                    IndexContentEnd);
 
            // remove table
            int IndexTableStart = Content.indexOf("<table");
            if (IndexTableStart != -1) {
                StringBuffer buffer = new StringBuffer();
                buffer.append(Content.substring(0, IndexTableStart));
 
                int IndexTableEnd = Content.indexOf("</table>") + 8;
                buffer.append(Content.substring(IndexTableEnd));
                Content = buffer.toString();
            }
 
            // extract paragraph between <p> and </p>
 
            StringBuffer buffer = new StringBuffer();
            int IndexParaStart = Content.indexOf("<p>");
            while (IndexParaStart != -1) {
                int IndexParaEnd = Content.indexOf("</p>");
                String para = Content.substring(IndexParaStart + 3,
                        IndexParaEnd) + NewLine;
                buffer.append(para);
                Content = Content.substring(IndexParaEnd + 4);
                IndexParaStart = Content.indexOf("<p>");
            }
 
            Content = buffer.toString().trim();
 
            this.NewsContent = Content;
 
        } catch (StringIndexOutOfBoundsException e) {
            // e.printStackTrace();
        }
    }
 
    private void StartCrawling() {
        StringBuffer buffer = new StringBuffer();
 
        try {
 
            URL NewsUrl = new URL(url);
            InputStreamReader isr = new InputStreamReader(NewsUrl.openStream());
 
            while (!isr.ready()) {
                // wait until the full web page has been downloaded.
            }
 
            BufferedReader br = new BufferedReader(isr);
            while (br.ready()) {
                buffer.append(br.readLine() + NewLine);
            }
            this.HtmlContent = buffer.toString();
            br.close();
            isr.close();
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {

            e.printStackTrace();

        }

    }

}

