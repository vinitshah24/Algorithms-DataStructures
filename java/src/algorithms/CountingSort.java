package algorithms;

import java.util.Arrays;

public class CountingSort {

	// Example array -> { 4, 3, 2, 5, 4, 3, 5, 1, 0, 2, 5 }
	// Returned array -> { 1, 2, 4, 6, 8, 11 }
	static int[] countElements(int[] input, int highestElement) {

		// Create an array to fill the count of all the elements
		int[] arrayWithCount = new int[highestElement + 1];
		Arrays.fill(arrayWithCount, 0);

		// Store the elements count in the array
		for (int i : input) {
			arrayWithCount[i] += 1;
		}

		// Add the value of previous element with current element
		for (int i = 1; i < arrayWithCount.length; i++) {
			arrayWithCount[i] += arrayWithCount[i - 1];
		}

		return arrayWithCount;
	}

	static int[] sort(int[] input, int highestElement) {

		// Get the count array
		int[] countArray = countElements(input, highestElement);

		// Create the output array
		int[] sortedArray = new int[input.length];

		// Fill the output array by starting from end of inputArray
		for (int i = input.length - 1; i >= 0; i--) {

			// Get the value of element to fill
			int current = input[i];

			// Subtract 1 from the count array to add to correct location
			sortedArray[countArray[current] - 1] = current;

			// Reduce the count from the count array
			countArray[current] -= 1;
		}
		return sortedArray;
	}

	public static void main(String[] args) {
		int[] input = { 4, 3, 2, 5, 4, 3, 5, 1, 0, 2, 5 };
		int highestElement = 5;
		int[] sortedArr = CountingSort.sort(input, highestElement);
		System.out.println(java.util.Arrays.toString(sortedArr));

	}

}
