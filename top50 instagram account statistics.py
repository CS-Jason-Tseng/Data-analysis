import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('/Users/tsengchunsheng/Library/Mobile Documents/com~apple~CloudDocs/Python study/Example/instagram_top_50_2023-07-03.csv')
pd.set_option('display.max_columns', None)  # display maximum columns
# print(df.head(5))
remove = ['Username']

# remove 'username' column
df = df.drop(columns=remove)

# Data rearrange
df = df.sort_values(['Followers(millions)'], ascending=False)
# print(df)

# -----------------------------------------------

# simple statistics of followers
follower = np.array(df['Followers(millions)'])
min = np.min(follower)
max = np.max(follower)
print(f"Maximum: {max}, Minimum: {min}")
sum = np.sum(follower)
print(f"Sum: {sum}")
mean = np.mean(follower).round()
print(f"Mean: {mean}")
median = np.median(follower).round()
print(f"Median: {median}")
std = np.std(follower).round()
print(f"Standard Deviation: {std}")

# -----------------------------------------------
# visualization for top 50 entries in bar chart

plt.figure(figsize=(12, 8))
# adjust based on the row number
plt.bar(df['Owner'][:50], df['Followers(millions)'][:50], color='skyblue')
# customization
plt.xlabel('Owner', fontdict={'fontname': 'Arial', 'fontsize': 14})
plt.ylabel('Followers (millions)', fontdict={'fontname': 'Arial', 'fontsize': 14})
plt.title('Top 50 Owners with Most Followers on Instagram (July 2023)', fontdict={'fontname': 'Arial', 'fontsize': 24})
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
plt.tight_layout()  # Adjust layout for better appearance

# plot notification text
plt.text(0, 650, 'Max=645')
plt.text(48, 80, 'Min=78.5')

plt.tight_layout()
plt.show()

# -----------------------------------------------
# horizontal bar chart: barh
plt.figure(figsize=(8, 8))
plt.barh(df['Owner'][:50], df['Followers(millions)'][:50], color='skyblue')
plt.gca().invert_yaxis()  # reverse the order of the y-axis labels
plt.xlabel('Followers (millions)', fontdict={'fontname': 'Arial', 'fontsize': 14})
plt.ylabel('Owner', fontdict={'fontname': 'Arial', 'fontsize': 14})
plt.title('Top 50 Owners with Most Followers on Instagram (July 2023)', fontdict={'fontname': 'Arial', 'fontsize': 14})

plt.tight_layout()
plt.show()
# -----------------------------------------------

# groupby analysis
# aggregate followers by profession/activity
profession = df.groupby('Profession/Activity')['Followers(millions)'].sum().reset_index()

# pie chart
plt.figure(figsize=(12, 8))
# font properties
label_font = {'fontsize': 9, 'fontweight': 'normal', 'fontname': 'Arial', 'color': 'black'}
# percent: autopct='%1.1f%%', display order: startangle
plt.pie(profession['Followers(millions)'], labels=profession['Profession/Activity'], autopct='%1.1f%%', startangle=90, textprops=label_font)
plt.title('Followers Distribution by Profession/Activity', fontdict={'fontsize': 16, 'fontweight': 'bold', 'fontname': 'Arial'})

plt.tight_layout()
plt.show()
# -----------------------------------------------

# aggregate followers by Countries
profession = df.groupby('Country')['Followers(millions)'].sum().reset_index()

# pie chart
plt.figure(figsize=(12, 8))
# font properties
label_font = {'fontsize': 9, 'fontweight': 'normal', 'fontname': 'Arial', 'color': 'black'}
# percent: autopct='%1.1f%%', display order: startangle
plt.pie(profession['Followers(millions)'], labels=profession['Country'], autopct='%1.1f%%', startangle=90, textprops=label_font)
plt.title('Followers Distribution by Countries', fontdict={'fontsize': 16, 'fontweight': 'bold', 'fontname': 'Arial'})

plt.tight_layout()
plt.show()
# -----------------------------------------------

# count the occurrences of each country
country_counts = df['Country'].value_counts()
print(country_counts)
# Plot a bar chart for the counts
plt.figure(figsize=(12, 6))
country_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Instagram Owners by Country', fontdict={'fontsize': 16, 'fontweight': 'bold', 'fontname': 'Arial'})
plt.xlabel('Country', fontdict={'fontsize': 12, 'fontweight': 'bold'})
plt.ylabel('Number of Owners', fontdict={'fontsize': 12, 'fontweight': 'bold'})
plt.xticks(rotation=45, ha='right', fontsize=10)

plt.tight_layout()
plt.show()

