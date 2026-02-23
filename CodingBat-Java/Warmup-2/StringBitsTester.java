/**
 * Tester for StringBits - CodingBat Java
 * 10 test cases
 */
public class StringBitsTester {

    public static void main(String[] args) {
        StringBits obj = new StringBits();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.stringBits("Hello").equals("Hlo")) {
            passed++;
        } else {
            System.out.println("FAIL: stringBits(\"Hello\") expected \"Hlo\"");
            failed++;
        }

        // Test 2
        if (obj.stringBits("Hi").equals("H")) {
            passed++;
        } else {
            System.out.println("FAIL: stringBits(\"Hi\") expected \"H\"");
            failed++;
        }

        // Test 3
        if (obj.stringBits("Heeololeo").equals("Hello")) {
            passed++;
        } else {
            System.out.println("FAIL: stringBits(\"Heeololeo\") expected \"Hello\"");
            failed++;
        }

        // Test 4
        if (obj.stringBits("HiHiHi").equals("HHH")) {
            passed++;
        } else {
            System.out.println("FAIL: stringBits(\"HiHiHi\") expected \"HHH\"");
            failed++;
        }

        // Test 5
        if (obj.stringBits("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: stringBits(\"\") expected \"\"");
            failed++;
        }

        // Test 6
        if (obj.stringBits("Greetings").equals("Getns")) {
            passed++;
        } else {
            System.out.println("FAIL: stringBits(\"Greetings\") expected \"Getns\"");
            failed++;
        }

        // Test 7
        if (obj.stringBits("Chocoate").equals("Coot")) {
            passed++;
        } else {
            System.out.println("FAIL: stringBits(\"Chocoate\") expected \"Coot\"");
            failed++;
        }

        // Test 8
        if (obj.stringBits("pi").equals("p")) {
            passed++;
        } else {
            System.out.println("FAIL: stringBits(\"pi\") expected \"p\"");
            failed++;
        }

        // Test 9
        if (obj.stringBits("Hello Kitten").equals("HloKte")) {
            passed++;
        } else {
            System.out.println("FAIL: stringBits(\"Hello Kitten\") expected \"HloKte\"");
            failed++;
        }

        // Test 10
        if (obj.stringBits("hxaxpxpxy").equals("happy")) {
            passed++;
        } else {
            System.out.println("FAIL: stringBits(\"hxaxpxpxy\") expected \"happy\"");
            failed++;
        }

        System.out.println("stringBits: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}