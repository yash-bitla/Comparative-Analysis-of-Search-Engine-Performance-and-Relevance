# %% [markdown]
# # Imports

# %%
import json
import pandas as pd

# %% [markdown]
# # Load Data

# %%
def get_data(file_name):
    with open(file_name) as file:
        return json.load(file)

# %%
google_data = get_data("Google_Result3.json")
ask_data = get_data("results.json")

# %% [markdown]
# # Generate Values

# %%
data = {"Queries": [], "Overlap": [], "Percent_Overlap": [], "Spearman_Coefficient": []}
itr = 1

for query in ask_data:
    data["Queries"].append(f"Query {itr}")
    itr +=1 

    google_set = set(google_data[query])
    ask_set = set(ask_data[query])
    overlap = google_set.intersection(ask_set)
    n = len(overlap)
    data["Overlap"].append(n)
    data["Percent_Overlap"].append(n*10)

    # print(query, overlap)
    # print([(google_data[query].index(url), ask_data[query].index(url)) for url in overlap])
    d_i2 = [(google_data[query].index(url)-ask_data[query].index(url))**2 for url in overlap]
    if n == 0:
        rho = 0
    elif n == 1:
        rho = 1 if d_i2[0] == 0 else 0
    else:
        rho = 1 - ((6 * sum(d_i2)) / (n * (n**2 - 1)))
    
    data["Spearman_Coefficient"].append(rho)
    # break

# %%
df = pd.DataFrame(data)
avgs = df.mean().to_dict()
avgs["col1"] = "Averages"
final_df = df.append(avgs, ignore_index=True)

# %%
final_df.to_csv("results.csv", index=False)


