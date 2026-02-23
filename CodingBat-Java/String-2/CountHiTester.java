/**
 * Tester for CountHi - CodingBat Java
 * 9 test cases
 */
public class CountHiTester {

    public static void main(String[] args) {
        CountHi obj = new CountHi();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.countHi("abc hi ho") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"abc hi ho\") expected 1");
            failed++;
        }

        // Test 2
        if (obj.countHi("ABChi hi") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"ABChi hi\") expected 2");
            failed++;
        }

        // Test 3
        if (obj.countHi("hihi") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"hihi\") expected 2");
            failed++;
        }

        // Test 4
        if (obj.countHi("hiHIhi") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"hiHIhi\") expected 2");
            failed++;
        }

        // Test 5
        if (obj.countHi("") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"\") expected 0");
            failed++;
        }

        // Test 6
        if (obj.countHi("h") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"h\") expected 0");
            failed++;
        }

        // Test 7
        if (obj.countHi("hi") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"hi\") expected 1");
            failed++;
        }

        // Test 8
        if (obj.countHi("Hi is no HI on ahI") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"Hi is no HI on ahI\") expected 0");
            failed++;
        }

        // Test 9
        if (obj.countHi("hiho not HOHIhi") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"hiho not HOHIhi\") expected 2");
            failed++;
        }

        System.out.println("countHi: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}