from string import ascii_letters, digits
from random import choice
from data import DATA, NAME, PREP, DATE, COMP
from random import random


# По условию невозможно реализовать нормальную хеш функцию, поэтому возникает много коллизий
# Но задачу я реализовал
def hash(name):
    """
    Generate reduced login.
    Example: name='Super Cool Man'
    login = Super_CM

    """
    table = [302, 907, 419, 925, 309, 520, 493, 380, 429, 208, 642, 947, 823, 950, 437, 245, 101, 298, 902, 903, 394, 811, 537, 363, 688, 105, 22, 876, 146, 819, 345, 674, 1021, 134, 54, 788, 469, 909, 355, 7, 956, 61, 714, 675, 343, 81, 230, 966, 593, 372, 147, 32, 111, 60, 936, 377, 364, 872, 442, 917, 979, 241, 232, 612, 84, 639, 25, 753, 694, 417, 747, 481, 213, 31, 852, 786, 334, 895, 3, 219, 449, 152, 451, 734, 992, 151, 148, 743, 63, 170, 846, 821, 412, 52, 997, 426, 854, 1001, 873, 866, 416, 273, 507, 506, 884, 558, 732, 233, 931, 922, 667, 444, 39, 144, 106, 485, 472, 177, 831, 311, 14, 527, 448, 414, 80, 15, 196, 896, 905, 633, 952, 566, 141, 281, 477, 654, 314, 684, 49, 705, 934, 615, 742, 420, 608, 802, 890, 46, 374, 850, 132, 610, 570, 752, 1017, 1009, 666, 44, 935, 860, 785, 239, 908, 829, 341, 231, 197, 810, 727, 292, 814, 215, 535, 758, 369, 773, 577, 724, 692, 462, 256, 10, 193, 137, 751, 360, 769, 5, 30, 961, 806, 159, 790, 236, 863, 209, 912, 86, 697, 464, 136, 48, 755, 718, 899, 555, 2, 1015, 924, 782, 190, 275, 409, 328, 651, 953, 969, 122, 977, 643, 118, 257, 499, 774, 293, 628, 143, 262, 719, 536, 382, 68, 1019, 920, 182, 405, 693, 376, 543, 391, 268, 951, 1014, 95, 62, 423, 212, 98, 125, 397, 204, 986, 978, 156, 584, 534, 690, 399, 928, 47, 856, 681, 510, 12, 498, 435, 609, 252, 869, 1022, 668, 351, 771, 838, 387, 243, 517, 468, 439, 260, 973, 138, 322, 760, 540, 930, 630, 853, 671, 673, 251, 592, 392, 778, 638, 845, 991, 691, 427, 646, 763, 133, 995, 130, 552, 911, 723, 461, 817, 1007, 713, 361, 918, 516, 432, 957, 249, 887, 1000, 479, 689, 750, 474, 653, 295, 546, 532, 906, 621, 411, 1006, 777, 720, 169, 207, 29, 205, 649, 926, 393, 597, 515, 254, 476, 385, 851, 791, 740, 410, 378, 775, 627, 894, 490, 487, 290, 971, 308, 285, 198, 728, 929, 575, 316, 834, 160, 706, 824, 301, 958, 730, 541, 496, 83, 715, 456, 6, 962, 963, 140, 1023, 910, 235, 340, 559, 366, 837, 441, 874, 157, 184, 849, 158, 403, 347, 168, 333, 784, 557, 324, 53, 880, 970, 187, 463, 794, 744, 656, 836, 446, 539, 644, 968, 556, 904, 766, 622, 960, 73, 486, 545, 858, 400, 686, 585, 938, 561, 55, 484, 349, 562, 945, 923, 438, 685, 739, 695, 1010, 702, 835, 210, 800, 88, 358, 503, 780, 18, 163, 109, 731, 972, 578, 71, 217, 421, 326, 665, 954, 650, 795, 983, 359, 607, 707, 20, 759, 191, 965, 661, 424, 996, 698, 542, 77, 647, 350, 57, 229, 283, 700, 51, 121, 914, 848, 40, 430, 266, 841, 381, 23, 530, 709, 812, 362, 843, 90, 34, 1016, 315, 882, 567, 491, 206, 522, 155, 875, 250, 861, 859, 721, 119, 531, 224, 815, 964, 330, 242, 42, 482, 173, 955, 679, 220, 325, 433, 320, 445, 56, 72, 640, 8, 1013, 107, 623, 725, 746, 683, 590, 149, 313, 497, 425, 560, 126, 258, 346, 589, 768, 303, 407, 614, 981, 75, 948, 480, 494, 770, 33, 544, 857, 891, 564, 519, 680, 153, 617, 329, 881, 396, 284, 789, 203, 189, 66, 820, 712, 344, 547, 473, 598, 582, 162, 940, 652, 270, 200, 629, 703, 717, 500, 276, 805, 218, 526, 943, 574, 237, 166, 521, 447, 222, 670, 117, 549, 757, 238, 331, 100, 454, 678, 613, 620, 687, 214, 816, 594, 569, 583, 492, 1012, 893, 139, 1011, 864, 1, 781, 129, 94, 226, 736, 244, 365, 754, 870, 398, 357, 253, 434, 913, 710, 871, 0, 179, 272, 518, 9, 264, 818, 733, 827, 842, 108, 664, 59, 901, 65, 458, 572, 389, 985, 886, 395, 677, 512, 696, 306, 660, 502, 228, 13, 259, 440, 645, 336, 889, 764, 501, 897, 513, 36, 581, 604, 672, 631, 915, 401, 50, 551, 634, 267, 762, 489, 120, 216, 375, 78, 28, 123, 776, 114, 980, 797, 726, 865, 682, 591, 514, 287, 289, 939, 263, 919, 975, 368, 998, 4, 183, 76, 45, 390, 987, 223, 538, 167, 1008, 43, 304, 982, 181, 310, 1002, 379, 384, 74, 949, 833, 460, 748, 265, 335, 877, 93, 274, 676, 662, 161, 408, 92, 808, 415, 885, 932, 648, 70, 431, 704, 988, 976, 269, 655, 659, 279, 798, 135, 280, 261, 131, 176, 636, 711, 195, 321, 625, 511, 495, 192, 475, 509, 174, 944, 342, 602, 234, 96, 830, 573, 525, 855, 296, 708, 79, 984, 611, 586, 64, 38, 386, 892, 99, 916, 67, 188, 801, 383, 27, 933, 300, 356, 37, 737, 626, 124, 286, 471, 524, 282, 533, 339, 422, 900, 990, 974, 103, 459, 367, 787, 466, 637, 867, 87, 113, 116, 658, 783, 862, 337, 450, 185, 989, 779, 807, 89, 878, 142, 616, 452, 402, 371, 508, 826, 741, 128, 921, 21, 318, 601, 16, 999, 606, 588, 528, 112, 483, 504, 1003, 255, 576, 587, 941, 199, 657, 373, 317, 993, 619, 58, 370, 247, 69, 959, 761, 294, 946, 579, 847, 180, 127, 699, 767, 478, 221, 327, 453, 832, 813, 388, 307, 338, 796, 729, 529, 967, 1018, 799, 1020, 641, 883, 194, 201, 888, 756, 618, 225, 603, 428, 505, 868, 271, 596, 635, 353, 568, 246, 624, 165, 299, 1004, 240, 605, 211, 840, 323, 839, 553, 828, 563, 175, 765, 701, 825, 82, 804, 17, 632, 792, 898, 154, 172, 803, 879, 11, 844, 749, 85, 404, 277, 457, 745, 291, 600, 413, 942, 418, 735, 822, 793, 102, 202, 571, 319, 550, 115, 465, 809, 19, 1005, 548, 297, 994, 722, 580, 470, 145, 97, 669, 348, 278, 35, 352, 488, 91, 436, 554, 288, 772, 927, 467, 186, 406, 937, 26, 41, 455, 305, 595, 150, 248, 663, 171, 24, 523, 104, 164, 738, 599, 312, 443, 565, 110, 332, 227, 354, 178, 716]
    s = 0
    for c in name:
        idx = table.index(ord(c) % 1024)
    s += idx
    s = s % 2048
    return str(s)

HASH = 'hash'

# Generating hash
for r in DATA:
    r[HASH] = hash(r[NAME])

# generating result file
with open("scientist_with_hash.csv", 'w', encoding='utf-8') as f:
    f.write("hash,ScientistName,preparation,date,components\n")
    f.write(
        "\n".join(map(lambda r: f"{r[HASH]},{r[NAME]},{r[PREP]},{str(r[DATE])},{' '.join(r[COMP])}", DATA))
    )