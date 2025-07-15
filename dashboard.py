import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Car Dashboard")
st.write("This dashboard provides insights into car data.")

# Load the dataset
df = sns.load_dataset("car_crashes")
df



# Add region column to the dataframe
df['region'] = pd.cut(df['total'], bins=[0, 10, 20, 30, 40], labels=['Low', 'Moderate', 'High', 'Very High'])

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Data")
regions = df['region'].cat.categories.tolist()
selected_regions = st.sidebar.multiselect("Select Region(s):", regions, default=regions)
states = df['abbrev'].unique().tolist()
selected_states = st.sidebar.multiselect("Select State(s):", states, default=states)

# Filter the dataframe
filtered_df = df[df['region'].isin(selected_regions) & df['abbrev'].isin(selected_states)]

# Show filtered data
st.dataframe(filtered_df)
# --- DASHBOARD VISUALIZATIONS ---
st.header("Dashboard Visualizations")


# Bar chart: Total crashes by region
st.subheader("Total Crashes by Region")
fig1 = px.bar(df.groupby('region')['total'].sum().reset_index(), x='region', y='total', title='Total Crashes by Region')
st.plotly_chart(fig1)
fig1.update_traces(marker_color="#9a0840")  

#Total Acccident by states
fig = px.bar(df,x='abbrev',y='total',
             title = "Total Accidents by State",
             labels = {'abbrev': 'state','total': 'Total Accidents'},
             color='total',
             color_continuous_scale='Blues')
st.plotly_chart(fig)



# Scatter plot: Speeding vs. Alcohol involvement
st.subheader("Speeding vs. Alcohol Involvement")
fig2 = px.scatter(df, x='speeding', y='alcohol', color='region', title='Speeding vs. Alcohol Involvement')
st.plotly_chart(fig2)

#Scattered chart(to find relations)
#Alcohol vs Speeding
fig = px.scatter(df,x ='speeding', y = 'alcohol',
                 color='abbrev',
                 size = 'total',
                 title='Speeding vs Alcohol Involment in Accident',
                 labels={'Speeding': 'Speeding Accidents','alcohol': 'Alcohol Involment'})
fig.update_layout(title={'x':0.5}) # for centering the labels
st.plotly_chart(fig)


# Pie chart: Proportion of crashes by region
st.subheader("Proportion of Crashes by Region")
region_counts = df['region'].value_counts().reset_index()
region_counts.columns = ['region', 'count']
fig3 = px.pie(region_counts, names='region', values='count', title='Proportion of Crashes by Region')
st.plotly_chart(fig3)


#Bar plot of speeding, alcohol, and not distracted accidents by state
st.subheader("Animated Comparison of Speeding, Alcohol and Not Distracted Accidents")
melted_df = df.melt(id_vars=['abbrev'], value_vars=['speeding','alcohol','not_distracted'])
fig = px.bar(melted_df, x='abbrev', y='value', color='variable',
             animation_frame='variable',
             title='Animated Comparison of Speeding, Alcohol and Not Distracted Accidents',
             labels={'Vlaues':'Percentages'})
st.plotly_chart(fig)




# Box plot: Insurance losses by region
st.subheader("Insurance Losses by Region")
fig5 = px.box(df, x='region', y='ins_premium', title='Insurance Premiums by Region')
st.plotly_chart(fig5)

# Line chart: Average total crashes per state (sorted)
st.subheader("Average Total Crashes per State")
avg_crashes = df.groupby('abbrev')['total'].mean().reset_index().sort_values('total', ascending=False)
fig6 = px.line(avg_crashes, x='abbrev', y='total', title='Average Total Crashes per State')
st.plotly_chart(fig6)


# Violin plot: Speeding by Region
st.subheader("Speeding by Region")
fig9 = px.violin(df, x='region', y='speeding', box=True, points='all', title='Speeding by Region')
st.plotly_chart(fig9)

#Top 10 states by insurances premium
#top10=df.nlargest(10.'ins_premium')
top10= df.sort_values('ins_premium',ascending=False).head(10)
fig=px.bar(top10, x='abbrev',y='ins_premium',color='ins_premium',
           title="Top 10 states by Insurance premium",
           labels={'abbrev':'States','ins_premium':'Insurance Premium'},color_continuous_scale='Viridis')
fig.show()
st.plotly_chart(fig)

# Sunburst chart: Region and State Breakdown by Total Crashes
st.subheader("Region and State Breakdown by Total Crashes")
fig10 = px.sunburst(df, path=['region', 'abbrev'], values='total', title='Region and State Breakdown by Total Crashes')
st.plotly_chart(fig10)

#Total Accident by US States
fig= px.choropleth(df,
                    locations='abbrev',
                    locationmode='USA-states',
                    color='total',
                    title='Total Accidents by US States',
                )
fig.show()
st.plotly_chart(fig)

#Insurance by region
fig = px.box(df, x='region' ,y='ins_premium',
             title = "Insurance Premium by Region",
             color='region')
fig.show()
st.plotly_chart(fig)






