SQL Server orderby with some fixed values
========

I came across a problem when we want to set the default language to English in a dropdown list. Such as:

```text
Chinese
Danish
English
German
Japanese
Swedish
```

We want the English come to the first, and the rest follows That’s:

```text
English    //go to first
Chinese
Danish
German
Japanese
Swedish
```

We can do this by uniting the two SQL result sets:

```sql
select * from country where lang='English'
union
select * from country where lang<>'English'
```
