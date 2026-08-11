//Insertfirst,last
import java.util.*;
public class  Main 
{
    static class  Node 
    {
        int data;
        Node next;
        Node(int data)
        {
            this.data=data;
            this.next=null;
        }
    }
    Node head;
    void insertfirst(int data)
    {
        Node newNode=new Node(data);
        newNode.next=head;
        head=newNode;
    }
    void insertlast(int data)
    {
         Node newNode=new Node(data);
         Node currNode =head;
         if(head==null)
         {
             return;
         }
         while(currNode.next!=null)
         {
            currNode=currNode.next;
            
         }
         currNode.next=newNode;
    }
    void display()
    {
        Node currNode=head;
        while(currNode!=null)
         {
            System.out.println(currNode.data + " ");
            currNode=currNode.next;
            
         }
    }
    void deletefirst()
    {
        if(head==null)
        return;
        head=head.next;
    }
    void deletelast()
    {
      Node currNode =head;
      Node prev=null;
         if(head==null)
         {
             
             return;
         }
         while(currNode.next!=null)
         {
             prev=currNode;
            currNode=currNode.next;
            
         }  
         prev.next=null;
    }
        
    
    public static void main(String[]args)
    {
      Main m=new Main();
      m.insertfirst(2);
      m.insertfirst(3);
      m.insertlast(8);
      m.insertfirst(6);
      m.insertlast(20);
      m.insertlast(24);
      m.deletefirst();
      m.deletelast();
      m.display();
    }
}