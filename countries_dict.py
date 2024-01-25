import pandas as pd

df_countries = pd.read_csv('all_items_duplicated.csv') 
df_countries = df_countries[df_countries['Collection_Name']=='14 Global intelligence']
country_names = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia",
    "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
    "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi",
    "Côte d'Ivoire", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China",
    "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia",
    "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt",
    "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon",
    "Gambia", "Georgia", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
    "Haiti", "Holy See", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
    "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia",
    "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi",
    "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia",
    "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Burma", "Namibia",
    "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Republic of the Niger", "Nigeria", "North Korea", "North Macedonia",
    "Norway", "Oman", "Pakistan", "Palau", "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru",
    "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
    "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
    "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia",
    "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
    "Syria", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia",
    "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates",
    "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe", 'Belgium', 'Kosovo', 'Yugoslavia','Mi̇lli̇ İsti̇hbarat Teşki̇latı', 
    'Belgian','Turkish', 'Ottoman Special Organization', 'Belgian', 'Portuguese', 'Chinese', 'Greek', 'Spanish', 'French', 'Canadian', 'Czechoslovak', 'Soviet','Polish', 'KGB',
    'FSB', 'Dutch', 'German', 'Mossad', 'Norwegian', 'Ottoman', 'Italian', 'Teşkilat-ı Mahsusa', 'Tsar', 'ACADEMIC INTELLIGENCE – A PLURIVALENT CONCEPT',
    'Vichy Regime','Safavids','Hungarian','Austro','Swedish','Nasser','Jewish','Finnish', 'Christofascism','Venice', 'Abdülhamid','Czechoslovakia', 'Third Reich', 'Kriegsmarine',
    'Bundesnachrichtendienst','Vappala Balachandran', 'Andropov', 'Kosova', 'Yom Kippur', "The Spy who Fell to Earth: My Relationship with the Secret Agent who Rocked the Middle East",
    "The Politics and Intelligence of the Oslo Peace Process", 'Shin bet','Sixteenth-Century Istanbul', 'Cheka','Arabizing the Omani intelligence services: Clash of cultures',
    'Putin', 'New memoirs from Moscow', "Mao's Secret"
]
replacements = {
    'Arabizing the Omani intelligence services: Clash of cultures':'Oman',
    'Belgian': 'Belgium',
    'Turkish': 'Turkey',
    'Portuguese': 'Portugal',
    'Chinese': 'China',
    'Greek': 'Greece',
    'Spanish': 'Spain',
    'French': 'France',
    'Canadian': 'Canada',
    'Czechoslovak': 'Czechia',
    'Mi̇lli̇ İsti̇hbarat Teşki̇latı': 'Turkey',
    'Soviet': 'Russia',
    'Polish': 'Poland',
    'FSB': 'Russia',
    'Dutch': 'Netherlands', 
    'German': 'Germany',
    'Germany':'Germany',
    'Mossad': 'Israel',
    'Norwegian': 'Norway',
    'Ottoman Special Organization':'Turkey',
    r'\bOttoman\b':'Turkey',
    'Italian':'Italy',
    'KGB':'Russia',
    'Teşkilat-ı Mahsusa':'Turkey',
    'Tsar':'Russia',
    'ACADEMIC INTELLIGENCE – A PLURIVALENT CONCEPT':'Romania',
    'Vichy Regime':'France',
    'Safavids':'Iran',
    'Hungarian':'Hungary',
    'Austro':'Austria',
    'Swedish':'Sweden',
    'Nasser':'Egypt',
    'Jewish':'Israel',
    'Finnish':'Finland',
    'Christofascism':'Romania',
    'Venice':'Italy',
    'Abdülhamid':'Turkey',
    'Czechoslovakia':'Czechia',
    'Third Reich':'Germany',
    'Kriegsmarine':'Germany',
    'Bundesnachrichtendienst':'Germany',
    'Vappala Balachandran':'India',
    'Andropov':'Russia',
    'Kosova':'Kosovo',
    'Yom Kippur':'Israel',
    "The Spy who Fell to Earth: My Relationship with the Secret Agent who Rocked the Middle East":"Israel",
    "The Politics and Intelligence of the Oslo Peace Process":'Israel',
    'Shin bet':'Israel',
    'Sixteenth-Century Istanbul':'Turkey',
    'Cheka':'Russia',
    'Putin':'Russia',
    'New memoirs from Moscow':'Russia',
    "Mao's Secret":'China',
    'Burma':'Myanmar'
    }

replacements['\\bOttoman\\b'] = 'Turkey'
replacements['\\bRomania\\b'] = 'Romania'

