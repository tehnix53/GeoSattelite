import pandas as pd

zero = {
    "Water": 3588,
    "Emergent Wetlands": 2699,
    "Tree Canopy": 402,
    "Shrubland": 652,
    "Low Vegetation": 1794477,
    "Barren": 12723,
    "Structures": 11752,
    "Impervious Surfaces": 5759
}

one = {
    "Tree Canopy": 957,
    "Shrubland": 627101,
    "Low Vegetation": 1693404,
    "Barren": 3680,
    "Structures": 18247,
    "Impervious Surfaces": 11906,
    "Impervious Roads": 36097,
    "Tree Canopy over Structures": 1944,
    "Tree Canopy over Impervious Roads": 260
}

two = {
    "Emergent Wetlands": 8819,
    "Tree Canopy": 583,
    "Shrubland": 1678,
    "Low Vegetation": 1763388,
    "Structures": 16174,
    "Impervious Surfaces": 16214,
    "Impervious Roads": 122,
    "Tree Canopy over Structures": 219
}

df = pd.DataFrame()
df['id'] = [0,1,2]
df['val'] = [zero, one, two]

value = df.loc[df.id == int(1)]['val'].values[0]
print (value)