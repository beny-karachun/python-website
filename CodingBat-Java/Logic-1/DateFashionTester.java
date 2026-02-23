/**
 * Tester for DateFashion - CodingBat Java
 * 12 test cases
 */
public class DateFashionTester {

    public static void main(String[] args) {
        DateFashion obj = new DateFashion();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.dateFashion(5, 10) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: dateFashion(5, 10) expected 2");
            failed++;
        }

        // Test 2
        if (obj.dateFashion(5, 2) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: dateFashion(5, 2) expected 0");
            failed++;
        }

        // Test 3
        if (obj.dateFashion(5, 5) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: dateFashion(5, 5) expected 1");
            failed++;
        }

        // Test 4
        if (obj.dateFashion(3, 3) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: dateFashion(3, 3) expected 1");
            failed++;
        }

        // Test 5
        if (obj.dateFashion(10, 2) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: dateFashion(10, 2) expected 0");
            failed++;
        }

        // Test 6
        if (obj.dateFashion(2, 9) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: dateFashion(2, 9) expected 0");
            failed++;
        }

        // Test 7
        if (obj.dateFashion(9, 9) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: dateFashion(9, 9) expected 2");
            failed++;
        }

        // Test 8
        if (obj.dateFashion(10, 5) == 2) {
            passed++;
        } else {
            System.out.println("FAIL: dateFashion(10, 5) expected 2");
            failed++;
        }

        // Test 9
        if (obj.dateFashion(2, 2) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: dateFashion(2, 2) expected 0");
            failed++;
        }

        // Test 10
        if (obj.dateFashion(3, 7) == 1) {
            passed++;
        } else {
            System.out.println("FAIL: dateFashion(3, 7) expected 1");
            failed++;
        }

        // Test 11
        if (obj.dateFashion(2, 7) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: dateFashion(2, 7) expected 0");
            failed++;
        }

        // Test 12
        if (obj.dateFashion(6, 2) == 0) {
            passed++;
        } else {
            System.out.println("FAIL: dateFashion(6, 2) expected 0");
            failed++;
        }

        System.out.println("dateFashion: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}