df_countries['Country'] = ''
# afghanistan_title_mask = df_countries['Title'].str.lower() == 'canadian military intelligence in afghanistan'
# df_countries.loc[afghanistan_title_mask, 'Country'] = 'Canada'
afghanistan_title_mask_2 = df_countries['Title'].str.lower() == 'canadian Military Intelligence: Operations and Evolution from the October Crisis to the War in Afghanistan'
df_countries.loc[afghanistan_title_mask_2, 'Country'] = 'Canada'

for country in country_names:
    if country.lower() == 'oman':
        # Special handling for 'Oman' to avoid categorizing 'Ottoman' titles under 'Oman'
        mask = df_countries['Title'].str.lower().str.contains(r'\bOman\b', regex=True)
    elif country.lower() == 'omani':
        mask = df_countries['Title'].str.lower().str.contains(r'\bOmani\b', regex=True)
    else:
        mask = df_countries['Title'].str.lower().str.contains(country.lower(), regex=False)
        
    df_countries.loc[mask, 'Country'] += country + '|' if not df_countries.loc[mask, 'Country'].empty else ''

df_countries['Country'] = df_countries['Country'].str.rstrip('|').replace(replacements, regex=True)
df_countries = df_countries.assign(Country=df_countries['Country'].str.split('|')).explode('Country')
df_countries = df_countries.drop_duplicates(subset=['Country', 'Zotero link'])
df_countries['Country'].replace('', 'Country not known', inplace=True) 

continent_country_names = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia",
    "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
    "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi",
    "Côte d'Ivoire", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China",
    "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia",
    "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt",
    "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon",
    "Gambia", "Georgia", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
    "Haiti", "Holy See", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
    "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia",
    "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi",
    "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia",
    "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (formerly Burma)", "Namibia",
    "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Republic of the Niger", "Nigeria", "North Korea", "North Macedonia",
    "Norway", "Oman", "Pakistan", "Palau", "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru",
    "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
    "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
    "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia",
    "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
    "Syria", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia",
    "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates",
    "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe", 'Belgium', 'Kosovo', 'Yugoslavia','Mi̇lli̇ İsti̇hbarat Teşki̇latı', 
    'Belgian','Turkish', 'Ottoman Special Organization', 'Belgian',  'Portuguese', 'Chinese', 'Greek', 'Spanish', 'French', 'Canadian', 'Czechoslovak', 'Soviet','Polish', 'KGB',
    'FSB', 'Dutch', 'German', 'Mossad', 'Norwegian', 'Ottoman', 'Italian', 'Teşkilat-ı Mahsusa', 'Tsar', 'ACADEMIC INTELLIGENCE – A PLURIVALENT CONCEPT',
    'Vichy Regime','Safavids','Hungarian','Austro','Swedish','Nasser','Jewish','Finnish','Africa','Asia','Arab','South America','Medina','Eastern Europe',
    'Latin America','Venice', 'Christofascism','Abdülhamid','Czechoslovakia', 'Third Reich','Kriegsmarine','Bundesnachrichtendienst', 'Vappala Balachandran','Andropov',
    'Kosova', 'Yom Kippur', 'The Spy who Fell to Earth: My Relationship with the Secret Agent who Rocked the Middle East', "The Politics and Intelligence of the Oslo Peace Process",
    'Shin bet','Sixteenth-Century Istanbul','Cheka', 'Omani','Putin','New memoirs from Moscow',"Mao's Secret"
]
continent_replacements = {
    'Belgian': 'Belgium', 
    'Turkish': 'Turkey',
    'Portuguese': 'Portugal',
    'Chinese': 'China',
    'Greek': 'Greece',
    'Spanish': 'Spain',
    'French': 'France',
    'Canadian': 'Canada',
    'Czechoslovak': 'Czechia',
    'Mi̇lli̇ İsti̇hbarat Teşki̇latı': 'Turkey',
    'Soviet': 'Russia',
    'Polish': 'Poland',
    'FSB': 'Russia',
    'Dutch': 'Netherlands',
    'German': 'Germany',
    'Germany':'Germany',
    'Mossad': 'Israel',
    'Norwegian': 'Norway',
    'Ottoman Special Organization':'Turkey',
    'Ottoman':'Turkey',
    'Italian':'Italy',
    'KGB':'Russia',
    'Teşkilat-ı Mahsusa':'Turkey',
    'Tsar':'Russia',
    'ACADEMIC INTELLIGENCE – A PLURIVALENT CONCEPT':'Romania',
    'Vichy Regime':'France',
    'Safavids':'Iran',
    'Hungarian':'Hungary',
    'Austro':'Austria',
    'Swedish':'Sweden',
    'Nasser':'Egypt',
    'Jewish':'Israel',
    'Finnish':'Finland',
    'Medina':'Saudi Arabia',
    'Venice':'Italy',
    'Christofascism':'Romania',
    'Abdülhamid':'Turkey',
    'Czechoslovakia':'Czechia',
    'Third Reich':'Germany',
    'Kriegsmarine':'Germany',
    'Bundesnachrichtendienst':'Germany',
    'Vappala Balachandran':'India',
    'Andropov':'Russia',
    'Kosova':'Kosovo',
    'Yom Kippur':'Israel',
    "The Spy who Fell to Earth: My Relationship with the Secret Agent who Rocked the Middle East":"Israel",
    "The Politics and Intelligence of the Oslo Peace Process":'Israel',
    'Shin bet':'Israel',
    'Sixteenth-Century Istanbul':'Turkey',
    'Cheka':'Russia',
     'Omani':'Oman',
     'Putin':'Russia',
     'New memoirs from Moscow':'Russia',
     "Mao's Secret":'China',
     'Burma':'Myanmar'
    }

