# Chef Mate: Restaurant Clustering & Cooking Guide Application

Project Overview and Objective:

The Chef Mate project is a web-based application designed to solve key challenges in the food and beverage domain. Its primary objective is to provide personalized restaurant recommendations and interactive recipe guidance to enhance the user's dining and cooking experience.

Problem Statement:

The problem revolves around enabling users to discover restaurants that match their preferences (e.g., cuisine, location, cost) while also assisting them in preparing meals through a chatbot. The project tackles the challenges of structuring unorganized data, efficient data preprocessing, and creating a user-friendly application with cloud support.

Step-by-Step Approach:

1.	Unstructured to Structured Data:

o	Transform raw JSON restaurant data into a structured format suitable for analysis and model training.

2.	Data Cleaning and Preprocessing:

o	Handle missing values, remove duplicates, normalize data, and select relevant features for clustering and visualization.

3.	Machine Learning Model Building:

o	Use clustering techniques (K-Means) to group similar restaurants and evaluate the optimal number of clusters.

4.	Streamlit Application:

o	Develop an interactive web application for restaurant recommendations and recipe guidance.

5.	Cooking Assistance Chatbot:

o	AI-powered chatbot integrated for providing detailed recipe guidance and cooking tips.

6.	AWS Cloud Integration:

o	Utilize AWS services for data storage, database management, and application hosting: 

	S3: Store and retrieve raw and cleaned datasets.

	RDS: Maintain structured restaurant data for queries.

	EC2: Host the Streamlit application for real-time access
