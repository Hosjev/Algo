curr_wd = "/home/wendiw/Documents/PythonPlay"
file_to_read = f"{curr_wd}/generators/dataset1.csv"

# 1st generator--yields one line at a time
lines = (line for line in open(file_to_read))
# 2nd gen--yields a new gen based on each line right stripped and split=list
# a gen of lists
list_line = (s.rstrip().split(",") for s in lines)

# same
cols = next(list_line)
# next gen is a dictifying the cols with data--most interesting thing
# each item yielded is a dict with the key from cols
company_dicts = (dict(zip(cols, data)) for data in list_line)

# the final gen yields an intergized col for col round based on search a
# again this is per line
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a:,.2f}")
