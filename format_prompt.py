import pandas as pd 

feature_def = pd.read_csv("feature_definitions.csv")
col_name = pd.read_csv("missing/static_0_missing.csv")
#col_name = []
ls = list(feature_def["Variable"])

f = open("def_registry_c_1.txt", "a")

ls_def = dict()

for i in range(1, len(col_name)):
    try:
        if(col_name["percent_missing"][i]<0.5):
            
            pivot = col_name["index"][i]
            idx = ls.index(pivot)

            ls_def[col_name["index"][i]]=(feature_def["Description"][idx])
            des = feature_def["Description"][idx]
            col_ = col_name["index"][i]
            f.write(f"{col_}\n description : {des}\n")
        else:
            print("too many missing value")
    except:
        print("can't find col name")
#print(ls_def)
f.close()