/**
 * Tester for ZipZap - CodingBat Java
 * 12 test cases
 */
public class ZipZapTester {

    public static void main(String[] args) {
        ZipZap obj = new ZipZap();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.zipZap("zipXzap").equals("zpXzp")) {
            passed++;
        } else {
            System.out.println("FAIL: zipZap(\"zipXzap\") expected \"zpXzp\"");
            failed++;
        }

        // Test 2
        if (obj.zipZap("zopzop").equals("zpzp")) {
            passed++;
        } else {
            System.out.println("FAIL: zipZap(\"zopzop\") expected \"zpzp\"");
            failed++;
        }

        // Test 3
        if (obj.zipZap("zzzopzop").equals("zzzpzp")) {
            passed++;
        } else {
            System.out.println("FAIL: zipZap(\"zzzopzop\") expected \"zzzpzp\"");
            failed++;
        }

        // Test 4
        if (obj.zipZap("zibzap").equals("zibzp")) {
            passed++;
        } else {
            System.out.println("FAIL: zipZap(\"zibzap\") expected \"zibzp\"");
            failed++;
        }

        // Test 5
        if (obj.zipZap("zip").equals("zp")) {
            passed++;
        } else {
            System.out.println("FAIL: zipZap(\"zip\") expected \"zp\"");
            failed++;
        }

        // Test 6
        if (obj.zipZap("zi").equals("zi")) {
            passed++;
        } else {
            System.out.println("FAIL: zipZap(\"zi\") expected \"zi\"");
            failed++;
        }

        // Test 7
        if (obj.zipZap("z").equals("z")) {
            passed++;
        } else {
            System.out.println("FAIL: zipZap(\"z\") expected \"z\"");
            failed++;
        }

        // Test 8
        if (obj.zipZap("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: zipZap(\"\") expected \"\"");
            failed++;
        }

        // Test 9
        if (obj.zipZap("zzp").equals("zp")) {
            passed++;
        } else {
            System.out.println("FAIL: zipZap(\"zzp\") expected \"zp\"");
            failed++;
        }

        // Test 10
        if (obj.zipZap("abcppp").equals("abcppp")) {
            passed++;
        } else {
            System.out.println("FAIL: zipZap(\"abcppp\") expected \"abcppp\"");
            failed++;
        }

        // Test 11
        if (obj.zipZap("azbcppp").equals("azbcppp")) {
            passed++;
        } else {
            System.out.println("FAIL: zipZap(\"azbcppp\") expected \"azbcppp\"");
            failed++;
        }

        // Test 12
        if (obj.zipZap("azbcpzpp").equals("azbcpzp")) {
            passed++;
        } else {
            System.out.println("FAIL: zipZap(\"azbcpzpp\") expected \"azbcpzp\"");
            failed++;
        }

        System.out.println("zipZap: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}