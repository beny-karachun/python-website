/**
 * Tester for EndOther - CodingBat Java
 * 14 test cases
 */
public class EndOtherTester {

    public static void main(String[] args) {
        EndOther obj = new EndOther();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.endOther("Hiabc", "abc") == true) {
            passed++;
        } else {
            System.out.println("FAIL: endOther(\"Hiabc\", \"abc\") expected true");
            failed++;
        }

        // Test 2
        if (obj.endOther("AbC", "HiaBc") == true) {
            passed++;
        } else {
            System.out.println("FAIL: endOther(\"AbC\", \"HiaBc\") expected true");
            failed++;
        }

        // Test 3
        if (obj.endOther("abc", "abXabc") == true) {
            passed++;
        } else {
            System.out.println("FAIL: endOther(\"abc\", \"abXabc\") expected true");
            failed++;
        }

        // Test 4
        if (obj.endOther("Hiabc", "abcd") == false) {
            passed++;
        } else {
            System.out.println("FAIL: endOther(\"Hiabc\", \"abcd\") expected false");
            failed++;
        }

        // Test 5
        if (obj.endOther("Hiabc", "bc") == true) {
            passed++;
        } else {
            System.out.println("FAIL: endOther(\"Hiabc\", \"bc\") expected true");
            failed++;
        }

        // Test 6
        if (obj.endOther("Hiabcx", "bc") == false) {
            passed++;
        } else {
            System.out.println("FAIL: endOther(\"Hiabcx\", \"bc\") expected false");
            failed++;
        }

        // Test 7
        if (obj.endOther("abc", "abc") == true) {
            passed++;
        } else {
            System.out.println("FAIL: endOther(\"abc\", \"abc\") expected true");
            failed++;
        }

        // Test 8
        if (obj.endOther("xyz", "12xyz") == true) {
            passed++;
        } else {
            System.out.println("FAIL: endOther(\"xyz\", \"12xyz\") expected true");
            failed++;
        }

        // Test 9
        if (obj.endOther("yz", "12xz") == false) {
            passed++;
        } else {
            System.out.println("FAIL: endOther(\"yz\", \"12xz\") expected false");
            failed++;
        }

        // Test 10
        if (obj.endOther("Z", "12xz") == true) {
            passed++;
        } else {
            System.out.println("FAIL: endOther(\"Z\", \"12xz\") expected true");
            failed++;
        }

        // Test 11
        if (obj.endOther("12", "12") == true) {
            passed++;
        } else {
            System.out.println("FAIL: endOther(\"12\", \"12\") expected true");
            failed++;
        }

        // Test 12
        if (obj.endOther("abcXYZ", "abcDEF") == false) {
            passed++;
        } else {
            System.out.println("FAIL: endOther(\"abcXYZ\", \"abcDEF\") expected false");
            failed++;
        }

        // Test 13
        if (obj.endOther("ab", "ab12") == false) {
            passed++;
        } else {
            System.out.println("FAIL: endOther(\"ab\", \"ab12\") expected false");
            failed++;
        }

        // Test 14
        if (obj.endOther("ab", "12ab") == true) {
            passed++;
        } else {
            System.out.println("FAIL: endOther(\"ab\", \"12ab\") expected true");
            failed++;
        }

        System.out.println("endOther: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}