df_continent = df_countries.copy()
df_continent['Country2'] = ''

for continent in continent_country_names:
    # mask = df_continent['Title'].str.contains(continent, regex=False)
    mask = df_continent['Title'].str.lower().str.contains(continent.lower(), regex=False)
    df_continent.loc[mask, 'Country2'] += continent + '|' if not df_continent.loc[mask, 'Country2'].empty else ''

df_continent['Country2'] = df_continent['Country2'].str.rstrip('|').replace(continent_replacements, regex=True)
df_continent = df_continent.assign(Country2=df_continent['Country2'].str.split('|')).explode('Country2')
df_continent = df_continent.drop_duplicates(subset=['Country2', 'Zotero link'])
df_continent['Country2'].replace('', 'Country2 not known', inplace=True)

continent_dict = { 
    "Africa":"Africa",
    'Eastern Europe':'Europe',
    "Asia":"Asia",
    'Latin America':'South America',
    'Arab':'Asia',
    'South America':'South America',
    "Afghanistan": "Asia",
    "Albania": "Europe",
    "Algeria": "Africa",
    "Andorra": "Europe",
    "Angola": "Africa",
    "Antigua and Barbuda": "North America",
    "Argentina": "South America",
    "Armenia": "Asia",
    "Australia": "Oceania",
    "Austria": "Europe",
    "Azerbaijan": "Asia",
    "Bahamas": "North America",
    "Bahrain": "Asia",
    "Bangladesh": "Asia",
    "Barbados": "North America",
    "Belarus": "Europe",
    "Belgium": "Europe",
    "Belize": "North America",
    "Benin": "Africa",
    "Bhutan": "Asia",
    "Bolivia": "South America",
    "Bosnia and Herzegovina": "Europe",
    "Botswana": "Africa",
    "Brazil": "South America",
    "Brunei": "Asia",
    "Bulgaria": "Europe",
    "Burkina Faso": "Africa",
    "Burundi": "Africa",
    "Côte d'Ivoire": "Africa",
    "Cabo Verde": "Africa",
    "Cambodia": "Asia",
    "Cameroon": "Africa",
    "Canada": "North America",
    "Central African Republic": "Africa",
    "Chad": "Africa",
    "Chile": "South America",
    "China": "Asia",
    "Colombia": "South America",
    "Comoros": "Africa",
    "Congo (Congo-Brazzaville)": "Africa",
    "Costa Rica": "North America",
    "Croatia": "Europe",
    "Cuba": "North America",
    "Cyprus": "Asia",
    "Czechia": "Europe",
    "Democratic Republic of the Congo": "Africa",
    "Denmark": "Europe",
    "Djibouti": "Africa",
    "Dominica": "North America",
    "Dominican Republic": "North America",
    "Ecuador": "South America",
    "Egypt": "Africa",
    "El Salvador": "North America",
    "Equatorial Guinea": "Africa",
    "Eritrea": "Africa",
    "Estonia": "Europe",
    "Eswatini": "Africa",
    "Ethiopia": "Africa",
    "Fiji": "Oceania",
    "Finland": "Europe",
    "France": "Europe",
    "Gabon": "Africa",
    "Gambia": "Africa",
    "Georgia": "Europe",
    "Germany": "Europe",
    "Ghana": "Africa",
    "Greece": "Europe",
    "Grenada": "North America",
    "Guatemala": "North America",
    "Guinea": "Africa",
    "Guinea-Bissau": "Africa",
    "Guyana": "South America",
    "Haiti": "North America",
    "Holy See": "Europe",
    "Honduras": "North America",
    "Hungary": "Europe",
    "Iceland": "Europe",
    "India": "Asia",
    "Indonesia": "Asia",
    "Iran": "Asia",
    "Iraq": "Asia",
    "Ireland": "Europe",
    "Israel": "Asia",
    "Italy": "Europe",
    "Jamaica": "North America",
    "Japan": "Asia",
    "Jordan": "Asia",
    "Kazakhstan": "Asia",
    "Kenya": "Africa",
    "Kiribati": "Oceania",
    "Kuwait": "Asia",
    "Kyrgyzstan": "Asia",
    "Laos": "Asia",
    "Latvia": "Europe",
    "Lebanon": "Asia",
    "Lesotho": "Africa",
    "Liberia": "Africa",
    "Libya": "Africa",
    "Liechtenstein": "Europe",
    "Lithuania": "Europe",
    "Luxembourg": "Europe",
    "Madagascar": "Africa",
    "Malawi": "Africa",
    "Malaysia": "Asia",
    "Maldives": "Asia",
    "Mali": "Africa",
    "Malta": "Europe",
    "Marshall Islands": "Oceania",
    "Mauritania": "Africa",
    "Mauritius": "Africa",
    "Mexico": "North America",
    "Micronesia": "Oceania",
    "Moldova": "Europe",
    "Monaco": "Europe",
    "Mongolia": "Asia",
    "Montenegro": "Europe",
    "Morocco": "Africa",
    "Mozambique": "Africa",
    "Myanmar": "Asia",
    "Burma": "Asia",
    "Namibia": "Africa",
    "Nauru": "Oceania",
    "Nepal": "Asia",
    "Netherlands": "Europe",
    "New Zealand": "Oceania",
    "Nicaragua": "North America",
    "Niger": "Africa",
    "Nigeria": "Africa",
    "North Korea": "Asia",
    "North Macedonia": "Europe",
    "Norway": "Europe",
    "Oman": "Asia",
    "Pakistan": "Asia",
    "Palau": "Oceania",
    "Palestine State": "Asia",
    "Panama": "North America",
    "Papua New Guinea": "Oceania",
    "Paraguay": "South America",
    "Peru": "South America",
    "Philippines": "Asia",
    "Poland": "Europe",
    "Portugal": "Europe",
    "Qatar": "Asia",
    "Romania": "Europe",
    "Russia": "Asia",
    "Rwanda": "Africa",
    "Saint Kitts and Nevis": "North America",
    "Saint Lucia": "North America",
    "Saint Vincent and the Grenadines": "North America",
    "Samoa": "Oceania",
    "San Marino": "Europe",
    "Sao Tome and Principe": "Africa",
    "Saudi Arabia": "Asia",
    "Senegal": "Africa",
    "Serbia": "Europe",
    "Seychelles": "Africa",
    "Sierra Leone": "Africa",
    "Singapore": "Asia",
    "Slovakia": "Europe",
    "Slovenia": "Europe",
    "Solomon Islands": "Oceania",
    "Somalia": "Africa",
    "South Africa": "Africa",
    "South Korea": "Asia",
    "South Sudan": "Africa",
    "Spain": "Europe",
    "Sri Lanka": "Asia",
    "Sudan": "Africa",
    "Suriname": "South America",
    "Sweden": "Europe",
    "Switzerland": "Europe",
    "Syria": "Asia",
    "Tajikistan": "Asia",
    "Tanzania": "Africa",
    "Thailand": "Asia",
    "Timor-Leste": "Asia",
    "Togo": "Africa",
    "Tonga": "Oceania",
    "Trinidad and Tobago": "North America",
    "Tunisia": "Africa",
    "Turkey": "Asia",
    "Turkmenistan": "Asia",
    "Tuvalu": "Oceania",
    "Uganda": "Africa",
    "Ukraine": "Europe",
    "United Arab Emirates": "Asia",
    "United Kingdom": "Europe",
    "United States of America": "North America",
    "Uruguay": "South America",
    "Uzbekistan": "Asia",
    "Vanuatu": "Oceania",
    "Venezuela": "South America",
    "Vietnam": "Asia",
    "Yemen": "Asia",
    "Zambia": "Africa",
    "Zimbabwe": "Africa",
    'Belgium': 'Europe',
    'Kosovo': 'Europe',
    'Yugoslavia': 'Europe',
    "Taiwan's":'Asia'
}

def get_continent(country):
    return continent_dict.get(country, 'Unknown')

# Create 'Continent' column using the function
df_continent['Continent'] = df_continent['Country2'].apply(get_continent)