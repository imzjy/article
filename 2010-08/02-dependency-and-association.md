Dependency & association in UML
=========

There two types of relationship between Classes: dependencies and associations.When we talk about one and while we forget another, this is misunderstanding caused by definition of dependency and association.Normally, the definition of those terms are:

- **Dependency**: there are two classes, class A depends on class B. Class B will be affected when class A changed.
- **Association**: An association represents a structural relationship that connects two classes.

the key point:  Association imply that there is strong dependency between two classes.In other words, the definition for association should be:

An association represents a structural relationship that connects two classes.class A associate with class B. Class B will be affected when class A changed yet.

In my view, dependency emphasize the needs of on class to another. the association emphasize that structure: one class holds the another, it can use freely when it needs.

Last but not least, a simple demo will told us the truth:

The diagram describe the blow relationships:  

![](http://images.cnblogs.com/cnblogs_com/Jerry-Chou/WindowsLiveWriter/DependencyassociationinUML_11BB1/dependency_association_thumb.png)

```csharp
class Program
{
    class Phone
    {
        public void SendMessage(string name,string message)
        {
            Console.WriteLine("Hi,{0}\n{1}",name,message);
        }
    }
    class Employee
    {
        public void SayHello2Customer()
        {
            Phone phone = new Phone();       //Dependency, employee needs the phone
            phone.SendMessage("Someone", "Hello");
        }
    }
    class Manager
    {
        Employee staff = new Employee();    //Association, a structure shwos that Manager employeed the staff.
        public void SayHello2Customer()
        {
            staff.SayHello2Customer();      //Manager can employ the staff do something if he want.
        }
    }
    static void Main(string[] args)
    {
        Manager manager = new Manager();
        manager.SayHello2Customer();
 
        Console.ReadKey();
    }
}
```
