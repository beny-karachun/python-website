/**
 * Tester for SumDigits - CodingBat Java
 * 9 test cases
 */
public class SumDigitsTester {

    public static void main(String[] args) {
        SumDigits obj = new SumDigits();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.sumDigits("aa1bc2d3") == 6) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(\"aa1bc2d3\") expected 6");
            failed++;
        }

        // Test 2
        if (obj.sumDigits("aa11b33") == 8) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(\"aa11b33\") expected 8");
            failed++;
        }

        // Test 3
        if (obj.sumDigits("Chocolate") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(\"Chocolate\") expected 0");
            failed++;
        }

        // Test 4
        if (obj.sumDigits("5hoco1a1e") == 7) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(\"5hoco1a1e\") expected 7");
            failed++;
        }

        // Test 5
        if (obj.sumDigits("123abc123") == 12) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(\"123abc123\") expected 12");
            failed++;
        }

        // Test 6
        if (obj.sumDigits("") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(\"\") expected 0");
            failed++;
        }

        // Test 7
        if (obj.sumDigits("Hello") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(\"Hello\") expected 0");
            failed++;
        }

        // Test 8
        if (obj.sumDigits("X1z9b2") == 12) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(\"X1z9b2\") expected 12");
            failed++;
        }

        // Test 9
        if (obj.sumDigits("5432a") == 14) {
            passed++;
        } else {
            System.out.println("FAIL: sumDigits(\"5432a\") expected 14");
            failed++;
        }

        System.out.println("sumDigits: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}