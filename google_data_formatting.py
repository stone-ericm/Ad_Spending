import csv, pandas

google_stats = "google-political-ads-creative-stats.csv"
# google_stats = "test_data.csv"
# with open(google_stats) as csvfile:
# 	reader = csv.reader(csvfile)
# 	for row in reader:
# 		print(len(row))
# 		# print(', '.join(row))
# 		break

############## IMPORT TRUMP PACS ###################

file = open('trump_pacs.txt', 'r')
trump_pac_list = file.readlines()
trump_pac_list = [x.upper() for x in trump_pac_list]

############## IMPORT BIDEN PACS ###################

file = open('biden_pacs.txt', 'r')
biden_pac_list = file.readlines()
biden_pac_list = [x.upper() for x in biden_pac_list]

df = pandas.read_csv(google_stats)
df["Candidate_Alignment"] = ""

print(df.shape)

# df_filtered = df[df["Advertiser_Name"].Series(trump_pac_list).any()]

# for each in df[df["Regions"]]:
# 	if each == "US":
# 		print (type(each))

# print(df_filtered.shape)
# print(df.head())

######## DROP NON-US REGIONS ################

indexNames = df[df['Regions'] != "US"].index
df.drop(indexNames, inplace=True)
print(df.shape)

df.loc[df["Advertiser_Name"].isin(biden_pac_list), "Candidate_Alignment"] = 'Biden'
df.loc[df["Advertiser_Name"].isin(trump_pac_list), "Candidate_Alignment"] = 'Trump'

print (df)
df.to_csv(google_stats, index=False)
