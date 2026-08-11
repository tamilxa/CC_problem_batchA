import java.util.*;
public class  Main 
{
    public static void main (String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int n,i;
        n=sc.nextInt();
        int arr[]=new int[n];
        for(i=0;i<n;i++)
        arr[i]=sc.nextInt();
        int currsum=arr[0],maxsum=arr[0];
        for(i=1;i<n;i++)
        {
            currsum=Math.max(arr[i],currsum+arr[i]);
            maxsum=Math.max(currsum,maxsum);
        }
        System.out.print(maxsum);
    }
}