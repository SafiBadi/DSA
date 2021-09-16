import java.util.*;

public class HelloWorld{
    public static void main(String args[]){
        
        Scanner input = new Scanner(System.in);
        
        int n = input.nextInt(); 
        int []arr = new int[n];
        
        for(int i =0; i<n; i++){
            arr[i] = input.nextInt();
        }
        
        arr = selectionsort(arr);
        
        System.out.println("Number of elements in Array: " + n );
        System.out.println("Sorted Array using Selection Sort: \n");
        
        for(int k = 0; k<arr.length; k++){
            System.out.print(arr[k] + " ");
        }
        
    }
     
    static int[] selectionsort(int[] arr){
        
        int minindex,pointer=0,temp,i,j;
        
        for(i = 0; i<arr.length; i++){
            minindex = pointer;
            
            for (j = pointer; j<arr.length; j++){
                if (arr[j] < arr[minindex]){
                    minindex = j;
                }
            }
            j--;
            
            temp = arr[pointer];
            arr[pointer] = arr[minindex];
            arr[minindex] = temp;
            pointer ++;
            
        }

        return arr;
    }
}