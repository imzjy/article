Enumerable in C#——内迭代与外迭代示例
===================

昨晚家里上不了网，打开以前下的视频:[what's new in csharp 3.0 ?](http://channel9.msdn.com/posts/DavidAiken/VS2008-Training-Kit-Whats-new-in-C-30/)。感叹于VS开发环境的中Code Snippet，以及 CSharp3.0 对迭代的支持。

随手仿照视频写了一个代码，用来演示CSharp3.0对迭代的支持。

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace EnumerableTest
{
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

            #region Outer Iteration
            //使用外迭代 One
            foreach (var cust in customers)
            {
                PrintCustomer(cust);  //可将迭代子(Iterator)传给其它函数

                //也可以进行Filter，但不是很Elegant
                if (cust.City == "Suzhou")
                    PrintCustomer(cust);
            }
            SeparatorLine();
            //使用外迭代 Two
            IEnumerator<Customer> itor = customers.GetEnumerator();
            while (itor.MoveNext())
            {
                PrintCustomer(itor.Current);
            }
            SeparatorLine();
            
            #endregion


            #region Inner Iteration
            //使用内迭代，对每个元素执行一个操作(函数),思想上实现了函数式编程
            //语义上：对每个元素执行，一个函数Action（PrintCustomer）,下面的语义等同于：
            //Action<Customer> printCustomer = delegate(Customer c)
            //{
            //    Console.WriteLine("ID:{0} Contact:{1} City:{2}", c.CustomerID.PadRight(10), c.ContactName.PadRight(10), ity);
            //};
            //customers.ForEach(printCustomer);
            customers.ForEach(c => PrintCustomer(c));  //More convenience, more elegant
            SeparatorLine();

            //使用内迭代，进行Filter:Where(c => c.City == "Suzhou")
            customers.Where(c => c.City == "Suzhou").ToList().ForEach(c => PrintCustomer(c));
            SeparatorLine();
            //多级Filter
            customers.Where(c => c.City == "Suzhou").Where(c => c.ContactName == "Peter").ToList().ForEach(c => ntCustomer(c));
            SeparatorLine(); 
            #endregion


            #region LINQ,对迭代的SQL Syntax式支持，我不太喜欢，还是感觉函数式编程更爽些，更直观些
            //似乎对于LINQ来说，Query功能完善。而：对于每一个元素执行一个操作（函数）却不支持.
            var result = from c in customers
                         where c.City == "Suzhou"
                         where c.ContactName == "Peter"
                         select c;

            result.ToList().ForEach(c => PrintCustomer(c));

            SeparatorLine();
            #endregion


            Console.ReadKey();
        }

        private static void SeparatorLine()
        {
            Console.WriteLine();
        }

        private static void PrintCustomer(Customer cust)
        {
            Console.WriteLine("ID:{0} Contact:{1} City:{2}", cust.CustomerID.PadRight(10), cust.ContactName.PadRight(10), t.City);
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
