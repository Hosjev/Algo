"""From the dataset labelled do:
1. read file into generator
2. split each line into list of values
3. extract column names
4. use column names and lists to create dictionary
5. filter out rounds NOT a
6. To get "a" round average and total.

permalink,company,numEmps,category,city,state,fundedDate,raisedAmt,raisedCurrency,round
digg,Digg,60,web,San Francisco,CA,1-Dec-06,8500000,USD,b
"""

curr_wd = "/home/wendiw/Xenial_Backup/PythonPlay"
file_to_read = f"{curr_wd}/Generators/dataset1.csv"

# most of my version is list comprehension, less code but not as readable ie-
#lines = [entry.rstrip().split(",") for entry in gen_data]
# build a dict of headers keys to list of column values by index
#dd = {col_headers[col_num] : [line[col_num] for line in lines] for col_num in range(len(col_headers))}
#build an index of column numbers then if data dict column number value is "a" get amount
#sum_amt = sum(int(dd.get("raisedAmt")[col_num]) for col_num in range(len(dd.get("round"))) if dd.get("round")[col_num] == "a")

#create gen
gen_data = (line for line in open(file_to_read, "r"))
headers = next(gen_data)
col_headers = headers.rstrip().split(",")

# gen an object of lists
lines = (entry.rstrip().split(",") for entry in gen_data)
# gen an object of dicts
data = (dict(zip(col_headers, line)) for line in lines)

round_data = (
    (entry.get("company"), int(entry.get("raisedAmt")))
    for entry in data
    if entry.get("round") == "a"
)

# Now iterate through data and build a dict on unique names
ca_dict = {}
for (c,a) in round_data:
    if ca_dict.__contains__(c):
        ca_dict[c] = ca_dict[c] + a
    else:
        ca_dict[c] = a

total_amt = sum(v for (k,v) in ca_dict.items())

print(f"The total collected monies for round 'a' is: {total_amt:,.2f}")
for k,v in ca_dict.items():
    print(f"Company {k} total/average: ${v:,.2f} -- %{v/total_amt*100:.2f}")
