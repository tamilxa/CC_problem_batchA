//implement of stack using queue
import java.util.*;
public class  Main
{
    public static class stack
    {
    Queue<Integer>s1=new LinkedList<>(); 
     void push(int data)
    {
        s1.add(data);
        int size=s1.size();
        for(i=0;i<size;i++)
        {
        s1.add(s1.peek());
        s1.poll();
        }
    } 
    void pop()
    {
        if (!s1.isEmpty())
            s1.poll();
    }
   int top()
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
       stack q=new stack();
       q.push(1);
       q.push(2);
       q.push(3);
       q.push(4);
       q.pop();
       System.out.println(q.front());
       q.pop();
    System.out.println(q.front());
       System.out.println(q.size());
       
    }
}
