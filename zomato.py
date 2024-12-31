import streamlit as st
import pandas as pd
import pickle

# Page configuration
st.set_page_config(
    page_title="Cuisine Clustering & Chatbot",
    layout="wide",
    page_icon="https://i.pinimg.com/736x/f4/34/e3/f434e30f1c5a170fc4700661cc99c3ab.jpg",
    initial_sidebar_state="expanded"
)
# Add custom theme and font styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;700&display=swap');
    
    .stApp {
        background-color:#dac480;
    .css-10trblm { 
        padding: 20px;
        font-family: 'Montserrat', sans-serif;
    }
    .stSidebar {
        background-color:#da80d9;
    }
    .css-18e3th9 {
        font-family: 'Montserrat', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Load the data and model
data_path = 'clustered data with mapping.csv'
model_path = 'cuisine_kmeans_model.pkl'

# Load the dataset
data = pd.read_csv(data_path)

# Load the KMeans model
with open(model_path, 'rb') as model_file:
    kmeans_model = pickle.load(model_file)

# Normalize cluster column for consistency
data['Mapped_Cuisines'] = data['Mapped_Cuisines'].str.strip().str.lower()

# Streamlit App
def cuisine_clustering_page():
    st.title("🍴Cuisine & City-Based Restaurant Recommendation")

    # # Sidebar for city selection
    st.sidebar.header("Filter Options")
    selected_city = st.sidebar.selectbox(
        "Select a City",
        options=data['City'].dropna().unique()
    )
     has_online_delivary=st.sidebar.selectbox(
        "Has online deliuvary",
        options=data['Has_Online_delivery'].dropna().unique()
    )
    has_table_booking=st.sidebar.selectbox(
        "Has table booking",
        options=data['Has_table_booking'].dropna().unique()
    )
    selected_rating_text = st.sidebar.selectbox(
        "Select Rating Text",
        options=data['Rating_text'].dropna().unique()
    )

    selected_currency = st.sidebar.selectbox(
        "Select Currency",
        options=data['Currency'].dropna().unique()
    )

    # List available cuisine clusters
    # st.markdown("### Available Cuisine Types")
    # available_cuisines = data['Mapped_Cuisines'].str.split(', ').explode().unique()
    # st.write(", ".join(sorted(available_cuisines)))

    # # Text input for cuisine type
    cuisine_input = st.text_input(
        "Enter a Cuisine Type (e.g., North Indian, Italian, Chinese):"
    )

    if cuisine_input:
       # Normalize the input for matching
        cuisine_input = [c.strip().lower() for c in cuisine_input.split(',')]
         

        # Find the corresponding cluster for the user input
        matching_clusters = data[data['Mapped_Cuisines'].str.contains('|'.join(cuisine_input), na=False, case=False)]['Cuisine_Cluster'].unique()

        if len(matching_clusters) == 0:
            st.error("The entered cuisine type does not match available clusters. Please try a valid option.")
            return

        # Filter data based on the selected city and cuisine input
        filtered_data = data[
            (data['City'] == selected_city) &
            (data['Cuisine_Cluster'].isin(matching_clusters))
        ]

        

        st.subheader("Recommended Restaurants")
        if not filtered_data.empty:
            st.dataframe(filtered_data[['Restaurant_id','Restaurant_Name','Cuisines','Price_Range','Average_cost_for_two','Currency',
                                        'Has_Online_delivery','is_delivering_now','Switch_to_order_menu','Has_table_booking',
                                        'City','Address','latitude','longitude','Locality_verbose','Locality',
                                        'Rating_text','Rating_Color','Rating_Votes','Aggregate_rating']])
        else:
            st.write("No restaurants found matching your preferences.")




import google.generativeai as genai
import streamlit as st

def chatbot_page():
    st.title("Google Gemini Chatbot")

    # Set up the Google Gemini chatbot
    api_key = "AIzaSyARWkQgtX-fLng1xBLeAsXzSiGc6ui_t3Y"
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    
    # Input for user to provide a prompt
    prompt = st.chat_input("Enter a question related to chefs, food, or cooking:")

    if prompt is not None:
        # Filter prompts to chef, food, or cooking topics
        keywords = ["chef", "cooking", "food", "recipe", "kitchen", "prepare", "how to make", "cook"]
        if any(keyword in prompt.lower() for keyword in keywords):
            # Generate response from the chatbot
            response = model.generate_content(contents=prompt)

            # Display the chatbot's response
            st.subheader("Response:")
            st.write(response.text)
        else:
            st.warning("The chatbot is designed to answer questions related to chefs, food, or cooking only. Please ask relevant queries.")

            


# Main Page Navigation
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to:", ["Cuisine Clustering", "Chatbot"])

    if page == "Cuisine Clustering":
        cuisine_clustering_page()
    elif page == "Chatbot":
        chatbot_page()

if __name__ == "__main__":
    main()


