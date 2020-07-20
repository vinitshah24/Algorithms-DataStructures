package algorithms;

public class MergeSort {

	public static int[] mergeSort(int[] arr) {
		// Base case for recursion
		if (arr.length <= 1) {
			return arr;
		}
		// Finding the midpoint to separate elements
		int midpoint = arr.length / 2;
		// Creating the array for left side
		int[] left = new int[midpoint];
		// Creating the array for right side
		int[] right;
		// If the right array is a even
		if (arr.length % 2 == 0) {
			right = new int[midpoint];
		}
		// If the right array is odd
		else {
			right = new int[midpoint + 1];
		}
		// Copy elements to right array left array
		for (int i = 0; i < midpoint; i++) {
			left[i] = arr[i];
		}
		// Copy elements to right array
		for (int j = 0; j < right.length; j++) {
			right[j] = arr[midpoint + j];
		}
		int[] result = new int[arr.length];
		// Recursively break down the left array
		left = mergeSort(left);
		// Recursively break down the right array
		right = mergeSort(right);
		// Merged left and right array
		result = merge(left, right);
		// Return the sorted merged array
		return result;
	}

	// Merge the left and right array in ascending order
	private static int[] merge(int[] left, int[] right) {
		// Merged result array
		int[] result = new int[left.length + right.length];
		// Declare and initialize pointers for all arrays
		int leftPointer, rightPointer, resultPointer;
		leftPointer = rightPointer = resultPointer = 0;
		// While there are items in either array
		while (leftPointer < left.length || rightPointer < right.length) {
			// If there are items in BOTH arrays
			if (leftPointer < left.length && rightPointer < right.length) {
				// If left item is less than right item
				if (left[leftPointer] < right[rightPointer]) {
					result[resultPointer++] = left[leftPointer++];
				} else {
					result[resultPointer++] = right[rightPointer++];
				}
			}
			// Items remaining in left array
			else if (leftPointer < left.length) {
				result[resultPointer++] = left[leftPointer++];
			}
			// Items remaining in right array
			else if (rightPointer < right.length) {
				result[resultPointer++] = right[rightPointer++];
			}
		}
		return result;
	}

	public static void main(String[] args) {
		int[] unsortedArr = Utils.generateRandomArray(10);
		System.out.println("Unsorted Array: " + java.util.Arrays.toString(unsortedArr));
		int[] outputArr = MergeSort.mergeSort(unsortedArr);
		System.out.println("Sorted Array: " + java.util.Arrays.toString(outputArr));
	}

}
