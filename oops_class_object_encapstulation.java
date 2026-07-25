import java.util.*;
class operations
{
    static int add(int a,int b)
    {
        return a+b;
    }
}
class operation
{
    static int sub(int a,int b)
    {
        return a-b;
    }
}
public class Main
{
	public static void main(String[] args) {
	    operation op=new operation();
	    operations ops=new operations();
	    Scanner sc=new Scanner(System.in);
	    System.out.println(op.sub(sc.nextInt(),sc.nextInt()));
	    System.out.println(ops.add(sc.nextInt(),sc.nextInt()));
	    
	}
}
