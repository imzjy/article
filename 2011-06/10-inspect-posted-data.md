Which data be post to the server when submitting a form
================

### 1,HTML Specification
In HTML specification, a section of [form submission](http://www.w3.org/TR/html401/interact/forms.html#h-17.13) dedicated to explain which data should be post to the sever when submitting a form. User agent(such as Chrome, IE) which compliant with the specification will send [form data set](http://www.w3.org/TR/html401/interact/forms.html#form-data-set) to the server by http protocol.

In general, form data set is a key/value pairs in which contains a number of name/value extracted by html element. Not all of html element value will be extracted, only [successful controls](http://www.w3.org/TR/html401/interact/forms.html#successful-controls) will be extracted and combine together as form data set.

Any elements that have the attribute of name and value is a successful control, except:

- Controls that are disabled cannot be successful.
- If a form contains more than one submit button, only the activated submit button is successful.
- All "on" checkboxes may be successful.
- For radio buttons that share the same value of the name attribute, only the "on" radio button may be successful.
- For menus, the control name is provided by a SELECT element and values are provided by OPTION elements. Only selected options may be successful. When no options are selected, the control is not successful and neither the name nor any values are submitted to the server when the form is submitted.
- The current value of a file select is a list of one or more file names. Upon submission of the form, the contents of each file are submitted with the rest of the form data. The file contents are packaged according to the form's content type.
- The current value of an object control is determined by the object's implementation.
- If a control doesn't have a current value when the form is submitted, user agents are not required to treat it as a successful control.

Please refer to [specification](http://www.w3.org/TR/html401/interact/forms.html#successful-controls) for details.

### 2,Example

If you have a web page like this:

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106101408065618.png)

```html
<html>
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        <input type="text" name="user" value=" " /><br /><br />
        <input type="checkbox" name="chk" value="CheckBoxA" /><span>CheckBoxA</span>
        <input type="checkbox" name="chk" value="CheckBoxB" /><span>CheckBoxB</span><br /><br />
        <input id="Radio1" type="radio" /><span>RadioA</span>
        <input id="Radio2" type="radio" /><span>RadioB</span><br /><br />
        <select id="Select1" name="Select1">
            <option>England</option>
            <option>US</option>
            <option>China</option>
        </select>
        <br /><br />
        <input id="Hidden1" name="Hidden1" type="hidden" value="HiddenValueA" />
        <input type="text" name="disableText" value=" DisableTextA" disabled="disabled" />
        <input type="text" name="invisbleText" value="invisbleText" style ="display:none;" />
    </div>
    <br /><br />
    <input id="Submit1" type="submit" value="submit" />
    </form>
</body>
</html>
```

We type some words and click some checkboxes, as following example. Which element’s value will be send after clicking submit button?

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106101408077047.png)

The answer(using firebug) to the example is:

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/201106/201106101408076240.png)

 

### Some question you may ask?

#### Q: Why RadioA do not extract as name/value pair?

A: Radio controls do not set the name attribute. if the radio control contains a atrribute called name, as <input id="Radio1" type="radio" name="Radio1" /><span>RadioA</span>, it will be extracted as name/value pair and send to server.

#### Q:How to extract the value in server-side by asp.net?

A:You want to extract value of user, for instance, you can use:

`string userValue = this.Request.Form["user"];`
 
#### Q:If the name of element duplicated, such as two of checkbox are named chk, how to separate one from another?

A:In server-side, they be separated by comma(,). If you extract the value of checkbox by follow csharp statement:

`string chk = this.Request.Form["chk"];`

You’ll get value as : CheckBoxA,CheckBoxB
