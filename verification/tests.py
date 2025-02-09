"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [5914, ],
            "answer": (6174, 3, True),
            "explanation": "Kaprekar constant"
        },
        {
            "input": [6174, ],
            "answer": (6174, 0, True),
            "explanation": "Input is already a Kaprekar constant"
        },
        {
            "input": [48, ],
            "answer": (27, 2, False),
            "explanation": "Kaprekar cycle"
        },
        {
            "input": [27, ],
            "answer": (27, 0, False),
            "explanation": "Input is already part of a Kaprekar cycle"
        },
        {
            "input": [111, ],
            "answer": (0, 1, None),
            "explanation": "Only one kind of digit in a number"
        },
        {
            "input": [9, ],
            "answer": (0, 1, None),
            "explanation": "One digit number"
        },
    ],
    "Extra": [
        {
            "input": [0, ],
            "answer": (0, 0, None),
            "explanation": "below 10 (1)",
        },
        {
            "input": [1, ],
            "answer": (0, 1, None),
            "explanation": "below 10 (2)",
        },
        {
            "input": [2, ],
            "answer": (0, 1, None),
            "explanation": "below 10 (3)",
        },
        {
            "input": [5, ],
            "answer": (0, 1, None),
            "explanation": "below 10 (4)",
        },
        {
            "input": [7, ],
            "answer": (0, 1, None),
            "explanation": "below 10 (5)",
        },
        {
            "input": [9, ],
            "answer": (0, 1, None),
            "explanation": "below 10 (6)",
        },
        {
            "input": [18, ],
            "answer": (63, 1, False),
            "explanation": "between 10 and 99 (1)",
        },
        {
            "input": [52, ],
            "answer": (27, 1, False),
            "explanation": "between 10 and 99 (2)",
        },
        {
            "input": [93, ],
            "answer": (9, 2, False),
            "explanation": "between 10 and 99 (3)",
        },
        {
            "input": [382, ],
            "answer": (495, 2, True),
            "explanation": "between 100 and 999 (1)",
        },
        {
            "input": [501, ],
            "answer": (495, 1, True),
            "explanation": "between 100 and 999 (2)",
        },
        {
            "input": [946, ],
            "answer": (495, 1, True),
            "explanation": "between 100 and 999 (3)",
        },
        {
            "input": [28151, ],
            "answer": (63954, 2, False),
            "explanation": "between 1000 and 9999 (1)",
        },
        {
            "input": [59410, ],
            "answer": (74943, 3, False),
            "explanation": "between 1000 and 9999 (2)",
        },
        {
            "input": [95654, ],
            "answer": (75933, 4, False),
            "explanation": "between 1000 and 9999 (3)",
        },
        {
            "input": [169410, ],
            "answer": (840852, 2, False),
            "explanation": "between 10000 and 999999 (1)",
        },
        {
            "input": [498056, ],
            "answer": (420876, 6, False),
            "explanation": "between 10000 and 999999 (2)",
        },
        {
            "input": [568094, ],
            "answer": (420876, 6, False),
            "explanation": "between 10000 and 999999 (3)",
        },
        {
            "input": [11, ],
            "answer": (0, 1, None),
            "explanation": "one-digit numbers (1)",
        },
        {
            "input": [6666, ],
            "answer": (0, 1, None),
            "explanation": "one-digit numbers (2)",
        },
        {
            "input": [888888, ],
            "answer": (0, 1, None),
            "explanation": "one-digit numbers (3)",
        },
        {
            "input": [6266, ],
            "answer": (6174, 4, True),
            "explanation": "only one digit difference (1)",
        },
        {
            "input": [1171, ],
            "answer": (6174, 6, True),
            "explanation": "only one digit difference (2)",
        },
        {
            "input": [84888, ],
            "answer": (62964, 2, False),
            "explanation": "only one digit difference (3)",
        },
        {
            "input": [655, ],
            "answer": (495, 6, True),
            "explanation": "special tests to check if leading zeros have been considered (1)",
        },
        {
            "input": [100000, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (2)",
        },
        {
            "input": [877777, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (3)",
        },
        {
            "input": [495, ],
            "answer": (495, 0, True),
            "explanation": "Kaprekar constants (1)",
        },
        {
            "input": [6174, ],
            "answer": (6174, 0, True),
            "explanation": "Kaprekar constants (2)",
        },
        {
            "input": [631764, ],
            "answer": (631764, 0, True),
            "explanation": "Kaprekar constants (3)",
        },
        {
            "input": [549945, ],
            "answer": (549945, 0, True),
            "explanation": "Kaprekar constants (4)",
        },
        {
            "input": [81, ],
            "answer": (81, 0, False),
            "explanation": "numbers from Kaprekar cycles (1)",
        },
        {
            "input": [63, ],
            "answer": (63, 0, False),
            "explanation": "numbers from Kaprekar cycles (2)",
        },
        {
            "input": [27, ],
            "answer": (27, 0, False),
            "explanation": "numbers from Kaprekar cycles (3)",
        },
        {
            "input": [45, ],
            "answer": (45, 0, False),
            "explanation": "numbers from Kaprekar cycles (4)",
        },
        {
            "input": [74943, ],
            "answer": (74943, 0, False),
            "explanation": "numbers from Kaprekar cycles (5)",
        },
        {
            "input": [62964, ],
            "answer": (62964, 0, False),
            "explanation": "numbers from Kaprekar cycles (6)",
        },
        {
            "input": [71973, ],
            "answer": (71973, 0, False),
            "explanation": "numbers from Kaprekar cycles (7)",
        },
        {
            "input": [83952, ],
            "answer": (83952, 0, False),
            "explanation": "numbers from Kaprekar cycles (8)",
        },
        {
            "input": [63954, ],
            "answer": (63954, 0, False),
            "explanation": "numbers from Kaprekar cycles (9)",
        },
        {
            "input": [61974, ],
            "answer": (61974, 0, False),
            "explanation": "numbers from Kaprekar cycles (10)",
        },
        {
            "input": [82962, ],
            "answer": (82962, 0, False),
            "explanation": "numbers from Kaprekar cycles (11)",
        },
        {
            "input": [75933, ],
            "answer": (75933, 0, False),
            "explanation": "numbers from Kaprekar cycles (12)",
        },
        {
            "input": [53955, ],
            "answer": (53955, 0, False),
            "explanation": "numbers from Kaprekar cycles (13)",
        },
        {
            "input": [59994, ],
            "answer": (59994, 0, False),
            "explanation": "numbers from Kaprekar cycles (14)",
        },
        {
            "input": [851742, ],
            "answer": (851742, 0, False),
            "explanation": "numbers from Kaprekar cycles (15)",
        },
        {
            "input": [750843, ],
            "answer": (750843, 0, False),
            "explanation": "numbers from Kaprekar cycles (16)",
        },
        {
            "input": [840852, ],
            "answer": (840852, 0, False),
            "explanation": "numbers from Kaprekar cycles (17)",
        },
        {
            "input": [860832, ],
            "answer": (860832, 0, False),
            "explanation": "numbers from Kaprekar cycles (18)",
        },
        {
            "input": [862632, ],
            "answer": (862632, 0, False),
            "explanation": "numbers from Kaprekar cycles (19)",
        },
        {
            "input": [642654, ],
            "answer": (642654, 0, False),
            "explanation": "numbers from Kaprekar cycles (20)",
        },
        {
            "input": [420876, ],
            "answer": (420876, 0, False),
            "explanation": "numbers from Kaprekar cycles (21)",
        },
        {
            "input": [12, ],
            "answer": (9, 1, False),
            "explanation": "leading to 9 (1)",
        },
        {
            "input": [39, ],
            "answer": (9, 2, False),
            "explanation": "leading to 9 (2)",
        },
        {
            "input": [57, ],
            "answer": (63, 2, False),
            "explanation": "leading to 63 (1)",
        },
        {
            "input": [46, ],
            "answer": (63, 2, False),
            "explanation": "leading to 63 (2)",
        },
        {
            "input": [73, ],
            "answer": (27, 2, False),
            "explanation": "leading to 27 (1)",
        },
        {
            "input": [95, ],
            "answer": (27, 2, False),
            "explanation": "leading to 27 (2)",
        },
        {
            "input": [83, ],
            "answer": (45, 1, False),
            "explanation": "leading to 45 (1)",
        },
        {
            "input": [38, ],
            "answer": (45, 1, False),
            "explanation": "leading to 45 (2)",
        },
        {
            "input": [90, ],
            "answer": (81, 1, False),
            "explanation": "leading to 81 (1)",
        },
        {
            "input": [682, ],
            "answer": (495, 2, True),
            "explanation": "leading to 495 (1)",
        },
        {
            "input": [574, ],
            "answer": (495, 4, True),
            "explanation": "leading to 495 (2)",
        },
        {
            "input": [1404, ],
            "answer": (6174, 3, True),
            "explanation": "leading to 6174 (1)",
        },
        {
            "input": [9328, ],
            "answer": (6174, 5, True),
            "explanation": "leading to 6174 (2)",
        },
        {
            "input": [76791, ],
            "answer": (74943, 4, False),
            "explanation": "leading to 74943 (1)",
        },
        {
            "input": [57072, ],
            "answer": (74943, 1, False),
            "explanation": "leading to 74943 (2)",
        },
        {
            "input": [45839, ],
            "answer": (63954, 1, False),
            "explanation": "leading to 63954 (1)",
        },
        {
            "input": [62682, ],
            "answer": (63954, 1, False),
            "explanation": "leading to 63954 (2)",
        },
        {
            "input": [90421, ],
            "answer": (75933, 3, False),
            "explanation": "leading to 75933 (1)",
        },
        {
            "input": [13299, ],
            "answer": (75933, 2, False),
            "explanation": "leading to 75933 (2)",
        },
        {
            "input": [21143, ],
            "answer": (83952, 2, False),
            "explanation": "leading to 83952 (1)",
        },
        {
            "input": [22680, ],
            "answer": (83952, 1, False),
            "explanation": "leading to 83952 (2)",
        },
        {
            "input": [85691, ],
            "answer": (82962, 1, False),
            "explanation": "leading to 82962 (1)",
        },
        {
            "input": [88506, ],
            "answer": (82962, 1, False),
            "explanation": "leading to 82962 (2)",
        },
        {
            "input": [79739, ],
            "answer": (61974, 1, False),
            "explanation": "leading to 61974 (1)",
        },
        {
            "input": [84253, ],
            "answer": (61974, 1, False),
            "explanation": "leading to 61974 (2)",
        },
        {
            "input": [12482, ],
            "answer": (71973, 1, False),
            "explanation": "leading to 71973 (1)",
        },
        {
            "input": [14044, ],
            "answer": (71973, 2, False),
            "explanation": "leading to 71973 (2)",
        },
        {
            "input": [15742, ],
            "answer": (62964, 1, False),
            "explanation": "leading to 62964 (1)",
        },
        {
            "input": [64110, ],
            "answer": (62964, 1, False),
            "explanation": "leading to 62964 (2)",
        },
        {
            "input": [95994, ],
            "answer": (53955, 1, False),
            "explanation": "leading to 53955 (1)",
        },
        {
            "input": [45040, ],
            "answer": (53955, 1, False),
            "explanation": "leading to 53955 (2)",
        },
        {
            "input": [71666, ],
            "answer": (59994, 1, False),
            "explanation": "leading to 59994 (1)",
        },
        {
            "input": [28333, ],
            "answer": (59994, 1, False),
            "explanation": "leading to 59994 (2)",
        },
        {
            "input": [202582, ],
            "answer": (851742, 8, False),
            "explanation": "leading to 851742 (1)",
        },
        {
            "input": [940991, ],
            "answer": (851742, 9, False),
            "explanation": "leading to 851742 (2)",
        },
        {
            "input": [536440, ],
            "answer": (860832, 3, False),
            "explanation": "leading to 860832 (1)",
        },
        {
            "input": [178939, ],
            "answer": (860832, 1, False),
            "explanation": "leading to 860832 (2)",
        },
        {
            "input": [110275, ],
            "answer": (840852, 2, False),
            "explanation": "leading to 840852 (1)",
        },
        {
            "input": [485619, ],
            "answer": (840852, 1, False),
            "explanation": "leading to 840852 (2)",
        },
        {
            "input": [307366, ],
            "answer": (420876, 6, False),
            "explanation": "leading to 420876 (1)",
        },
        {
            "input": [567244, ],
            "answer": (420876, 4, False),
            "explanation": "leading to 420876 (2)",
        },
        {
            "input": [916030, ],
            "answer": (862632, 2, False),
            "explanation": "leading to 862632 (1)",
        },
        {
            "input": [527108, ],
            "answer": (862632, 1, False),
            "explanation": "leading to 862632 (2)",
        },
        {
            "input": [100843, ],
            "answer": (750843, 2, False),
            "explanation": "leading to 750843 (1)",
        },
        {
            "input": [681275, ],
            "answer": (750843, 1, False),
            "explanation": "leading to 750843 (2)",
        },
        {
            "input": [821172, ],
            "answer": (631764, 3, True),
            "explanation": "leading to 631764 (1)",
        },
        {
            "input": [933536, ],
            "answer": (631764, 1, True),
            "explanation": "leading to 631764 (2)",
        },
        {
            "input": [358385, ],
            "answer": (549945, 1, True),
            "explanation": "leading to 549945 (1)",
        },
        {
            "input": [738837, ],
            "answer": (549945, 1, True),
            "explanation": "leading to 549945 (2)",
        },
        {
            "input": [584983, ],
            "answer": (642654, 1, False),
            "explanation": "leading to 642654 (1)",
        },
        {
            "input": [174821, ],
            "answer": (642654, 2, False),
            "explanation": "leading to 642654 (2)",
        },
    ]
}
