package algorithms;

public class QuickSort {

	public static int partition(int arr[], int left, int right) {
		int pivot = arr[(left + right) / 2]; // Pick a pivot point. Can be an element.
		while (left <= right) { // Until we've gone through the whole array
			// Find element on left that should be on right
			while (arr[left] < pivot) {
				left++;
			}
			// Find element on right that should be on left
			while (arr[right] > pivot) {
				right--;
			}
			// Swap elements, and move left and right indices
			if (left <= right) {
				int tmp = arr[left];
				arr[left] = arr[right];
				arr[right] = tmp;
				left++;
				right--;
			}
		}
		return left;
	}

	public static void quickSort(int arr[], int left, int right) {
		int index = partition(arr, left, right);
		if (left < index - 1) { // Sort left half
			quickSort(arr, left, index - 1);
		}
		if (index < right) { // Sort right half
			quickSort(arr, index, right);
		}
	}

	public static void main(String[] args) {
		int[] array = Utils.generateRandomArray(10);
		System.out.println("Unsorted Array: " + java.util.Arrays.toString(array));
		QuickSort.quickSort(array, 0, array.length - 1);
		System.out.println("Sorted Array: " + java.util.Arrays.toString(array));
	}

}