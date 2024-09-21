
!pip install plotly
import streamlit as st
import plotly.graph_objects as go

# Title and description
st.title("Tourism Initiatives and Tourism Index by Governorate")
st.write("""
This dashboard presents two barchart related to tourism across various governorates. The first barchart presents the existance of tourism inititve when we have touristic attraction. the second barchart presents us the tousim index by governorate.
""")

# Interactivity: Select which variables to show in the first bar plot
st.sidebar.header("Customize Visualizations")
show_initiatives = st.sidebar.checkbox("Show Tourism Initiatives", True)
show_attractions = st.sidebar.checkbox("Show Tourist Attractions", True)

# First Visualization: Tourism Initiatives and Attractions by Governorate
st.subheader("Tourism Initiatives and Tourist Attractions by Governorate")
if show_initiatives or show_attractions:
    governorates = ["Akkar", "Aley", "Baabda", "Baalbek-Hermel", "Batroun", "Bint Jbeil", "Byblos", "Hasbaya"]
    initiatives_data = [30, 15, 12, 18, 8, 5, 20, 7]
    attractions_data = [10, 8, 6, 7, 4, 2, 10, 3]

    fig1 = go.Figure()

    if show_initiatives:
        fig1.add_trace(go.Bar(
            x=governorates,
            y=initiatives_data,
            name='Existence of initiatives',
            marker_color='indianred'
        ))

    if show_attractions:
        fig1.add_trace(go.Bar(
            x=governorates,
            y=attractions_data,
            name='Existence of tourist attractions',
            marker_color='blue'
        ))

    fig1.update_layout(barmode='group', title="Tourism Initiatives and Tourist Attractions by Governorate")
    st.plotly_chart(fig1)

# Insights
st.write("""
### Insights:
- We can see that the higher the existence of ourist attractions the higher the initiative, meaning that the existence of touristic attraction plays a role in facilitating governorate work in having more ideas to enhance the touristic experience when locals and tourists visit. 
- For example, Governorates like **Akkar** and **Byblos** show a higher number of tourism initiatives, indicating significant development efforts in those areas and that is due to the rich history of both governorate.
- As for cases such as Bint Jbeil, we can see a low existence of tourist attractions leading to a lower existence of initiatives.
""")
# Second Visualization
tourism_index_data = [3.5, 3.0, 4.0, 2.5, 4.2, 3.8, 5.0, 2.7]
# Interactivity
selected_governorates = st.sidebar.multiselect(
    "Select Governorates to Display",
    options=governorates,
    default=governorates
)

# Filter the tourism index data based on the selected governorates
filtered_governorates = []
filtered_tourism_index = []

# Filtering based on selected governorates
for gov, index in zip(governorates, tourism_index_data):
    if gov in selected_governorates:
        filtered_governorates.append(gov)
        filtered_tourism_index.append(index)

# Second Visualization: Average Tourism Index by Governorate
st.subheader("Average Tourism Index by Governorate")
fig2 = go.Figure(data=go.Bar(
    x=filtered_governorates,  # Use filtered governorates
    y=filtered_tourism_index,  # Use filtered tourism index
    marker=dict(
        color=filtered_tourism_index,
        colorscale='Viridis'
    )
))

fig2.update_layout(
    title="Average Tourism Index by Governorate",
    xaxis_title="Governorate",
    yaxis_title="Average Tourism Index",
    coloraxis_colorbar=dict(title="Index"),
    width=1000,
    height=500
)

st.plotly_chart(fig2)

# Insights Section
st.write("""
### Insights:
- The Tourism index is calculated based on the number of touristic attractions, number of restaurants, coffeshops, hotels and guesthouses. therefre the higher the number of each previously mentioned location the higher their average.
- Byblos, due to its rich history being one of the oldest city and one of the most recommended cities to visit when visiting Lebanon has the highest tourism index, being one of the main cities under the Phoenician era.
- Batroun, recently became one of the hottest touristic attractions due its beaches and nightlife even with little touristic attarctions, they have one of the highest touristic indexes that is due to number of restaurants, hotels guest houses available in the city.

""")
