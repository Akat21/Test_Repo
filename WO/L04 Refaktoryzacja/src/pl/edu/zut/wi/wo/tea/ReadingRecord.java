package pl.edu.zut.wi.wo.tea;


public class ReadingRecord {
	String customer;
	int quantity;
	int month;
	int year;

	public static double firstMethod() {
		ReadingRecord aReading = acquireReading();
		double baseCharge = baseRate(aReading.month, aReading.year) * aReading.quantity;
		return baseCharge;
	}

	public static double secondMethod() {
		ReadingRecord aReading = acquireReading();
		double base = (baseRate(aReading.month, aReading.year) * aReading.quantity);
		double taxableCharge = Math.max(0, base - taxThreshold(aReading.year));
		return taxableCharge;
	}
	
	public static double thirdMethod() {
		ReadingRecord aReading = acquireReading();
		double basicChargeAmount = calculateBaseCharge(aReading);
		return basicChargeAmount;
	}

	private static double calculateBaseCharge(ReadingRecord aReading) {
		return baseRate(aReading.month, aReading.year) * aReading.quantity;
	}

	private static double taxThreshold(int year) {
		return 100;
	}

	private static double baseRate(int month, int year) {
		return 12.5;
	}

	private static ReadingRecord acquireReading() {
		ReadingRecord reading = new ReadingRecord();
		reading.customer = "ivan";
		reading.quantity = 10;
		reading.month = 2;
		reading.year = 2019;
		return reading;
	}
}
