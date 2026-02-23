/**
 * Tester for XyBalance - CodingBat Java
 * 18 test cases
 */
public class XyBalanceTester {

    public static void main(String[] args) {
        XyBalance obj = new XyBalance();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.xyBalance("aaxbby") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyBalance(\"aaxbby\") expected true");
            failed++;
        }

        // Test 2
        if (obj.xyBalance("aaxbb") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyBalance(\"aaxbb\") expected false");
            failed++;
        }

        // Test 3
        if (obj.xyBalance("yaaxbb") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyBalance(\"yaaxbb\") expected false");
            failed++;
        }

        // Test 4
        if (obj.xyBalance("yaaxbby") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyBalance(\"yaaxbby\") expected true");
            failed++;
        }

        // Test 5
        if (obj.xyBalance("xaxxbby") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyBalance(\"xaxxbby\") expected true");
            failed++;
        }

        // Test 6
        if (obj.xyBalance("xaxxbbyx") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyBalance(\"xaxxbbyx\") expected false");
            failed++;
        }

        // Test 7
        if (obj.xyBalance("xxbxy") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyBalance(\"xxbxy\") expected true");
            failed++;
        }

        // Test 8
        if (obj.xyBalance("xxbx") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyBalance(\"xxbx\") expected false");
            failed++;
        }

        // Test 9
        if (obj.xyBalance("bbb") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyBalance(\"bbb\") expected true");
            failed++;
        }

        // Test 10
        if (obj.xyBalance("bxbb") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyBalance(\"bxbb\") expected false");
            failed++;
        }

        // Test 11
        if (obj.xyBalance("bxyb") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyBalance(\"bxyb\") expected true");
            failed++;
        }

        // Test 12
        if (obj.xyBalance("xy") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyBalance(\"xy\") expected true");
            failed++;
        }

        // Test 13
        if (obj.xyBalance("y") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyBalance(\"y\") expected true");
            failed++;
        }

        // Test 14
        if (obj.xyBalance("x") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyBalance(\"x\") expected false");
            failed++;
        }

        // Test 15
        if (obj.xyBalance("") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyBalance(\"\") expected true");
            failed++;
        }

        // Test 16
        if (obj.xyBalance("yxyxyxyx") == false) {
            passed++;
        } else {
            System.out.println("FAIL: xyBalance(\"yxyxyxyx\") expected false");
            failed++;
        }

        // Test 17
        if (obj.xyBalance("yxyxyxyxy") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyBalance(\"yxyxyxyxy\") expected true");
            failed++;
        }

        // Test 18
        if (obj.xyBalance("12xabxxydxyxyzz") == true) {
            passed++;
        } else {
            System.out.println("FAIL: xyBalance(\"12xabxxydxyxyzz\") expected true");
            failed++;
        }

        System.out.println("xyBalance: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}