import csv, pandas

google_stats = "google-political-ads-creative-stats.csv"

df = pandas.read_csv(google_stats)

biden_counter = 0
trump_counter = 0
neither = 0

for each in df["Candidate_Alignment"]:
	if each == "Biden":
		biden_counter += 1
	elif each == "Trump":
		trump_counter += 1
	else:
		neither += 1

print("Trump Count ", trump_counter)
print("Biden Count ", biden_counter)
print("Neither ", neither)

# for each in df["Advertiser_Name"]:
# 	if each == "DONALD J. TRUMP FOR PRESIDENT, INC.":
# 		print(each)



# df_filtered = df[df["Candidate_Alignment"] == "Trump"]

# print(df_filtered.head())