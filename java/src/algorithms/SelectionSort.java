package algorithms;

public class SelectionSort {

	public static int[] selectionSort(int[] arr) {
		int temp = 0;
		for (int i = 0; i < arr.length - 1; i++) {
			for (int j = i + 1; j < arr.length; j++) {
				if (arr[j] < arr[i]) {
					temp = arr[i];
					arr[i] = arr[j];
					arr[j] = temp;
				}
			}
		}
		return arr;
	}

	public static void main(String[] args) {
		int[] unsortedArr = Utils.generateRandomArray(10);
		System.out.println("Unsorted Array: " + java.util.Arrays.toString(unsortedArr));
		int[] outputArr = SelectionSort.selectionSort(unsortedArr);
		System.out.println("Sorted Array: " + java.util.Arrays.toString(outputArr));
	}

}
