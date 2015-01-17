家庭作业之线性表
======

国庆之前《数据结构》的陈老师布置了家庭作业：实现数据结构中的线性表。线性表是最常用的一种数据结构，几乎每个程序都会用到。但只是简单地把书上要求的线性表实现出来也没有多大劲。于是我想到了泛型(Generic Programing)编程，这样也许更有难度些，最主要的是更好玩，毕竟平日里自己很少在的工作中用到GP，毕竟写库的程序员也很少。

在给出源码之前，我想聊聊我们这学期的数据结构老师cy.或许是我们年纪相仿，所以很容易沟通。cy有勇气到在第一堂《数据结构》就把这门课放至它该有的位置。这着实让我佩服不已!能在第一堂课就把软件工程思想带到课堂上的老师，现在似乎也不多。很幸运我可以在学校遇到这样的好老师!

现给出顺序表的源码(Sequence List)：

```c++
//Platform: WinXp + VC6.0

/*--------------------------
File name: SeqList.h
Created date: 10/11'07
Created by Jerry
Description:

      GP实现的顺序表
---------------------------*/
#ifndef SEQLIST_H
#define SEQLIST_H
#define ERROR_ID 11111111

template<typename _MyT=int, int _Size=10>
class SeqList
{
    public:
        SeqList();
        _MyT Get(int _pos);
        int Length();
        int Locate(int _elm);
        _MyT Prior(_MyT _elm);
        _MyT Next(_MyT _elm);
        bool Empty();
        void Clear();
        void Insert(int _pos, _MyT _value);
        void Delete(int _pos);
    private:
        _MyT buffer[_Size];
        int lastIndex;

};


template<class _MyT, int _Size>
SeqList<_MyT,_Size>::SeqList()
{
    lastIndex = -1;
}

template<class _MyT, int _Size>
bool SeqList<_MyT,_Size>::Empty()
{
    if(lastIndex == -1)
        return true;
    else
        return false;

}

template<class _MyT, int _Size>
void SeqList<_MyT,_Size>::Clear()
{
    lastIndex = -1;
}

template<class _MyT, int _Size>
int SeqList<_MyT,_Size>::Length()
{
    if(Empty())
        return 0;
    else
        return lastIndex+1;
}

template<class _MyT, int _Size>
_MyT SeqList<_MyT,_Size>::Get(int _pos)
{
    if(Empty())
        return ERROR_ID;

    if(_pos > 0 && _pos <= Length())
        return buffer[_pos-1];
    else
        return ERROR_ID;

}

template<class _MyT, int _Size>
int SeqList<_MyT,_Size>::Locate(int _elm)
{
    if(Empty())
        return 0;

    for(int i=0; i<=lastIndex; i++)
    {
        if(buffer[i] == _elm)
            return i+1;
    }

    return 0;
}

template<class _MyT, int _Size>
_MyT SeqList<_MyT,_Size>::Prior(_MyT _elm)
{
    //there isn't prior element if currect list's length less than 2

    if(Length() <= 1)
        return 0;

    int pos = Locate(_elm);
    if(pos > 1)
    {
        return buffer[pos-2]; //the index of _elm of pos-1,

    }                         //therefore,pos-2 is the prior of _elm;

    else
    {
        return 0;
    }
}

template<class _MyT, int _Size>
_MyT SeqList<_MyT,_Size>::Next(_MyT _elm)
{
    //there isn't next element if currect list's length less than 2

    if(Length() <= 1)
        return 0;

    int pos = Locate(_elm);
    if(pos != 0 && pos < Length())
        return buffer[pos]; //the index of _elm of pos-1,therefore [index+1==pos]

    else
        return 0;
}

template<class _MyT, int _Size>
void SeqList<_MyT,_Size>::Insert(int _pos, _MyT _value) //(前插法)

{
    //currect list is full?

    if(Length() >= _Size)
    {
        cout<<"List is full, You couldn't insert anything!"<<endl;
        return;
    }

    //Initail first element if currect list is empty.

    if(Empty())
    {
#ifdef _DEBUG
        cout<<"Initial first element, value:"<<_value<<endl;
#endif

        buffer[0] = _value;
        lastIndex++;
        return;
    }

    //Range check

    if(_pos <= 0 || _pos > _Size)
    {
        cout<<"Overflow!"<<endl;
        return;
    }
    if(_pos > lastIndex+1)
    {
        cout<<"Line list cann't fill by disorder!"<<endl;
        return;
    }

    //Perform insert

    if(1)
    {
        for(int i=lastIndex+1; i>=_pos ; i--)
        {
            buffer[i] = buffer[i-1];
        }
        buffer[_pos-1] = _value;
        lastIndex++;
#ifdef _DEBUG
        cout<<"Insert value:"<<_value
            <<" before postion:"<<_pos<<" success!"<<endl;
#endif
    }
}

template<class _MyT, int _Size>
void SeqList<_MyT,_Size>::Delete(int _pos)
{
    //Current list is empty?

    if(Empty())
    {
        cout<<"List is full! You couldn't delete anything!"<<endl;
        return;
    }

    //Range check

    if(_pos <= 0 || _pos > Length())
    {
        cout<<"There is no value in position of "<<_pos<<" ."<<endl;
        return;
    }


    //

    if(1)
    {
#ifdef _DEBUG
        cout<<"Delete value:"<<buffer[_pos-1]
            <<" at postion:"<<_pos<<" success!"<<endl;
#endif
        for(int i=_pos-1; i<=lastIndex-1; i++)
        {
            buffer[i] = buffer[i+1];
        }
        lastIndex--;
    }

}

#endif
```

