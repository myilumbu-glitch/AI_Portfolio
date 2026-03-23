import json                #19.03.26

text = input("Enter text: ")

# Clean text
text = text.lower()
text = text.replace("!", "").replace(".", "").replace(",", "")

words = text.split()

counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

# Print results
for word, count in counts.items():
    print(f"{word}: {count}")

# Save to file
with open("word_count.json", "w") as file:
    json.dump(counts, file)