package algorithms;

public class Utils {

	public static int[] generateRandomArray(int arraySize) {
		int[] randomArr;
		if (arraySize >= 1) {
			randomArr = new int[arraySize];
		} else {
			randomArr = new int[10];
		}
		for (int i = 0; i < arraySize; i++) {
			int min = 1;
			int max = 50;
			int randomNum = (int) (Math.random() * ((max - min) + 1)) + min;
			randomArr[i] = randomNum;
		}
		return randomArr;
	}

}
