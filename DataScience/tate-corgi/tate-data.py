import tate

list_of_art = tate.get_artwork()

female_metal = []

# for ele in list_of_art:
#     word = "metal"
#     if (word in ele["data"]["medium"].lower()) and (ele["artist"]["gender"] == "Female"):
#         female_metal.append(ele)
#
# print(len(female_metal))

birth_year = []

for ele in list_of_art:
    year = 1863
    if (ele["artist"]["birth"]["year"] == year):
        birth_year.append(ele["artist"]["name"])

for name in birth_year:
    print(name)
