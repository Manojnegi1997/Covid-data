import pandas as pd

with open('covid_19_data.csv', 'r') as file:
    reader = pd.read_csv(file, delimiter=',')

    # data frame information
    print("complete data frame column name and data type ")
    print(reader.info())

    # case1 populate max death's country wise

    print("case1 populate max death's country wise")
    max_death_con_wise = reader.groupby("Country").max("Deaths").head(10)
    print(max_death_con_wise)

    # case2 populate total recovered

    print("populate total recovered")
    total_recovered = reader["Recovered"].sum()
    print(total_recovered)

    # case3 populate confirmed as per state

    print("populate confirmed as per state")
    confirmed_as_state = reader.groupby(["Country", "State"]).sum("Confirmed")
    print(confirmed_as_state)

    # case4 populate on daily bases how many confirmed cases arrived worldwide

    print("populate on daily bases how many confirmed cases arrived worldwide")
    daily_bases_cases = reader.groupby("ObservationDate").sum("Confirmed")
    print(daily_bases_cases)
