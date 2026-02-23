/**
 * Tester for EndX - CodingBat Java
 * 12 test cases
 */
public class EndXTester {

    public static void main(String[] args) {
        EndX obj = new EndX();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.endX("xxre").equals("rexx")) {
            passed++;
        } else {
            System.out.println("FAIL: endX(\"xxre\") expected \"rexx\"");
            failed++;
        }

        // Test 2
        if (obj.endX("xxhixx").equals("hixxxx")) {
            passed++;
        } else {
            System.out.println("FAIL: endX(\"xxhixx\") expected \"hixxxx\"");
            failed++;
        }

        // Test 3
        if (obj.endX("xhixhix").equals("hihixxx")) {
            passed++;
        } else {
            System.out.println("FAIL: endX(\"xhixhix\") expected \"hihixxx\"");
            failed++;
        }

        // Test 4
        if (obj.endX("hiy").equals("hiy")) {
            passed++;
        } else {
            System.out.println("FAIL: endX(\"hiy\") expected \"hiy\"");
            failed++;
        }

        // Test 5
        if (obj.endX("h").equals("h")) {
            passed++;
        } else {
            System.out.println("FAIL: endX(\"h\") expected \"h\"");
            failed++;
        }

        // Test 6
        if (obj.endX("x").equals("x")) {
            passed++;
        } else {
            System.out.println("FAIL: endX(\"x\") expected \"x\"");
            failed++;
        }

        // Test 7
        if (obj.endX("xx").equals("xx")) {
            passed++;
        } else {
            System.out.println("FAIL: endX(\"xx\") expected \"xx\"");
            failed++;
        }

        // Test 8
        if (obj.endX("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: endX(\"\") expected \"\"");
            failed++;
        }

        // Test 9
        if (obj.endX("bxx").equals("bxx")) {
            passed++;
        } else {
            System.out.println("FAIL: endX(\"bxx\") expected \"bxx\"");
            failed++;
        }

        // Test 10
        if (obj.endX("bxax").equals("baxx")) {
            passed++;
        } else {
            System.out.println("FAIL: endX(\"bxax\") expected \"baxx\"");
            failed++;
        }

        // Test 11
        if (obj.endX("axaxax").equals("aaaxxx")) {
            passed++;
        } else {
            System.out.println("FAIL: endX(\"axaxax\") expected \"aaaxxx\"");
            failed++;
        }

        // Test 12
        if (obj.endX("xxhxi").equals("hixxx")) {
            passed++;
        } else {
            System.out.println("FAIL: endX(\"xxhxi\") expected \"hixxx\"");
            failed++;
        }

        System.out.println("endX: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}