# Define the pages
pages = {}
for page in webpages:
 pages[page["url"]] = page["nodes"]

# Calculate page rank
d = 0.85 # damping factor
N = len(pages) # number of webpages
r = [1/N] * N # page rank values (initialized to 1/N)

# iterate until convergence
while True:
 new_r = [0] * N
 for i, node in enumerate(pages):
 for neighbor in pages[node]:
 new_r[i] += r[pages[node].index(neighbor)] / len(pages[neighbor])
 new_r[i] *= d
 new_r[i] += (1 - d) / N
 if sum([abs(new_r[i] - r[i]) for i in range(N)]) < 0.001:
 break
 else:
 r = new_r

# Print the results
for url, page_rank in zip(pages.keys(), r):
 print(url, ":", page_rank)