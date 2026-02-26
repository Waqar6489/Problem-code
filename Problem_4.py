# Merge Dictnaries

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

# make two dictionaries and merge them
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
result = merge_dictionaries(dict1, dict2)
print("Merged dictionary:", result)