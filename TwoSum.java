class TwoSum {

	public static void main(String[] args){
		int[] a = {3,3};
		int[] b = twoSum(a,6);
		if(b != null){
			System.out.println(b[0]+" "+b[1]);
		}
		
	}
	
    public static int[] twoSum(int[] nums, int target) {
        int len = nums.length-2;
        int length = nums.length;
        for(int i =0; i<=len; i++){
			System.out.println("inside1"+i);
            for(int j=i+1; j<=length-1; j++){
				System.out.println("inside2"+j);
                if((nums[i]+nums[j]) == target){
                    int[] a = new int[2];
                    a[0]=i;
                    a[1]=j;
					return a;
                }
            }
        }
		return null;
    }
}