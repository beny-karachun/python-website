/**
 * Tester for OneTwo - CodingBat Java
 * 16 test cases
 */
public class OneTwoTester {

    public static void main(String[] args) {
        OneTwo obj = new OneTwo();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.oneTwo("abc").equals("bca")) {
            passed++;
        } else {
            System.out.println("FAIL: oneTwo(\"abc\") expected \"bca\"");
            failed++;
        }

        // Test 2
        if (obj.oneTwo("tca").equals("cat")) {
            passed++;
        } else {
            System.out.println("FAIL: oneTwo(\"tca\") expected \"cat\"");
            failed++;
        }

        // Test 3
        if (obj.oneTwo("tcagdo").equals("catdog")) {
            passed++;
        } else {
            System.out.println("FAIL: oneTwo(\"tcagdo\") expected \"catdog\"");
            failed++;
        }

        // Test 4
        if (obj.oneTwo("chocolate").equals("hocolctea")) {
            passed++;
        } else {
            System.out.println("FAIL: oneTwo(\"chocolate\") expected \"hocolctea\"");
            failed++;
        }

        // Test 5
        if (obj.oneTwo("1234567890").equals("231564897")) {
            passed++;
        } else {
            System.out.println("FAIL: oneTwo(\"1234567890\") expected \"231564897\"");
            failed++;
        }

        // Test 6
        if (obj.oneTwo("xabxabxabxabxabxabxab").equals("abxabxabxabxabxabxabx")) {
            passed++;
        } else {
            System.out.println("FAIL: oneTwo(\"xabxabxabxabxabxabxab\") expected \"abxabxabxabxabxabxabx\"");
            failed++;
        }

        // Test 7
        if (obj.oneTwo("abcdefx").equals("bcaefd")) {
            passed++;
        } else {
            System.out.println("FAIL: oneTwo(\"abcdefx\") expected \"bcaefd\"");
            failed++;
        }

        // Test 8
        if (obj.oneTwo("abcdefxy").equals("bcaefd")) {
            passed++;
        } else {
            System.out.println("FAIL: oneTwo(\"abcdefxy\") expected \"bcaefd\"");
            failed++;
        }

        // Test 9
        if (obj.oneTwo("abcdefxyz").equals("bcaefdyzx")) {
            passed++;
        } else {
            System.out.println("FAIL: oneTwo(\"abcdefxyz\") expected \"bcaefdyzx\"");
            failed++;
        }

        // Test 10
        if (obj.oneTwo("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: oneTwo(\"\") expected \"\"");
            failed++;
        }

        // Test 11
        if (obj.oneTwo("x").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: oneTwo(\"x\") expected \"\"");
            failed++;
        }

        // Test 12
        if (obj.oneTwo("xy").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: oneTwo(\"xy\") expected \"\"");
            failed++;
        }

        // Test 13
        if (obj.oneTwo("xyz").equals("yzx")) {
            passed++;
        } else {
            System.out.println("FAIL: oneTwo(\"xyz\") expected \"yzx\"");
            failed++;
        }

        // Test 14
        if (obj.oneTwo("abcdefghijklkmnopqrstuvwxyz1234567890").equals("bcaefdhigkljmnkpqostrvwuyzx231564897")) {
            passed++;
        } else {
            System.out.println("FAIL: oneTwo(\"abcdefghijklkmnopqrstuvwxyz1234567890\") expected \"bcaefdhigkljmnkpqostrvwuyzx231564897\"");
            failed++;
        }

        // Test 15
        if (obj.oneTwo("abcdefghijklkmnopqrstuvwxyz123456789").equals("bcaefdhigkljmnkpqostrvwuyzx231564897")) {
            passed++;
        } else {
            System.out.println("FAIL: oneTwo(\"abcdefghijklkmnopqrstuvwxyz123456789\") expected \"bcaefdhigkljmnkpqostrvwuyzx231564897\"");
            failed++;
        }

        // Test 16
        if (obj.oneTwo("abcdefghijklkmnopqrstuvwxyz12345678").equals("bcaefdhigkljmnkpqostrvwuyzx231564")) {
            passed++;
        } else {
            System.out.println("FAIL: oneTwo(\"abcdefghijklkmnopqrstuvwxyz12345678\") expected \"bcaefdhigkljmnkpqostrvwuyzx231564\"");
            failed++;
        }

        System.out.println("oneTwo: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}