# -----------------------------------------------
# classify each country to continent
# create dictionary
country_to_continent = {
    'United States': 'North America',
    'India': 'Asia',
    'Canada': 'North America',
    'Spain': 'Europe',
    'Israel': 'Asia',
    'South Korea': 'Asia',
    'United Kingdom': 'Europe',
    'United States Canada': 'North America',
    'Colombia': 'South America',
    'United Kingdom Albania': 'Europe',
    'Thailand': 'Asia',
    'Europe': 'Europe',
    'France': 'Europe',
    'Portugal': 'Europe',
    'Barbados': 'North America',
    'Brazil': 'South America',
    'Trinidad and Tobago United States': 'North America',
    'Argentina': 'South America',
    'Italy Senegal': 'Europe'
}
# add a new column 'Continent' to the DataFrame based on the mapping
df['Continent'] = df['Country'].map(country_to_continent)
df['Count'] = 1
# Sum the number of owners per continent
continent_owner_counts = df.groupby('Continent')['Count'].sum().reset_index()

# plot a bar chart for the sums
plt.figure(figsize=(6, 4))
bars = plt.bar(continent_owner_counts['Continent'], continent_owner_counts['Count'], color='skyblue')
plt.title('Number of Instagram Owners by Continent', fontdict={'fontsize': 16, 'fontweight': 'bold', 'fontname': 'Arial'})
plt.xlabel('Continent', fontdict={'fontsize': 12, 'fontweight': 'bold'})
plt.ylabel('Number of Owners', fontdict={'fontsize': 12, 'fontweight': 'bold'})
plt.xticks(rotation=0, ha='center', fontsize=10)

# add data text on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 1), ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()
# -----------------------------------------------
# classify gender of top 50 insta owner

owner_to_gender = {
    'Instagram': 'Official account',
    'Cristiano Ronaldo': 'Male',
    'Lionel Messi': 'Male',
    'Selena Gomez': 'Female',
    'Kylie Jenner': 'Female',
    'Dwayne Johnson': 'Male',
    'Ariana Grande': 'Female',
    'Kim Kardashian': 'Female',
    'Beyoncé': 'Female',
    'Khloé Kardashian': 'Female',
    'Nike': 'Official account',
    'Justin Bieber': 'Male',
    'Kendall Jenner': 'Female',
    'National Geographic': 'Official account',
    'Taylor Swift': 'Female',
    'Virat Kohli': 'Male',
    'Jennifer Lopez': 'Female',
    'Kourtney Kardashian': 'Female',
    'Nicki Minaj': 'Female',
    'Miley Cyrus': 'Female',
    'Neymar': 'Male',
    'Katy Perry': 'Female',
    'Zendaya': 'Female',
    'Kevin Hart': 'Male',
    'Cardi B': 'Female',
    'Demi Lovato': 'Female',
    'LeBron James': 'Male',
    'Rihanna': 'Female',
    'Chris Brown': 'Male',
    'Real Madrid CF': 'Official account',
    'Ellen DeGeneres': 'Female',
    'Drake': 'Male',
    'FC Barcelona': 'Official account',
    'Billie Eilish': 'Female',
    'UEFA Champions League': 'Official account',
    'Kylian Mbappé': 'Male',
    'Gal Gadot': 'Female',
    'Vin Diesel': 'Male',
    'Lisa': 'Female',
    'NASA': 'Official account',
    'Dua Lipa': 'Female',
    'Priyanka Chopra': 'Female',
    'Shakira': 'Female',
    'NBA': 'Official account',
    'Shraddha Kapoor': 'Female',
    'Snoop Dogg': 'Male',
    'David Beckham': 'Male',
    'Jennie': 'Female',
    'Khaby Lame': 'Male',
    'Gigi Hadid': 'Female'
}
df['Gender'] = df['Owner'].map(owner_to_gender)
gender_count = df['Gender'].value_counts()
print(gender_count)
# from the organized data above, set new variables
gender_statistic = {'Male': 15, 'Female': 27}

# pie chart in percent
plt.figure(figsize=(4, 4))
colors = ['skyblue', 'lightcoral']
explode = (0, 0.1)  # Explode the 2nd slice
label_font = {'fontsize': 12, 'fontweight': 'normal', 'fontname': 'Arial', 'color': 'white'}
patches, texts, autotexts = plt.pie(gender_statistic.values(), explode=explode, labels=gender_statistic.keys(),
                                    autopct='%1.1f%%', colors=colors, textprops=label_font, startangle=120, labeldistance=0.43)
plt.axis('equal')
plt.title('Gender Distribution', fontsize=18, fontweight='bold', fontname='Arial')
plt.suptitle('Based on a Sample of 42 Instagram Accounts', y=0.83, fontsize=10, fontname='Arial', color='gray')
# adjust label positions
for text, autotext in zip(texts, autotexts):
    a, b = text.get_position()
    text.set_position((a, b + 0.07))
    x, y = autotext.get_position()
    autotext.set_position((x, y - 0.07))

plt.tight_layout()
plt.show()
