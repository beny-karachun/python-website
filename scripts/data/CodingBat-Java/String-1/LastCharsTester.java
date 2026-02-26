/**
 * Tester for LastChars - CodingBat Java
 * 9 test cases
 */
public class LastCharsTester {

    public static void main(String[] args) {
        LastChars obj = new LastChars();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.lastChars("last", "chars").equals("ls")) {
            passed++;
        } else {
            System.out.println("FAIL: lastChars(\"last\", \"chars\") expected \"ls\"");
            failed++;
        }

        // Test 2
        if (obj.lastChars("yo", "java").equals("ya")) {
            passed++;
        } else {
            System.out.println("FAIL: lastChars(\"yo\", \"java\") expected \"ya\"");
            failed++;
        }

        // Test 3
        if (obj.lastChars("hi", "").equals("h@")) {
            passed++;
        } else {
            System.out.println("FAIL: lastChars(\"hi\", \"\") expected \"h@\"");
            failed++;
        }

        // Test 4
        if (obj.lastChars("", "hello").equals("@o")) {
            passed++;
        } else {
            System.out.println("FAIL: lastChars(\"\", \"hello\") expected \"@o\"");
            failed++;
        }

        // Test 5
        if (obj.lastChars("", "").equals("@@")) {
            passed++;
        } else {
            System.out.println("FAIL: lastChars(\"\", \"\") expected \"@@\"");
            failed++;
        }

        // Test 6
        if (obj.lastChars("kitten", "hi").equals("ki")) {
            passed++;
        } else {
            System.out.println("FAIL: lastChars(\"kitten\", \"hi\") expected \"ki\"");
            failed++;
        }

        // Test 7
        if (obj.lastChars("k", "zip").equals("kp")) {
            passed++;
        } else {
            System.out.println("FAIL: lastChars(\"k\", \"zip\") expected \"kp\"");
            failed++;
        }

        // Test 8
        if (obj.lastChars("kitten", "").equals("k@")) {
            passed++;
        } else {
            System.out.println("FAIL: lastChars(\"kitten\", \"\") expected \"k@\"");
            failed++;
        }

        // Test 9
        if (obj.lastChars("kitten", "zip").equals("kp")) {
            passed++;
        } else {
            System.out.println("FAIL: lastChars(\"kitten\", \"zip\") expected \"kp\"");
            failed++;
        }

        System.out.println("lastChars: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}