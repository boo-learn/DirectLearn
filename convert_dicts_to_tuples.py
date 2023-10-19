data_dicts = [
    {
        'Id': 460174,
        'Name': 'Test API Sandbox campaign 1',
        'State': 'OFF',
        'Status': 'ACCEPTED',
        'Type': 'TEXT_CAMPAIGN'
    },
    {
        'Id': 460175,
        'Name': 'Test API Sandbox campaign 2',
        'State': 'OFF',
        'Status': 'DRAFT',
        'Type': 'TEXT_CAMPAIGN'
    },
    {
        'Id': 460176,
        'Name': 'Test API Sandbox campaign 3',
        'State': 'OFF',
        'Status': 'DRAFT',
        'Type': 'TEXT_CAMPAIGN'
    }
]

data_tupes = []
for comp in data_dicts:
    data_tupes.append(tuple(comp.values()))

print(data_tupes)