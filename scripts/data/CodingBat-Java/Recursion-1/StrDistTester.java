/**
 * Tester for StrDist - CodingBat Java
 * 14 test cases
 */
public class StrDistTester {

    public static void main(String[] args) {
        StrDist obj = new StrDist();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.strDist("catcowcat", "cat") == 9) {
            passed++;
        } else {
            System.out.println("FAIL: strDist(\"catcowcat\", \"cat\") expected 9");
            failed++;
        }

        // Test 2
        if (obj.strDist("catcowcat", "cow") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: strDist(\"catcowcat\", \"cow\") expected 3");
            failed++;
        }

        // Test 3
        if (obj.strDist("cccatcowcatxx", "cat") == 9) {
            passed++;
        } else {
            System.out.println("FAIL: strDist(\"cccatcowcatxx\", \"cat\") expected 9");
            failed++;
        }

        // Test 4
        if (obj.strDist("abccatcowcatcatxyz", "cat") == 12) {
            passed++;
        } else {
            System.out.println("FAIL: strDist(\"abccatcowcatcatxyz\", \"cat\") expected 12");
            failed++;
        }

        // Test 5
        if (obj.strDist("xyx", "x") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: strDist(\"xyx\", \"x\") expected 3");
            failed++;
        }

        // Test 6
        if (obj.strDist("xyx", "y") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: strDist(\"xyx\", \"y\") expected 1");
            failed++;
        }

        // Test 7
        if (obj.strDist("xyx", "z") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: strDist(\"xyx\", \"z\") expected 0");
            failed++;
        }

        // Test 8
        if (obj.strDist("z", "z") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: strDist(\"z\", \"z\") expected 1");
            failed++;
        }

        // Test 9
        if (obj.strDist("x", "z") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: strDist(\"x\", \"z\") expected 0");
            failed++;
        }

        // Test 10
        if (obj.strDist("", "z") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: strDist(\"\", \"z\") expected 0");
            failed++;
        }

        // Test 11
        if (obj.strDist("hiHellohihihi", "hi") == 13) {
            passed++;
        } else {
            System.out.println("FAIL: strDist(\"hiHellohihihi\", \"hi\") expected 13");
            failed++;
        }

        // Test 12
        if (obj.strDist("hiHellohihihi", "hih") == 5) {
            passed++;
        } else {
            System.out.println("FAIL: strDist(\"hiHellohihihi\", \"hih\") expected 5");
            failed++;
        }

        // Test 13
        if (obj.strDist("hiHellohihihi", "o") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: strDist(\"hiHellohihihi\", \"o\") expected 1");
            failed++;
        }

        // Test 14
        if (obj.strDist("hiHellohihihi", "ll") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: strDist(\"hiHellohihihi\", \"ll\") expected 2");
            failed++;
        }

        System.out.println("strDist: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}