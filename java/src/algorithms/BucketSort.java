
package algorithms;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;

public class BucketSort {

	// Hashing algorithm to decide which elements gets placed into which bucket
	private static int hash(int i, int max, int numberOfBuckets) {
		return (int) ((double) i / max * (numberOfBuckets - 1));
	}

	// Determine the maximum integer in input list
	public static int findMax(List<Integer> input) {
		int m = Integer.MIN_VALUE;
		for (int i : input)
			m = Math.max(i, m);
		return m;
	}

	public static List<Integer> sort(List<Integer> list) {
		// Specify the number of bins as a square root of the input list size:
		final int numberOfBuckets = (int) Math.sqrt(list.size());
		List<List<Integer>> buckets = new ArrayList<>(numberOfBuckets);
		for (int i = 0; i < numberOfBuckets; i++) {
			buckets.add(new ArrayList<>());
		}

		// Distribute each element of input list into its relevant bucket using hash
		// method
		int max = findMax(list);
		for (int i : list) {
			buckets.get(hash(i, max, numberOfBuckets)).add(i);
		}

		// Using Comparator to sort items [Can also use Insertion sort]
		Comparator<Integer> comparator = Comparator.naturalOrder();
		for (List<Integer> bucket : buckets) {
			bucket.sort(comparator);
		}

		// Pull the buckets together to recreate the single list
		List<Integer> sortedArray = new LinkedList<>();
		for (List<Integer> bucket : buckets)
			sortedArray.addAll(bucket);

		return sortedArray;
	}

	public static void main(String[] args) {
		List<Integer> unsorted = Arrays.asList(80, 50, 60, 30, 20, 10, 70, 0, 40, 500, 600, 602, 200, 15);
		List<Integer> sorted = BucketSort.sort(unsorted);
		System.out.println(sorted.toString());
	}

}
