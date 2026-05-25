# # 4. Cloud Storage Duplicate File Name Resolver

# A cloud storage company stores uploaded filenames from users.

# Sometimes multiple duplicate filenames are uploaded.

# The system should:

# * Keep the first occurrence unchanged
# * Add (1), (2), (3)... for duplicates

# ### Input:

# ```text
# file file image file image data
# ```

# ### Output:

# ```text
# file file(1) image file(2) image(1) data
# ```

# ---


files = input().split()

seen = {}
result = []

for name in files:
    if name not in seen:
        seen[name] = 0
        result.append(name)
    else:
        seen[name] += 1
        result.append(name + "(" + str(seen[name]) + ")")

print(" ".join(result))

