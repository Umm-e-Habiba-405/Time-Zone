import streamlit as st 
from datetime import datetime
from zoneinfo import ZoneInfo 
TIME_ZONES = [
    'UTC',
    'Asia/Karachi',
    'America/New_York',
    'Europe/London',
    'Australia/Sydney',
    'Pacific/Auckland',
    'Africa/Cairo',
    'America/Chicago',
    'Asia/Tokyo',
    'Europe/Paris',
    'Australia/Perth',
    'Africa/Nairobi',
    'America/Los_Angeles',
    'Asia/Shanghai',
    'Europe/Berlin',
    'Australia/Brisbane',
    'Africa/Johannesburg',

    ]
st.title("Time Zone App")
selected_timezone= st.multiselect("Select time zones",TIME_ZONES,default=['Asia/Karachi'])
st.subheader("Selected Timezone")
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime('%Y-%m-%d %I %H:%M:%S %p')
    st.write(f"**{tz}**: {current_time}")

st.subheader("Convert Time Between Timezones")
current_time = st.time_input("Current Time",value=datetime.now().time())
from_tz = st.selectbox("From timezone",TIME_ZONES,index=0)
to_tz = st.selectbox("To timezone",TIME_ZONES,index=1)
if st.button("Convert Time"):
    dt= datetime.combine(datetime.today(),current_time,tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime('%Y-%m-%d %I %H:%M:%S %p')
    st.success(f"Converted Time zone in{to_tz}:{converted_time}")



