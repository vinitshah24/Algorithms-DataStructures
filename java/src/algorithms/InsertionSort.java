package algorithms;

public class InsertionSort {

	public static int[] insertionSort(int[] arr) {

		int temp, j = 0;
		for (int i = 1; i < arr.length; i++) {
			temp = arr[i];
			j = i;
			while (j > 0 && arr[j - 1] > temp) {
				arr[j] = arr[j - 1];
				j--;
			}
			arr[j] = temp;
		}
		return arr;
	}

	public static void main(String[] args) {
		int[] unsortedArr = Utils.generateRandomArray(10);
		System.out.println("Unsorted Array: " + java.util.Arrays.toString(unsortedArr));
		int[] outputArr = InsertionSort.insertionSort(unsortedArr);
		System.out.println("Sorted Array: " + java.util.Arrays.toString(outputArr));
	}
}
