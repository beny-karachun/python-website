/**
 * Tester for CountHi - CodingBat Java
 * 11 test cases
 */
public class CountHiTester {

    public static void main(String[] args) {
        CountHi obj = new CountHi();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.countHi("xxhixx") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"xxhixx\") expected 1");
            failed++;
        }

        // Test 2
        if (obj.countHi("xhixhix") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"xhixhix\") expected 2");
            failed++;
        }

        // Test 3
        if (obj.countHi("hi") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"hi\") expected 1");
            failed++;
        }

        // Test 4
        if (obj.countHi("hihih") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"hihih\") expected 2");
            failed++;
        }

        // Test 5
        if (obj.countHi("h") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"h\") expected 0");
            failed++;
        }

        // Test 6
        if (obj.countHi("") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"\") expected 0");
            failed++;
        }

        // Test 7
        if (obj.countHi("ihihihihih") == 4) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"ihihihihih\") expected 4");
            failed++;
        }

        // Test 8
        if (obj.countHi("ihihihihihi") == 5) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"ihihihihihi\") expected 5");
            failed++;
        }

        // Test 9
        if (obj.countHi("hiAAhi12hi") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"hiAAhi12hi\") expected 3");
            failed++;
        }

        // Test 10
        if (obj.countHi("xhixhxihihhhih") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"xhixhxihihhhih\") expected 3");
            failed++;
        }

        // Test 11
        if (obj.countHi("ship") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countHi(\"ship\") expected 1");
            failed++;
        }

        System.out.println("countHi: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}