package algorithms;

public class BubbleSort {

	public static int[] bubbleSort(int[] arr) {
		int temp = 0;
		for (int i = arr.length - 1; i > 0; i--) {
			for (int j = 0; j < i; i++) {
				if (arr[j + 1] < arr[j]) {
					temp = arr[j];
					arr[j] = arr[j + 1];
					arr[j + 1] = temp;
				}
			}
		}
		return arr;
	}

	public static int[] bubbleSort2(int[] arr) {
		int temp = 0;
		for (int i = 0; i < arr.length - 1; i++) {
			for (int j = 0; j < arr.length - i - 1; j++) {
				if (arr[j + 1] < arr[j]) {
					temp = arr[j];
					arr[j] = arr[j + 1];
					arr[j + 1] = temp;
				}
			}
		}
		return arr;
	}

	public static void main(String[] args) {
		int[] unsortedArr = Utils.generateRandomArray(10);
		System.out.println("Unsorted Array: " + java.util.Arrays.toString(unsortedArr));
		int[] outputArr = BubbleSort.bubbleSort(unsortedArr);
		System.out.println("Sorted Array: " + java.util.Arrays.toString(outputArr));
	}
}
