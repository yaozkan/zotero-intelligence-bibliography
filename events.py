import pandas as pd 
from streamlit_gsheets import GSheetsConnection


conn = st.connection("gsheets", type=GSheetsConnection)

# Read the first spreadsheet
df_gs = conn.read(spreadsheet='https://docs.google.com/spreadsheets/d/10ezNUOUpzBayqIMJWuS_zsvwklxP49zlfBWsiJI6aqI/edit#gid=0')

# Read the second spreadsheet
df_forms = conn.read(spreadsheet='https://docs.google.com/spreadsheets/d/10ezNUOUpzBayqIMJWuS_zsvwklxP49zlfBWsiJI6aqI/edit#gid=1941981997')
df_forms = df_forms.rename(columns={'Event name':'event_name', 'Event organiser':'organiser','Link to the event':'link','Date of event':'date', 'Event venue':'venue', 'Details':'details'})
df_forms = df_forms.drop(columns=['Timestamp'])

# Convert and format dates in df_gs
df_gs['date'] = pd.to_datetime(df_gs['date'])
df_gs['date_new'] = df_gs['date'].dt.strftime('%Y-%m-%d')

# Convert and format dates in df_forms
df_forms['date'] = pd.to_datetime(df_forms['date'])
df_forms['date_new'] = df_forms['date'].dt.strftime('%Y-%m-%d')
df_forms['month'] = df_forms['date'].dt.strftime('%m')
df_forms['year'] = df_forms['date'].dt.strftime('%Y')
df_forms['month_year'] = df_forms['date'].dt.strftime('%Y-%m')
df_forms.sort_values(by='date', ascending=True, inplace=True)
df_forms = df_forms.drop_duplicates(subset=['event_name', 'link', 'date'], keep='first')

# Fill missing values in df_forms
df_forms['details'] = df_forms['details'].fillna('No details')
df_forms = df_forms.fillna('')

# Concatenate df_gs and df_forms
df_gs = pd.concat([df_gs, df_forms], axis=0)
df_gs = df_gs.reset_index(drop=True)
df_gs = df_gs.drop_duplicates(subset=['event_name', 'link', 'date'], keep='first')

# Sort the concatenated dataframe by date_new
df_gs = df_gs.sort_values(by='date_new', ascending=True)

# Filter events happening today or in the future
today = dt.date.today()
df_gs['date'] = pd.to_datetime(df_gs['date'], dayfirst=True)  # Ensure 'date' is datetime
filter = df_gs['date'] >= pd.to_datetime(today)
df_gs = df_gs[filter]

# Display the filtered dataframe
df_gs = df_gs.loc[filter]
df_gs = df_gs.fillna('')
df_gs = df_gs.head(3)
if df_gs['event_name'].any() in ("", [], None, 0, False):
    st.write('No upcoming event!')
df_gs1 = ('['+ df_gs['event_name'] + ']'+ '('+ df_gs['link'] + ')'', organised by ' + '**' + df_gs['organiser'] + '**' + '. Date: ' + df_gs['date_new'] + ', Venue: ' + df_gs['venue'])
row_nu = len(df_gs.index)
for i in range(row_nu):
    st.write(''+str(i+1)+') '+ df_gs1.iloc[i])
st.write('Visit the [Events on intelligence](https://intelligence.streamlit.app/Events) page to see more!')

st.markdown('##### Next conference')
df_con = conn.read(spreadsheet='https://docs.google.com/spreadsheets/d/10ezNUOUpzBayqIMJWuS_zsvwklxP49zlfBWsiJI6aqI/edit#gid=939232836')
df_con['date'] = pd.to_datetime(df_con['date'])
df_con['date_new'] = df_con['date'].dt.strftime('%Y-%m-%d')
df_con['date_new'] = pd.to_datetime(df_con['date'], dayfirst = True).dt.strftime('%d/%m/%Y')
df_con['date_new_end'] = pd.to_datetime(df_con['date_end'], dayfirst = True).dt.strftime('%d/%m/%Y')
df_con.sort_values(by='date', ascending = True, inplace=True)
df_con['details'] = df_con['details'].fillna('No details')
df_con['location'] = df_con['location'].fillna('No details')
df_con = df_con.fillna('')
df_con['date_end'] = pd.to_datetime(df_con['date'], dayfirst=True)     
filter = df_con['date_end']>=pd.to_datetime(today)
df_con = df_con.loc[filter]
df_con = df_con.head(1)
if df_con['conference_name'].any() in ("", [], None, 0, False):
    st.write('No upcoming conference!')
df_con1 = ('['+ df_con['conference_name'] + ']'+ '('+ df_con['link'] + ')'', organised by ' + '**' + df_con['organiser'] + '**' + '. Date(s): ' + df_con['date_new'] + ' - ' + df_con['date_new_end'] + ', Venue: ' + df_con['venue'])
row_nu = len(df_con.index)
for i in range(row_nu):
    st.write( df_con1.iloc[i])
st.write('Visit the [Events on intelligence](https://intelligence.streamlit.app/Events) page to see more!')