使用时只要将SeqList.h头文件包含一下就可以了，示例：

```
#include <iostream>
#include "SeqList.h"

using namespace std;

int main()
{

    SeqList<int,10> seq;
    seq.Insert(0,12);
    seq.Insert(1,43);
    seq.Insert(2,99);

    cout<<seq.Get(1)<<endl;
    cout<<seq.Get(2)<<endl;
    cout<<seq.Get(3)<<endl;

    seq.Delete(3);
    seq.Insert(1,27);

    cout<<seq.Get(1)<<endl;
    cout<<seq.Get(2)<<endl;
    cout<<seq.Get(3)<<endl;

    return 0;
}
```

其实GP写东西也挺好玩的，更容易让人看见编译时刻Compiler还可以做许多事情。也让我们更加佩服Compiler的实现者。只不过GP不是我最近学习的方向。如果一切正常我想等明年开春之后我会将GP部分再认真学习一下。

还有一个是链表，本来我是想用C来写得，但写着写着就又用到了C++的class。最终我造出一个怪物——一个混合了C和C++的链表(Link List)。首先这种编程体验就很不爽。在写代码时你就觉得[怪怪得...]。也觉得很別扭。这让我想起的Scott Meyers的《Effective C++ 3/e》的条款1：将C++视为一个语言联邦.

现在怪物要出来了(大家赶快躲啊.....)：

```c++
/*--------------------------
Notes:混合了C语言的struct和C++语言的class及封装，很不好的编程体验, I prefer c++ first.
--------------------------*/

#define DATA_NOT_FIND 0
#define ID_NOT_FIND 0

typedef struct node
{
    int ID;
    int data;
    struct node *next;
}NODE;


class LinkList
{
public:
    LinkList(){ pHead = 0; }
    void Clear(){ pHead = 0; }
    bool Empty(){ return pHead?false:true;}
    void AddNode(NODE* pNode);
    NODE* GetHead(){return pHead;}
    NODE* Find(int _id);        //retrieve data

    NODE* Locate (int _data); //retrieve id

    int Next(int _id);    //retrieve next data from the position of _id

    bool Insert(int _id, NODE* pNode); //insert _data behind _id

private:
    NODE *pHead;
};


void LinkList::AddNode(NODE* pNode) //Add to the head of LinkList.

{
    NODE* oldHead = pHead;
    pHead = pNode;
    pNode->next = oldHead;
}
NODE* LinkList::Find(int _id)
{
    for(NODE* p = pHead; p != 0; p = p->next)
    {
        if(p->ID == _id)
            return p;
    }

    return ID_NOT_FIND;
}
NODE* LinkList::Locate(int _data)
{
    for(NODE* p = pHead; p != 0; p = p->next)
    {
        if(p->data == _data)
            return p;
    }

    return DATA_NOT_FIND;
}
int LinkList::Next(int _id)
{
    NODE *p = Find(_id);
    if(p != ID_NOT_FIND)
        return p->next->data;
    else
        return ID_NOT_FIND;
}
bool LinkList::Insert(int _id, NODE* pNode)
{
    NODE *p = Find(_id);
    if(p != ID_NOT_FIND)
    {
        NODE* pOldNode = p->next;
        p->next = pNode;
        pNode->next = pOldNode;
        return true;
    }
    else
        return false;
}
```

再给出使用代码：

```
#include <iostream>
#include "LinkList.h"

using namespace std;

int main()
{
    NODE n1,n2,n3;
    //first

    n1.ID = 1;
    n1.data = 123;
    n1.next = 0;
    //second

    n2.ID = 2;
    n2.data = 456;
    n2.next = 0;
    //third

    n3.ID = 3;
    n3.data = 789;
    n3.next = 0;

    LinkList linkList;

    linkList.AddNode(&n1);
    //add n2 to list and the position before n1

    linkList.AddNode(&n2);

    //add n3 behind node that id equal 2

    linkList.Insert(2,&n3);

    cout<<"The data:"<<linkList.Next(2)<<" behind the node that id equal 2"<<endl;


    for(NODE* p = linkList.GetHead(); p != 0; p = p->next)
    {
        cout<<"ID = "<<p->ID<<" "
            <<"Data= "<<p->data<<endl;
    }

    return 0;
}
```
