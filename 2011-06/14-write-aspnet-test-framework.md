Write a asp.net web page test framework less than 150 lines of code
==================

### Talking About Test

I hate the unit test to some extent, since I think unit test is a kind of duplication. We all know “Don’t Repeat Yourself”, but test definitely duplicated with production code. Think about that you are compelled to change test when if you change the production code.

After some practice of writing test, I found the productivity improvement can persuade me to writing test in a project. As a programmer we spent a lot of time to debug when develop a application. We should cut down the debug time if we want to improve the productivity during development. Writing test a good way that can save the time in debug. We are talking about debug in here is not just finding a bug in our code, but verifying the result when implemented a function of application. We stop coding and check out our code whether working as we expected it does. This is a time killer, this is why I decide to writing test at last.

### Testing a ASP.NET web page Automatically

#### 1, Scenario

I have a asp.net web page. In that page, there is a link button and submit button on the page. as following:

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106141026158776.png)

If we click the New Account link, I will be redirect to the page that allowing user creating new a account. meanwhile, I be redirect the category list page if I fill out Category ID and click the Query Category button.The code of this page are following:

```csharp
protected void lnk_Click(object sender, EventArgs e)
{
    this.Response.Redirect("NewAccount.aspx");
}
 
protected void btnQueryCategory_Click(object sender, EventArgs e)
{
    if (txtCategoryID.Text.Trim() != string.Empty)
    {
        this.Response.Redirect(string.Format("Categories.aspx?ID={0}", this.txtCategoryID.Text));
    }
}
```

#### 2, How our test looks like

```csharp
[TestClass]
public class UnitTest1
{
    [TestMethod]
    public void CanOpenIndexPage()
    {
        AspNetTestBrowser browser = new AspNetTestBrowser();
        browser.Open("http://localhost:50002/Index.aspx");
 
        Assert.IsTrue(browser.PageHtml.Contains("Index"));
    }
 
    [TestMethod]
    public void CanRedirectNewAccountPage()
    {
        AspNetTestBrowser browser = new AspNetTestBrowser();
        browser.Open("http://localhost:50002/Index.aspx");
 
        Dictionary<string, string> parms = new Dictionary<string, string>();
        parms.Add(AspHiddenField.EVENTTARGET, "lnkNewAccount");
        parms.Add(AspHiddenField.EVENTARGUMENT, string.Empty);
        browser.Postback(parms);
 
        Assert.IsTrue(browser.PageHtml.Contains("Create New Account"));
         
    }
 
    [TestMethod]
    public void CanRedirectCategoryPage()
    {
        AspNetTestBrowser browser = new AspNetTestBrowser();
        browser.Open("http://localhost:50002/Index.aspx");
 
 
        Dictionary<string, string> parms = new Dictionary<string, string>();
        parms.Add("txtCategoryID", "5");
        parms.Add("btnQueryCategory", "Query Category");
        browser.Postback(parms);
 
        Debug.WriteLine(browser.PageHtml);
        Assert.IsTrue(browser.PageHtml.Contains("Categories"));
    }
}
```

The things you should to know is which element will be post to server when we click the button, you can refer to my previous blog. Another trick is using firebug(a plugin for firefox browser). as following:

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/20110614102615238.png)

#### 3,less than 150 lines of code to help our test

The things our test framework does:

- extract the hidden field by asp.net.
- post the web page by WebClient class(built in .net framework)
 

[Here is the code](http://code.google.com/p/code-gallery/source/browse/trunk/dotnet/aspnet-test-utils/aspnet-test-lib/AspNetTestBrowser.cs):

```csharp
namespace aspnet_test_lib
{
    public class AspHiddenField
    {
        public const string VIEWSTATE = "__VIEWSTATE";
        public const string EVENTVALIDATION = "__EVENTVALIDATION";
        public const string EVENTTARGET = "__EVENTTARGET";
        public const string EVENTARGUMENT = "__EVENTARGUMENT";
    }
 
    public static class WebClientEx
    {
        public static string HttpPost(this WebClient webClient, string URI, string Parameters)
        {
            WebRequest req = System.Net.WebRequest.Create(URI);
            //Add these, as we're doing a POST
            req.ContentType = "application/x-www-form-urlencoded";
            req.Method = "POST";
            //We need to count how many bytes we're sending. Post'ed Faked Forms should be name=value&
            byte[] bytes = System.Text.Encoding.ASCII.GetBytes(Parameters);
            req.ContentLength = bytes.Length;
            System.IO.Stream os = req.GetRequestStream();
            os.Write(bytes, 0, bytes.Length); //Push it out there
            os.Close();
            System.Net.WebResponse resp = req.GetResponse();
            if (resp == null) return null;
            System.IO.StreamReader sr = new System.IO.StreamReader(resp.GetResponseStream());
            return sr.ReadToEnd().Trim();
        }
    }
 
    public class AspNetTestBrowser
    {
        private WebClient _webClient = new WebClient();
        public WebClient WebClient
        {
            get { return _webClient; }
        }
 
        private string _pageHtml = string.Empty;
        public string PageHtml
        {
            get { return _pageHtml; }
            private set { _pageHtml = value; }
        }
 
        private string _urlLocation = string.Empty;
        public string UrlLocation
        {
            get { return _urlLocation; }
            private set { _urlLocation = value; }
        }
 
        public string Open(string address)
        {
            this.UrlLocation = address;
            PageHtml = WebClient.DownloadString(address);
 
            return PageHtml;
        }
 
        public string Postback(string address, IDictionary<string, string> parms)
        {
             
            parms.Add(AspHiddenField.VIEWSTATE, GetAspHiddenField(this.PageHtml, AspHiddenField.VIEWSTATE));
            string eventValidation = GetAspHiddenField(this.PageHtml, AspHiddenField.EVENTVALIDATION);
            if (eventValidation != null)
            {
                parms.Add(AspHiddenField.EVENTVALIDATION, GetAspHiddenField(this.PageHtml, AspHiddenField.EVENTVALIDATION));
            }
 
 
            string urlParameters = string.Empty;
            foreach (var parm in parms)
            {
                if (!string.IsNullOrEmpty(parm.Value))
                {
                    urlParameters += string.Format("{0}={1}", parm.Key, parm.Value);
                    urlParameters += "&";
                }
            }
            if (urlParameters.EndsWith("&"))
            {
                urlParameters = urlParameters.Remove(urlParameters.Length - 1, 1);
            }
 
            this.PageHtml = this.WebClient.HttpPost(address, urlParameters);
 
            return this.PageHtml;
        }
 
        public string Postback(string address, string parms)
        {
            this.PageHtml =  this.WebClient.HttpPost(address, parms);
            return this.PageHtml;
        }
 
        public string Postback(IDictionary<string, string> parms)
        {
            return this.Postback(this.UrlLocation, parms);
        }
 
        private string GetAspHiddenField(string pageHtml, string hiddenField)
        {
            string pattern = string.Format("<input type=\"hidden\" name=\"{0}\" id=\"{0}\" value=\"(?<view>.*)\" />",
                hiddenField);
            Regex regex = new Regex(pattern);
            var match = regex.Match(pageHtml);
 
            if (match.Groups["view"].Success)
            {
                return match.Groups["view"].Value;
            }
            else
            {
                return null;
            }
        }
    }
}
```
 
