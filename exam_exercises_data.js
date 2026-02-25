// Auto-generated Exam Exercises data
const EXERCISES_DATA = {
    "categories": [
        {
            "name": "תבניות רקורסיה",
            "problems": [
                {
                    "id": "subset_count",
                    "name": "כמות דרכים (Subset Sum)",
                    "description": "כתבו פונקציה `count_ways(lst, summ)` המקבלת רשימת מספרים `lst` וסכום יעד `summ`. על הפונקציה להחזיר את מספר הדרכים השונות לבחור תת-קבוצה מתוך הרשימה שסכומה שווה בדיוק ל-`summ`.\n\n**הנחיות:**\n- חובה להשתמש ברקורסיה.\n- מותר להניח שכל המספרים חיוביים.",
                    "stub": "def count_ways(lst, summ):\n    # TODO: implement recursive solution\n    pass\n",
                    "tests": [
                        { "call": "count_ways([1, 5, 3, 2, 6, 8, 3], 9)", "expected": "4" },
                        { "call": "count_ways([1, 2, 3], 3)", "expected": "2" },
                        { "call": "count_ways([1, 2], 5)", "expected": "0" }
                    ]
                },
                {
                    "id": "subset_max",
                    "name": "מקסימום פריטים (Max Fit)",
                    "description": "כתבו פונקציה `max_items(lst, summ)` המקבלת רשימת מספרים וסכום יעד. הפונקציה תחזיר את **המספר המקסימלי** של איברים שניתן לקחת מהרשימה כך שסכומם יהיה שווה בדיוק ליעד.\n\nאם לא קיימת שום תת-קבוצה שסכומה מתאים, החזירו `-1`.",
                    "stub": "def max_items(lst, summ):\n    # TODO: implement recursive solution\n    pass\n",
                    "tests": [
                        { "call": "max_items([1, 5, 3, 2, 6, 8, 3], 9)", "expected": "3" },
                        { "call": "max_items([4, 5], 10)", "expected": "-1" },
                        { "call": "max_items([1, 1, 1, 1], 2)", "expected": "2" }
                    ]
                },
                {
                    "id": "subset_bool",
                    "name": "האם אפשרי (Bool)",
                    "description": "כתבו פונקציה `is_possible(lst, summ)` המחזירה `True` אם ניתן לבחור תת-קבוצה מהרשימה שסכומה שווה בדיוק ל-`summ`, ו-`False` אחרת.",
                    "stub": "def is_possible(lst, summ):\n    # TODO: implement recursive solution\n    pass\n",
                    "tests": [
                        { "call": "is_possible([1, 5, 3, 2, 6, 8, 3], 8)", "expected": "True" },
                        { "call": "is_possible([1, 5, 3, 2, 6, 8, 3], 135)", "expected": "False" },
                        { "call": "is_possible([10, 20], 30)", "expected": "True" }
                    ]
                },
                {
                    "id": "subset_closest",
                    "name": "סכום הכי קרוב מתחת למקסימום",
                    "description": "כתבו פונקציה `closest_sum(lst, max_val, value=0)` המחזירה את הסכום הגדול ביותר שניתן להרכיב מהרשימה אשר **אינו עולה** על `max_val`.",
                    "stub": "def closest_sum(lst, max_val, value=0):\n    # TODO: implement recursive solution\n    pass\n",
                    "tests": [
                        { "call": "closest_sum([5, 3, 9, 4], 11)", "expected": "9" },
                        { "call": "closest_sum([1, 2, 3], 10)", "expected": "6" },
                        { "call": "closest_sum([10, 20], 5)", "expected": "0" }
                    ]
                }
            ]
        },
        {
            "name": "אלגוריתמי מיון",
            "problems": [
                {
                    "id": "bucket_sort",
                    "name": "Bucket Sort (Histogram)",
                    "description": "ממשו את פונקציית `bucket_sort(lst, max_val)` אשר מקבלת רשימת מספרים שלמים חיוביים (ו-0) ואת הערך המקסימלי האפשרי `max_val`, וממיינת את הרשימה באמצעות שיטת מערך מונים (היסטוגרמה). הפונקציה צריכה להחזיר רשימה ממוינת חדשה.\n\n**זמן ריצה נדרש: O(n)**",
                    "stub": "def bucket_sort(lst, max_val):\n    # TODO: implement array counting approach\n    pass\n",
                    "tests": [
                        { "call": "bucket_sort([4, 2, 2, 8, 3, 3, 1], 8)", "expected": "[1, 2, 2, 3, 3, 4, 8]" },
                        { "call": "bucket_sort([0, 1, 0, 1], 1)", "expected": "[0, 0, 1, 1]" }
                    ]
                },
                {
                    "id": "bubble_sort",
                    "name": "Bubble Sort",
                    "description": "כתבו פונקציה `bubble_sort(lst)` הממיינת את הרשימה במקום (in-place) על ידי בעבוע האיבר הגדול ביותר לסוף המערך בכל איטרציה. החזירו את הרשימה.",
                    "stub": "def bubble_sort(lst):\n    # TODO: implement\n    pass\n",
                    "tests": [
                        { "call": "bubble_sort([64, 34, 25, 12, 22, 11, 90])", "expected": "[11, 12, 22, 25, 34, 64, 90]" },
                        { "call": "bubble_sort([3, 2, 1])", "expected": "[1, 2, 3]" }
                    ]
                }
            ]
        },
        {
            "name": "אלגוריתמי חיפוש",
            "problems": [
                {
                    "id": "binary_search",
                    "name": "Binary Search (Iterative)",
                    "description": "כתבו פונקציה `binary_search(lst, target)` המקבלת רשימת מספרים ממוינת `lst` ומספר יעד `target`. הפונקציה תבצע חיפוש בינארי בלולאה (איטרטיבי) ותחזיר את ה**אינדקס** של יעד. אם הוא לא קיים, יוחזר `-1`.",
                    "stub": "def binary_search(lst, target):\n    # TODO: implement iterative binary search\n    pass\n",
                    "tests": [
                        { "call": "binary_search([2, 3, 4, 10, 40], 10)", "expected": "3" },
                        { "call": "binary_search([2, 3, 4, 10, 40], 5)", "expected": "-1" }
                    ]
                },
                {
                    "id": "binary_search_rec",
                    "name": "Binary Search (Recursive)",
                    "description": "כתבו פונקציה `binary_search_rec(lst, target, low, high)` המבצעת את אותו חיפוש בינארי על המערך הממוין, אך הפעם בגישה **רקורסיבית**.",
                    "stub": "def binary_search_rec(lst, target, low, high):\n    # TODO: implement recursive binary search\n    pass\n",
                    "tests": [
                        { "call": "binary_search_rec([2, 3, 4, 10, 40], 10, 0, 4)", "expected": "3" },
                        { "call": "binary_search_rec([2, 3, 4, 10, 40], 5, 0, 4)", "expected": "-1" }
                    ]
                }
            ]
        }
    ]
};
