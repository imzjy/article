Enumerable in C#——内迭代与外迭代示例
===================

昨晚家里上不了网，打开以前下的视频:[what's new in csharp 3.0 ?](http://channel9.msdn.com/posts/DavidAiken/VS2008-Training-Kit-Whats-new-in-C-30/)。感叹于VS开发环境的中Code Snippet，以及 CSharp3.0 对迭代的支持。

随手仿照视频写了一个代码，用来演示CSharp3.0对迭代的支持。

```csharp
sing System;
sing System.Collections.Generic;
sing System.Linq;
sing System.Text;
amespace EnumerableTest

  class Customer
  {
        public string CustomerID { get; set; }
        public string ContactName { get; set; }
        public string City { get; set; }
    }


    class Program
    {
        static void Main(string[] args)
        {
            List<Customer> customers = LoadCustomers();

            Outer Iteration


            Inner Iteration


            LINQ,对迭代的SQL Syntax式支持，我不太喜欢，还是感觉函数式编程更爽些，更直观些


            Console.ReadKey();
        }

        private static void SeparatorLine()
        {
            Console.WriteLine();
        }

        private static void PrintCustomer(Customer cust)
        {
            Console.WriteLine("ID:{0} Contact:{1} City:{2}", cust.CustomerID.PadRight(10), cust.ContactName.PadRight(10), cust.City);
        }

        private static List<Customer> LoadCustomers()
        {
            List<Customer> customers = new List<Customer>() 
            { 
                new Customer(){ CustomerID="Andrew", ContactName="Anco", City="Hefei"},
                new Customer(){ CustomerID="Nortel", ContactName="Anco", City="Shanghai"},
                new Customer(){ CustomerID="Cisco", ContactName="Candy", City="Beijing"},
                new Customer(){ CustomerID="HP", ContactName="Peter", City="Suzhou"},
                new Customer(){ CustomerID="Lenovo", ContactName="Linda", City="Suzhou"}
            };
            return customers;
        }
    }
}
```
