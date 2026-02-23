/**
 * Tester for StartHi - CodingBat Java
 * 8 test cases
 */
public class StartHiTester {

    public static void main(String[] args) {
        StartHi obj = new StartHi();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.startHi("hi there") == true) {
            passed++;
        } else {
            System.out.println("FAIL: startHi(\"hi there\") expected true");
            failed++;
        }

        // Test 2
        if (obj.startHi("hi") == true) {
            passed++;
        } else {
            System.out.println("FAIL: startHi(\"hi\") expected true");
            failed++;
        }

        // Test 3
        if (obj.startHi("hello hi") == false) {
            passed++;
        } else {
            System.out.println("FAIL: startHi(\"hello hi\") expected false");
            failed++;
        }

        // Test 4
        if (obj.startHi("he") == false) {
            passed++;
        } else {
            System.out.println("FAIL: startHi(\"he\") expected false");
            failed++;
        }

        // Test 5
        if (obj.startHi("h") == false) {
            passed++;
        } else {
            System.out.println("FAIL: startHi(\"h\") expected false");
            failed++;
        }

        // Test 6
        if (obj.startHi("") == false) {
            passed++;
        } else {
            System.out.println("FAIL: startHi(\"\") expected false");
            failed++;
        }

        // Test 7
        if (obj.startHi("ho hi") == false) {
            passed++;
        } else {
            System.out.println("FAIL: startHi(\"ho hi\") expected false");
            failed++;
        }

        // Test 8
        if (obj.startHi("hi ho") == true) {
            passed++;
        } else {
            System.out.println("FAIL: startHi(\"hi ho\") expected true");
            failed++;
        }

        System.out.println("startHi: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}