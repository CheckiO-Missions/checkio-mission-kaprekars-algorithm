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
            "input": [25, ],
            "answer": (27, 1, False),
            "explanation": "between 10 and 99 (2)",
        },
        {
            "input": [31, ],
            "answer": (63, 2, False),
            "explanation": "between 10 and 99 (3)",
        },
        {
            "input": [49, ],
            "answer": (45, 1, False),
            "explanation": "between 10 and 99 (4)",
        },
        {
            "input": [52, ],
            "answer": (27, 1, False),
            "explanation": "between 10 and 99 (5)",
        },
        {
            "input": [64, ],
            "answer": (63, 2, False),
            "explanation": "between 10 and 99 (6)",
        },
        {
            "input": [78, ],
            "answer": (9, 1, False),
            "explanation": "between 10 and 99 (7)",
        },
        {
            "input": [82, ],
            "answer": (9, 2, False),
            "explanation": "between 10 and 99 (8)",
        },
        {
            "input": [93, ],
            "answer": (9, 2, False),
            "explanation": "between 10 and 99 (9)",
        },
        {
            "input": [178, ],
            "answer": (495, 3, True),
            "explanation": "between 100 and 999 (1)",
        },
        {
            "input": [268, ],
            "answer": (495, 2, True),
            "explanation": "between 100 and 999 (2)",
        },
        {
            "input": [382, ],
            "answer": (495, 2, True),
            "explanation": "between 100 and 999 (3)",
        },
        {
            "input": [496, ],
            "answer": (495, 1, True),
            "explanation": "between 100 and 999 (4)",
        },
        {
            "input": [501, ],
            "answer": (495, 1, True),
            "explanation": "between 100 and 999 (5)",
        },
        {
            "input": [630, ],
            "answer": (495, 2, True),
            "explanation": "between 100 and 999 (6)",
        },
        {
            "input": [794, ],
            "answer": (495, 1, True),
            "explanation": "between 100 and 999 (7)",
        },
        {
            "input": [820, ],
            "answer": (495, 4, True),
            "explanation": "between 100 and 999 (8)",
        },
        {
            "input": [946, ],
            "answer": (495, 1, True),
            "explanation": "between 100 and 999 (9)",
        },
        {
            "input": [10200, ],
            "answer": (74943, 4, False),
            "explanation": "between 1000 and 9999 (1)",
        },
        {
            "input": [14698, ],
            "answer": (83952, 1, False),
            "explanation": "between 1000 and 9999 (2)",
        },
        {
            "input": [26578, ],
            "answer": (61974, 1, False),
            "explanation": "between 1000 and 9999 (3)",
        },
        {
            "input": [28151, ],
            "answer": (63954, 2, False),
            "explanation": "between 1000 and 9999 (4)",
        },
        {
            "input": [30065, ],
            "answer": (74943, 5, False),
            "explanation": "between 1000 and 9999 (5)",
        },
        {
            "input": [36489, ],
            "answer": (63954, 1, False),
            "explanation": "between 1000 and 9999 (6)",
        },
        {
            "input": [48978, ],
            "answer": (75933, 4, False),
            "explanation": "between 1000 and 9999 (7)",
        },
        {
            "input": [40158, ],
            "answer": (83952, 1, False),
            "explanation": "between 1000 and 9999 (8)",
        },
        {
            "input": [59410, ],
            "answer": (74943, 3, False),
            "explanation": "between 1000 and 9999 (9)",
        },
        {
            "input": [54870, ],
            "answer": (82962, 1, False),
            "explanation": "between 1000 and 9999 (10)",
        },
        {
            "input": [67904, ],
            "answer": (75933, 3, False),
            "explanation": "between 1000 and 9999 (11)",
        },
        {
            "input": [69098, ],
            "answer": (75933, 3, False),
            "explanation": "between 1000 and 9999 (12)",
        },
        {
            "input": [70549, ],
            "answer": (75933, 3, False),
            "explanation": "between 1000 and 9999 (13)",
        },
        {
            "input": [70900, ],
            "answer": (75933, 3, False),
            "explanation": "between 1000 and 9999 (14)",
        },
        {
            "input": [89204, ],
            "answer": (74943, 3, False),
            "explanation": "between 1000 and 9999 (15)",
        },
        {
            "input": [89059, ],
            "answer": (74943, 3, False),
            "explanation": "between 1000 and 9999 (16)",
        },
        {
            "input": [90606, ],
            "answer": (74943, 3, False),
            "explanation": "between 1000 and 9999 (17)",
        },
        {
            "input": [95654, ],
            "answer": (75933, 4, False),
            "explanation": "between 1000 and 9999 (18)",
        },
        {
            "input": [106894, ],
            "answer": (420876, 6, False),
            "explanation": "between 10000 and 999999 (1)",
        },
        {
            "input": [169410, ],
            "answer": (840852, 2, False),
            "explanation": "between 10000 and 999999 (2)",
        },
        {
            "input": [246102, ],
            "answer": (420876, 4, False),
            "explanation": "between 10000 and 999999 (3)",
        },
        {
            "input": [286481, ],
            "answer": (642654, 2, False),
            "explanation": "between 10000 and 999999 (4)",
        },
        {
            "input": [304856, ],
            "answer": (862632, 2, False),
            "explanation": "between 10000 and 999999 (5)",
        },
        {
            "input": [304897, ],
            "answer": (840852, 2, False),
            "explanation": "between 10000 and 999999 (6)",
        },
        {
            "input": [498056, ],
            "answer": (420876, 6, False),
            "explanation": "between 10000 and 999999 (7)",
        },
        {
            "input": [497802, ],
            "answer": (420876, 9, False),
            "explanation": "between 10000 and 999999 (8)",
        },
        {
            "input": [568094, ],
            "answer": (420876, 6, False),
            "explanation": "between 10000 and 999999 (9)",
        },
        {
            "input": [597803, ],
            "answer": (860832, 2, False),
            "explanation": "between 10000 and 999999 (10)",
        },
        {
            "input": [616049, ],
            "answer": (860832, 2, False),
            "explanation": "between 10000 and 999999 (11)",
        },
        {
            "input": [647904, ],
            "answer": (862632, 2, False),
            "explanation": "between 10000 and 999999 (12)",
        },
        {
            "input": [708864, ],
            "answer": (840852, 1, False),
            "explanation": "between 10000 and 999999 (13)",
        },
        {
            "input": [799984, ],
            "answer": (420876, 4, False),
            "explanation": "between 10000 and 999999 (14)",
        },
        {
            "input": [895260, ],
            "answer": (851742, 5, False),
            "explanation": "between 10000 and 999999 (15)",
        },
        {
            "input": [894604, ],
            "answer": (860832, 2, False),
            "explanation": "between 10000 and 999999 (16)",
        },
        {
            "input": [961209, ],
            "answer": (860832, 6, False),
            "explanation": "between 10000 and 999999 (17)",
        },
        {
            "input": [960471, ],
            "answer": (862632, 2, False),
            "explanation": "between 10000 and 999999 (18)",
        },
        {
            "input": [11, ],
            "answer": (0, 1, None),
            "explanation": "one-digit numbers (1)",
        },
        {
            "input": [22, ],
            "answer": (0, 1, None),
            "explanation": "one-digit numbers (2)",
        },
        {
            "input": [33, ],
            "answer": (0, 1, None),
            "explanation": "one-digit numbers (3)",
        },
        {
            "input": [77, ],
            "answer": (0, 1, None),
            "explanation": "one-digit numbers (4)",
        },
        {
            "input": [333, ],
            "answer": (0, 1, None),
            "explanation": "one-digit numbers (5)",
        },
        {
            "input": [555, ],
            "answer": (0, 1, None),
            "explanation": "one-digit numbers (6)",
        },
        {
            "input": [2222, ],
            "answer": (0, 1, None),
            "explanation": "one-digit numbers (7)",
        },
        {
            "input": [6666, ],
            "answer": (0, 1, None),
            "explanation": "one-digit numbers (8)",
        },
        {
            "input": [44444, ],
            "answer": (0, 1, None),
            "explanation": "one-digit numbers (9)",
        },
        {
            "input": [99999, ],
            "answer": (0, 1, None),
            "explanation": "one-digit numbers (10)",
        },
        {
            "input": [888888, ],
            "answer": (0, 1, None),
            "explanation": "one-digit numbers (11)",
        },
        {
            "input": [111111, ],
            "answer": (0, 1, None),
            "explanation": "one-digit numbers (12)",
        },
        {
            "input": [191, ],
            "answer": (495, 4, True),
            "explanation": "only one digit difference (1)",
        },
        {
            "input": [885, ],
            "answer": (495, 4, True),
            "explanation": "only one digit difference (2)",
        },
        {
            "input": [6266, ],
            "answer": (6174, 4, True),
            "explanation": "only one digit difference (3)",
        },
        {
            "input": [1171, ],
            "answer": (6174, 6, True),
            "explanation": "only one digit difference (4)",
        },
        {
            "input": [84888, ],
            "answer": (62964, 2, False),
            "explanation": "only one digit difference (5)",
        },
        {
            "input": [655, ],
            "answer": (495, 6, True),
            "explanation": "special tests to check if leading zeros have been considered (1)",
        },
        {
            "input": [665, ],
            "answer": (495, 6, True),
            "explanation": "special tests to check if leading zeros have been considered (2)",
        },
        {
            "input": [766, ],
            "answer": (495, 6, True),
            "explanation": "special tests to check if leading zeros have been considered (3)",
        },
        {
            "input": [776, ],
            "answer": (495, 6, True),
            "explanation": "special tests to check if leading zeros have been considered (4)",
        },
        {
            "input": [877, ],
            "answer": (495, 6, True),
            "explanation": "special tests to check if leading zeros have been considered (5)",
        },
        {
            "input": [887, ],
            "answer": (495, 6, True),
            "explanation": "special tests to check if leading zeros have been considered (6)",
        },
        {
            "input": [988, ],
            "answer": (495, 6, True),
            "explanation": "special tests to check if leading zeros have been considered (7)",
        },
        {
            "input": [998, ],
            "answer": (495, 6, True),
            "explanation": "special tests to check if leading zeros have been considered (8)",
        },
        {
            "input": [1000, ],
            "answer": (6174, 5, True),
            "explanation": "special tests to check if leading zeros have been considered (9)",
        },
        {
            "input": [1110, ],
            "answer": (6174, 5, True),
            "explanation": "special tests to check if leading zeros have been considered (10)",
        },
        {
            "input": [2111, ],
            "answer": (6174, 5, True),
            "explanation": "special tests to check if leading zeros have been considered (11)",
        },
        {
            "input": [2221, ],
            "answer": (6174, 5, True),
            "explanation": "special tests to check if leading zeros have been considered (12)",
        },
        {
            "input": [3222, ],
            "answer": (6174, 5, True),
            "explanation": "special tests to check if leading zeros have been considered (13)",
        },
        {
            "input": [3332, ],
            "answer": (6174, 5, True),
            "explanation": "special tests to check if leading zeros have been considered (14)",
        },
        {
            "input": [4333, ],
            "answer": (6174, 5, True),
            "explanation": "special tests to check if leading zeros have been considered (15)",
        },
        {
            "input": [4443, ],
            "answer": (6174, 5, True),
            "explanation": "special tests to check if leading zeros have been considered (16)",
        },
        {
            "input": [5444, ],
            "answer": (6174, 5, True),
            "explanation": "special tests to check if leading zeros have been considered (17)",
        },
        {
            "input": [5554, ],
            "answer": (6174, 5, True),
            "explanation": "special tests to check if leading zeros have been considered (18)",
        },
        {
            "input": [6555, ],
            "answer": (6174, 5, True),
            "explanation": "special tests to check if leading zeros have been considered (19)",
        },
        {
            "input": [6665, ],
            "answer": (6174, 5, True),
            "explanation": "special tests to check if leading zeros have been considered (20)",
        },
        {
            "input": [7666, ],
            "answer": (6174, 5, True),
            "explanation": "special tests to check if leading zeros have been considered (21)",
        },
        {
            "input": [7776, ],
            "answer": (6174, 5, True),
            "explanation": "special tests to check if leading zeros have been considered (22)",
        },
        {
            "input": [8777, ],
            "answer": (6174, 5, True),
            "explanation": "special tests to check if leading zeros have been considered (23)",
        },
        {
            "input": [8887, ],
            "answer": (6174, 5, True),
            "explanation": "special tests to check if leading zeros have been considered (24)",
        },
        {
            "input": [9888, ],
            "answer": (6174, 5, True),
            "explanation": "special tests to check if leading zeros have been considered (25)",
        },
        {
            "input": [9998, ],
            "answer": (6174, 5, True),
            "explanation": "special tests to check if leading zeros have been considered (26)",
        },
        {
            "input": [10000, ],
            "answer": (74943, 6, False),
            "explanation": "special tests to check if leading zeros have been considered (27)",
        },
        {
            "input": [11110, ],
            "answer": (74943, 6, False),
            "explanation": "special tests to check if leading zeros have been considered (28)",
        },
        {
            "input": [21111, ],
            "answer": (74943, 6, False),
            "explanation": "special tests to check if leading zeros have been considered (29)",
        },
        {
            "input": [22221, ],
            "answer": (74943, 6, False),
            "explanation": "special tests to check if leading zeros have been considered (30)",
        },
        {
            "input": [32222, ],
            "answer": (74943, 6, False),
            "explanation": "special tests to check if leading zeros have been considered (31)",
        },
        {
            "input": [33332, ],
            "answer": (74943, 6, False),
            "explanation": "special tests to check if leading zeros have been considered (32)",
        },
        {
            "input": [43333, ],
            "answer": (74943, 6, False),
            "explanation": "special tests to check if leading zeros have been considered (33)",
        },
        {
            "input": [44443, ],
            "answer": (74943, 6, False),
            "explanation": "special tests to check if leading zeros have been considered (34)",
        },
        {
            "input": [54444, ],
            "answer": (74943, 6, False),
            "explanation": "special tests to check if leading zeros have been considered (35)",
        },
        {
            "input": [55554, ],
            "answer": (74943, 6, False),
            "explanation": "special tests to check if leading zeros have been considered (36)",
        },
        {
            "input": [65555, ],
            "answer": (74943, 6, False),
            "explanation": "special tests to check if leading zeros have been considered (37)",
        },
        {
            "input": [66665, ],
            "answer": (74943, 6, False),
            "explanation": "special tests to check if leading zeros have been considered (38)",
        },
        {
            "input": [76666, ],
            "answer": (74943, 6, False),
            "explanation": "special tests to check if leading zeros have been considered (39)",
        },
        {
            "input": [77776, ],
            "answer": (74943, 6, False),
            "explanation": "special tests to check if leading zeros have been considered (40)",
        },
        {
            "input": [87777, ],
            "answer": (74943, 6, False),
            "explanation": "special tests to check if leading zeros have been considered (41)",
        },
        {
            "input": [88887, ],
            "answer": (74943, 6, False),
            "explanation": "special tests to check if leading zeros have been considered (42)",
        },
        {
            "input": [98888, ],
            "answer": (74943, 6, False),
            "explanation": "special tests to check if leading zeros have been considered (43)",
        },
        {
            "input": [99998, ],
            "answer": (74943, 6, False),
            "explanation": "special tests to check if leading zeros have been considered (44)",
        },
        {
            "input": [100000, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (45)",
        },
        {
            "input": [111110, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (46)",
        },
        {
            "input": [211111, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (47)",
        },
        {
            "input": [222221, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (48)",
        },
        {
            "input": [322222, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (49)",
        },
        {
            "input": [333332, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (50)",
        },
        {
            "input": [433333, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (51)",
        },
        {
            "input": [444443, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (52)",
        },
        {
            "input": [544444, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (53)",
        },
        {
            "input": [555554, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (54)",
        },
        {
            "input": [655555, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (55)",
        },
        {
            "input": [666665, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (56)",
        },
        {
            "input": [766666, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (57)",
        },
        {
            "input": [777776, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (58)",
        },
        {
            "input": [877777, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (59)",
        },
        {
            "input": [888887, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (60)",
        },
        {
            "input": [988888, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (61)",
        },
        {
            "input": [999998, ],
            "answer": (851742, 11, False),
            "explanation": "special tests to check if leading zeros have been considered (62)",
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
            "input": [56, ],
            "answer": (9, 1, False),
            "explanation": "leading to 9 (3)",
        },
        {
            "input": [98, ],
            "answer": (9, 1, False),
            "explanation": "leading to 9 (4)",
        },
        {
            "input": [43, ],
            "answer": (9, 1, False),
            "explanation": "leading to 9 (5)",
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
            "input": [75, ],
            "answer": (63, 2, False),
            "explanation": "leading to 63 (3)",
        },
        {
            "input": [86, ],
            "answer": (63, 2, False),
            "explanation": "leading to 63 (4)",
        },
        {
            "input": [68, ],
            "answer": (63, 2, False),
            "explanation": "leading to 63 (5)",
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
            "input": [36, ],
            "answer": (27, 1, False),
            "explanation": "leading to 27 (3)",
        },
        {
            "input": [74, ],
            "answer": (27, 1, False),
            "explanation": "leading to 27 (4)",
        },
        {
            "input": [40, ],
            "answer": (27, 2, False),
            "explanation": "leading to 27 (5)",
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
            "input": [61, ],
            "answer": (45, 1, False),
            "explanation": "leading to 45 (3)",
        },
        {
            "input": [94, ],
            "answer": (45, 1, False),
            "explanation": "leading to 45 (4)",
        },
        {
            "input": [91, ],
            "answer": (45, 2, False),
            "explanation": "leading to 45 (5)",
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
            "input": [911, ],
            "answer": (495, 4, True),
            "explanation": "leading to 495 (3)",
        },
        {
            "input": [608, ],
            "answer": (495, 4, True),
            "explanation": "leading to 495 (4)",
        },
        {
            "input": [677, ],
            "answer": (495, 6, True),
            "explanation": "leading to 495 (5)",
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
            "input": [8989, ],
            "answer": (6174, 4, True),
            "explanation": "leading to 6174 (3)",
        },
        {
            "input": [5259, ],
            "answer": (6174, 4, True),
            "explanation": "leading to 6174 (4)",
        },
        {
            "input": [6215, ],
            "answer": (6174, 5, True),
            "explanation": "leading to 6174 (5)",
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
            "input": [40598, ],
            "answer": (74943, 3, False),
            "explanation": "leading to 74943 (3)",
        },
        {
            "input": [64123, ],
            "answer": (74943, 4, False),
            "explanation": "leading to 74943 (4)",
        },
        {
            "input": [82483, ],
            "answer": (74943, 5, False),
            "explanation": "leading to 74943 (5)",
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
            "input": [86212, ],
            "answer": (63954, 2, False),
            "explanation": "leading to 63954 (3)",
        },
        {
            "input": [38143, ],
            "answer": (63954, 5, False),
            "explanation": "leading to 63954 (4)",
        },
        {
            "input": [66128, ],
            "answer": (63954, 2, False),
            "explanation": "leading to 63954 (5)",
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
            "input": [43247, ],
            "answer": (75933, 4, False),
            "explanation": "leading to 75933 (3)",
        },
        {
            "input": [90607, ],
            "answer": (75933, 3, False),
            "explanation": "leading to 75933 (4)",
        },
        {
            "input": [91299, ],
            "answer": (75933, 2, False),
            "explanation": "leading to 75933 (5)",
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
            "input": [10158, ],
            "answer": (83952, 1, False),
            "explanation": "leading to 83952 (3)",
        },
        {
            "input": [43536, ],
            "answer": (83952, 2, False),
            "explanation": "leading to 83952 (4)",
        },
        {
            "input": [75919, ],
            "answer": (83952, 1, False),
            "explanation": "leading to 83952 (5)",
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
            "input": [71694, ],
            "answer": (82962, 1, False),
            "explanation": "leading to 82962 (3)",
        },
        {
            "input": [91563, ],
            "answer": (82962, 1, False),
            "explanation": "leading to 82962 (4)",
        },
        {
            "input": [88466, ],
            "answer": (82962, 2, False),
            "explanation": "leading to 82962 (5)",
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
            "input": [66934, ],
            "answer": (61974, 1, False),
            "explanation": "leading to 61974 (3)",
        },
        {
            "input": [56793, ],
            "answer": (61974, 1, False),
            "explanation": "leading to 61974 (4)",
        },
        {
            "input": [33106, ],
            "answer": (61974, 1, False),
            "explanation": "leading to 61974 (5)",
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
            "input": [75996, ],
            "answer": (71973, 2, False),
            "explanation": "leading to 71973 (3)",
        },
        {
            "input": [72200, ],
            "answer": (71973, 1, False),
            "explanation": "leading to 71973 (4)",
        },
        {
            "input": [84744, ],
            "answer": (71973, 2, False),
            "explanation": "leading to 71973 (5)",
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
            "input": [55158, ],
            "answer": (62964, 2, False),
            "explanation": "leading to 62964 (3)",
        },
        {
            "input": [33956, ],
            "answer": (62964, 1, False),
            "explanation": "leading to 62964 (4)",
        },
        {
            "input": [53228, ],
            "answer": (62964, 1, False),
            "explanation": "leading to 62964 (5)",
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
            "input": [27642, ],
            "answer": (53955, 1, False),
            "explanation": "leading to 53955 (3)",
        },
        {
            "input": [36873, ],
            "answer": (53955, 1, False),
            "explanation": "leading to 53955 (4)",
        },
        {
            "input": [51565, ],
            "answer": (53955, 2, False),
            "explanation": "leading to 53955 (5)",
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
            "input": [36033, ],
            "answer": (59994, 1, False),
            "explanation": "leading to 59994 (3)",
        },
        {
            "input": [33339, ],
            "answer": (59994, 1, False),
            "explanation": "leading to 59994 (4)",
        },
        {
            "input": [99399, ],
            "answer": (59994, 1, False),
            "explanation": "leading to 59994 (5)",
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
            "input": [330856, ],
            "answer": (851742, 11, False),
            "explanation": "leading to 851742 (3)",
        },
        {
            "input": [158901, ],
            "answer": (851742, 2, False),
            "explanation": "leading to 851742 (4)",
        },
        {
            "input": [495624, ],
            "answer": (851742, 4, False),
            "explanation": "leading to 851742 (5)",
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
            "input": [379421, ],
            "answer": (860832, 2, False),
            "explanation": "leading to 860832 (3)",
        },
        {
            "input": [590727, ],
            "answer": (860832, 2, False),
            "explanation": "leading to 860832 (4)",
        },
        {
            "input": [981007, ],
            "answer": (860832, 6, False),
            "explanation": "leading to 860832 (5)",
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
            "input": [912456, ],
            "answer": (840852, 1, False),
            "explanation": "leading to 840852 (3)",
        },
        {
            "input": [408526, ],
            "answer": (840852, 1, False),
            "explanation": "leading to 840852 (4)",
        },
        {
            "input": [741688, ],
            "answer": (840852, 2, False),
            "explanation": "leading to 840852 (5)",
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
            "input": [694532, ],
            "answer": (420876, 9, False),
            "explanation": "leading to 420876 (3)",
        },
        {
            "input": [961833, ],
            "answer": (420876, 8, False),
            "explanation": "leading to 420876 (4)",
        },
        {
            "input": [222761, ],
            "answer": (420876, 8, False),
            "explanation": "leading to 420876 (5)",
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
            "input": [170924, ],
            "answer": (862632, 2, False),
            "explanation": "leading to 862632 (3)",
        },
        {
            "input": [360781, ],
            "answer": (862632, 1, False),
            "explanation": "leading to 862632 (4)",
        },
        {
            "input": [255390, ],
            "answer": (862632, 2, False),
            "explanation": "leading to 862632 (5)",
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
            "input": [140673, ],
            "answer": (750843, 1, False),
            "explanation": "leading to 750843 (3)",
        },
        {
            "input": [849927, ],
            "answer": (750843, 1, False),
            "explanation": "leading to 750843 (4)",
        },
        {
            "input": [672110, ],
            "answer": (750843, 1, False),
            "explanation": "leading to 750843 (5)",
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
            "input": [830717, ],
            "answer": (631764, 2, True),
            "explanation": "leading to 631764 (3)",
        },
        {
            "input": [606973, ],
            "answer": (631764, 3, True),
            "explanation": "leading to 631764 (4)",
        },
        {
            "input": [611728, ],
            "answer": (631764, 3, True),
            "explanation": "leading to 631764 (5)",
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
            "input": [553388, ],
            "answer": (549945, 1, True),
            "explanation": "leading to 549945 (3)",
        },
        {
            "input": [783873, ],
            "answer": (549945, 1, True),
            "explanation": "leading to 549945 (4)",
        },
        {
            "input": [151566, ],
            "answer": (549945, 1, True),
            "explanation": "leading to 549945 (5)",
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
        {
            "input": [369599, ],
            "answer": (642654, 1, False),
            "explanation": "leading to 642654 (3)",
        },
        {
            "input": [119971, ],
            "answer": (642654, 3, False),
            "explanation": "leading to 642654 (4)",
        },
        {
            "input": [487112, ],
            "answer": (642654, 2, False),
            "explanation": "leading to 642654 (5)",
        },
    ]
}
