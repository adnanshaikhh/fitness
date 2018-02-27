# Types of carbs

# Starch also known as complex carbs
# Starch or amylum is a polymeric carbohydrate consisting of a large number of
# glucose units joined by glycosidic bonds. This polysaccharide is produced by
# most green plants as energy storage
# Limit refined starches. These are grains that have been processed so that the
# nutrient and fiber-rich parts are removed (bran and germ) (the two outer
# layers) and only the starchy interior remains.
#   BEFORE          AFTER
# (unrefined)     (refined)
#  Brown rice     White rice
# Wholemeal flour  White Flour
# Examples include whole-grain rice, wholemeal bread, porridge oats and
# whole-wheat pasta. Contain more fibre, keep you fuller for longer.

# Fats

# 1. Triacylglycerols (fats and oils)
# Structure: Made from 1 glycerol + 3 fatty acid tails = tri-acylglycerol
# Example: Fats: Butter, lard Oils: Corn oil, olive oil, margerine

# TWO major functions of fats and oils:

# A. Energy storage. Fats are a more compact fuel than starch.
#    Fat contains twice the energy-rich (C-H) bonds as glucose
#    Fat stores twice as much energy as glucose
#    Fat produces twice as many calories (9 kcal/gm vs 4 kcal/gm) when burned
#    Unfortunately, you need to put twice as much energy to burn off a pound of
#    excess fat than you do of glycogen...

# B. Cushions and insulates the body and nerves.
#    Each and every one of your nerves is wrapped in a lipid-rich layer called
#    the myelin sheath.

# Fats are needed for proper functioning of nerves and brain cells, allow
# absorption of the fat-soluble vitamins A,D,E and K, provide needed fatty acids
# and cholesterol for cell membranes. "Best" fats are mono- or poly-unsaturated
# vegetable oils (olive oil, canola oil); limit saturated fats in red meat,
# butter, cheese, avoid partially hydrogenated oils with trans fats. 

# Proteins

# BMR = 1500
# 33% reduction = 1000
import sys
from tabulate import tabulate
from colorama import init
init()

calorie_lim = 1000

# 4 cals per g
carb_lim = 75
pro_lim = 100
# 9 cals per g
fat_lim = 33

macro_dict = {
    # Cals, Carbs, Protein, Fat
    # Chicken contains no carbs at all
    "chicken":[187, 0, 33, 4],
    "eggs raw":[143, 0.7, 13, 10],
    "eggs boiled":[155, 1.1, 13, 11],
    "paneer":[98, 3.4, 11, 4.3],
    # Neither does butter
    "butter":[717, 0.1, 0.9, 81],
    # Assuming it's sunflower
    # NOTE: 2tbsp = 1/8 cup = 29.57g 
    # NOTE: Ladle = 12g, Normally put about 8g avg 
    "oil":[884, 0, 0, 100],
    # Assuming it's Chitale
    "milk":[69, 5.1, 3.6, 3.8],

    # Starchy
    "roti":[220, 44, 8, 2],
    "rice":[130, 28, 2.7, 0.3],
    "bread":[265, 49, 9, 3.2],
    "potato":[77, 17, 2, 0.1],
    "corn":[86, 19, 3.2, 1.2],
    # Starchy + Fruity
    "banana":[89, 23, 1.1, 0.3],
    # Starchy + Protein
    "chickpeas":[164, 27, 9, 2.6],
    "kidney beans":[127, 23, 9, 0.5],
    
    # Veggies
    "tomato":[18, 3.9, 0.9, 0.2],
    "cucumber":[16, 3.6, 0.7, 0.1],
    "cabbage":[25, 6, 1.3, 0.1],
    "red cabbage":[31, 7, 1.4, 0.2],
    "onion":[40, 9, 1.1, 0.1],
    "fenugreek":[49, 6, 4, 1],

    # Fruits
    "apple":[52, 14, 0.3, 0.2],
    "sweet lime":[43, 10, 1, 0],
    "kiwi":[61, 15, 1.1, 0.5],
    "guava":[68, 14, 2.6, 1],
    
    # 1 scoop
    "whey":[120, 3, 24, 1]
    }

TOTAL_CALS = 0.0
TOTAL_C = 0.0
TOTAL_P = 0.0
TOTAL_F = 0.0

table = []

with open(sys.argv[1]) as f:
    content = f.readlines()
    for line in content:
        line_arr = line.split(':')
        food_item = line_arr[0]
        food_mult = float(line_arr[1]) / 100
        if food_item in macro_dict:
            food_macros = macro_dict[food_item]
            CURR_CALS = food_mult * food_macros[0]
            CURR_C = food_mult * food_macros[1]
            CURR_P = food_mult * food_macros[2]
            CURR_F = food_mult * food_macros[3]
            table.append( [food_item, food_mult, round(CURR_CALS, 2), \
                                                 round(CURR_C, 2),    \
                                                 round(CURR_P, 2),    \
                                                 round(CURR_F, 2)])
            TOTAL_CALS += CURR_CALS
            TOTAL_C += CURR_C
            TOTAL_P += CURR_P
            TOTAL_F += CURR_F
        else:
            print(food_item + "doesn't exist in the dict!")
    table.append( ['\033[1m\033[36m' + "TOTAL", "---", round(TOTAL_CALS, 2), \
                                   round(TOTAL_C, 2),    \
                                   round(TOTAL_P, 2),    \
                                   round(TOTAL_F, 2)])

    print(tabulate(table, headers=["Food",       \
                                   "Multiplier", \
                                   "Calories",   \
                                   "Carbs",      \
                                   "Protein",    \
                                   "Fats"]))

    print('\033[31m' + "Cals left: " + str(round ((calorie_lim - TOTAL_CALS), 2)) + \
          '\033[32m' + " Carbs left: " + str (round ((carb_lim - TOTAL_C), 2)) +    \
          '\033[33m' + " Protein left: " + str (round ((pro_lim - TOTAL_P),2)) +    \
          '\033[35m' + " Fats left: " + str (round((fat_lim - TOTAL_F),2)) )
