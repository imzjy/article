Code 1-2-3
=========

来了外包公司才感受到生存的压力，时常加班，忙得没有时间休息。更别说看书，或是做别的有趣事了。在进度面前，首当其冲的是牺牲代码的质量。但愿自己还能保持自己对代码的要求，简洁，有力。

上周接到一个Bug，修改一个Message。进行一个业务操作，如果有一个收据证明(Receipt Number)的话，对用户的显示Message将所有所不同，最简单直接的实现：

```text
if (string.IsNullOrEmpty(this._presenter.ReceiptNumber))
{
    if (Utility.ShowMessageBox(Messages.Tenancy.TNC059).Equals(DialogResult.No)) return;
}
else
{
    if (Utility.ShowMessageBox(Messages.Tenancy.TNC131).Equals(DialogResult.No)) return;
}
```
光这个Snippets看不出别扭，在代码中这个Snippets还套在另一个If…else之中，那个难看啊。我想缩短代码行数：

```text
if (Utility.ShowMessageBox(string.IsNullOrEmpty(this._presenter.ReceiptNumber) ? Messages.Tenancy.TNC131 : Messages.Tenancy.TNC059).Equals(DialogResult.No)) return;
```

但是这段代码的表现力又不够强，我又修改了一下，加强一下表现力。

```text
var message = string.IsNullOrEmpty(this._presenter.ReceiptNumber) ? Messages.Tenancy.TNC131 : Messages.Tenancy.TNC059;
if (Utility.ShowMessageBox(message).Equals(DialogResult.No)) return;
```

这下，我满意多了。
