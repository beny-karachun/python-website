/**
 * Tester for MakeAbba - CodingBat Java
 * 9 test cases
 */
public class MakeAbbaTester {

    public static void main(String[] args) {
        MakeAbba obj = new MakeAbba();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.makeAbba("Hi", "Bye").equals("HiByeByeHi")) {
            passed++;
        } else {
            System.out.println("FAIL: makeAbba(\"Hi\", \"Bye\") expected \"HiByeByeHi\"");
            failed++;
        }

        // Test 2
        if (obj.makeAbba("Yo", "Alice").equals("YoAliceAliceYo")) {
            passed++;
        } else {
            System.out.println("FAIL: makeAbba(\"Yo\", \"Alice\") expected \"YoAliceAliceYo\"");
            failed++;
        }

        // Test 3
        if (obj.makeAbba("What", "Up").equals("WhatUpUpWhat")) {
            passed++;
        } else {
            System.out.println("FAIL: makeAbba(\"What\", \"Up\") expected \"WhatUpUpWhat\"");
            failed++;
        }

        // Test 4
        if (obj.makeAbba("aaa", "bbb").equals("aaabbbbbbaaa")) {
            passed++;
        } else {
            System.out.println("FAIL: makeAbba(\"aaa\", \"bbb\") expected \"aaabbbbbbaaa\"");
            failed++;
        }

        // Test 5
        if (obj.makeAbba("x", "y").equals("xyyx")) {
            passed++;
        } else {
            System.out.println("FAIL: makeAbba(\"x\", \"y\") expected \"xyyx\"");
            failed++;
        }

        // Test 6
        if (obj.makeAbba("x", "").equals("xx")) {
            passed++;
        } else {
            System.out.println("FAIL: makeAbba(\"x\", \"\") expected \"xx\"");
            failed++;
        }

        // Test 7
        if (obj.makeAbba("", "y").equals("yy")) {
            passed++;
        } else {
            System.out.println("FAIL: makeAbba(\"\", \"y\") expected \"yy\"");
            failed++;
        }

        // Test 8
        if (obj.makeAbba("Bo", "Ya").equals("BoYaYaBo")) {
            passed++;
        } else {
            System.out.println("FAIL: makeAbba(\"Bo\", \"Ya\") expected \"BoYaYaBo\"");
            failed++;
        }

        // Test 9
        if (obj.makeAbba("Ya", "Ya").equals("YaYaYaYa")) {
            passed++;
        } else {
            System.out.println("FAIL: makeAbba(\"Ya\", \"Ya\") expected \"YaYaYaYa\"");
            failed++;
        }

        System.out.println("makeAbba: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}