import java.util.*;
public class  Main
{
    public static class queue
    {
    Stack<Integer>s1=new Stack<>(); 
    Stack<Integer>s2=new Stack<>();
     void enqueue(int data)
    {
        while(!s1.isEmpty())
        {
        s2.push(s1.pop());
        }
        s1.push(data);
        while(!s2.isEmpty())
        {
            s1.push(s2.pop());
        }
        
    } 
    void dequeue()
    {
        if (!s1.isEmpty())
            s1.pop();
    }
   int front()
    {
      if (!s1.isEmpty())
      
          return s1.peek();
          return 0 ;
    }
    int size()
    {
        return s1.size();
    }
    }
    public static void main(String[]args)
    {
       queue q=new queue();
       q.enqueue(1);
       q.enqueue(2);
       q.enqueue(3);
       q.dequeue();
       System.out.println(q.front());
       q.dequeue();
    System.out.println(q.front());
       System.out.println(q.size());
       
    }
}
