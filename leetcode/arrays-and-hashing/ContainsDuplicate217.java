import java.util.HashSet;

public class ContainsDuplicate217 {
  public static void main(String[] args) {
    int[] numbs = {1,2,3,1}; 
    int[] numbs2 = {1,2,3,4}; 
    int[] numbs3 = {1,1,1,3,3,4,3,2,4,2}; 
    
    System.out.println(containsDuplicate(numbs));
    System.out.println(containsDuplicate(numbs2));
    System.out.println(containsDuplicate(numbs3));
  }

  private static boolean  containsDuplicate(int[] nums) {
    HashSet<Integer> hashset = new HashSet<>();
    
    for (int i=0; i<nums.length; i++){
      if(hashset.contains(nums[i])) return true;
      hashset.add(nums[i]);
    }
    return false;
  }  
}