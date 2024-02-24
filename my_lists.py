
import random

# related and ordered data
# lists are mutable
us_states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]  # noqa: E501
uk_countries = ["England", "Scotland", "Wales", "Northern Ireland"]
england_counties = ["Bedfordshire", "Berkshire", "Bristol", "Buckinghamshire", "Cambridgeshire", "Cheshire", "City of London", "Cornwall", "Cumbria", "Derbyshire", "Devon", "Dorset", "Durham", "East Riding of Yorkshire", "East Sussex", "Essex", "Gloucestershire", "Greater London", "Greater Manchester", "Hampshire", "Herefordshire", "Hertfordshire", "Isle of Wight", "Kent", "Lancashire", "Leicestershire", "Lincolnshire", "Merseyside", "Norfolk", "North Yorkshire", "Northamptonshire", "Northumberland", "Nottinghamshire", "Oxfordshire", "Rutland", "Shropshire", "Somerset", "South Yorkshire", "Staffordshire", "Suffolk", "Surrey", "Tyne and Wear", "Warwickshire", "West Midlands", "West Sussex", "West Yorkshire", "Wiltshire", "Worcestershire"]  # noqa: E501
australia_states = ["New South Wales", "Queensland", "South Australia", "Tasmania", "Victoria", "Western Australia"]  # noqa: E501
canada_provinces = ["Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador", "Nova Scotia", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan"]  # noqa: E501
# Path: my_lists.py

print(f"The total number of states in the US are {len(us_states)}")
print(f"The total number of states in the UK are {len(uk_countries)}")
print(f"The total number of states in Australia are {len(australia_states)}")
print(f"The total number of states in Canada are {len(canada_provinces)}")
print(F"The total number of counties in England are {len(england_counties)}")

total_english_speaking = us_states + uk_countries + england_counties + australia_states + canada_provinces

print(total_english_speaking)
print(len(total_english_speaking))

us_states.sort()

for state in us_states:
    print(state)

for county in england_counties:
    print(county)

for aus_states in australia_states:
    print(aus_states)

print(f"The total number of counties in England are {len(england_counties)}")
print(f"The last county is {england_counties[-1]}")
print(f"Total number of english speaking jurisdictions are {len(total_english_speaking )}")



for i in range(500):
    myrandom = random.randint(0, 117)
    print(total_english_speaking[myrandom])


total_english_speaking.append("Singapore")
print(f"The first ten are {total_english_speaking[0:10]}")
print(f"The last ten are {total_english_speaking[-10:]}")


total_lists = [us_states, uk_countries, england_counties, australia_states, canada_provinces]

print(total_lists)