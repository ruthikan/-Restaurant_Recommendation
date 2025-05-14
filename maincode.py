import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Dataset
df = pd.read_csv('Dataset .csv')

# Drop rows with missing relevant values
df = df.dropna(subset=['Cuisines', 'Price range', 'Has Online delivery'])
df.reset_index(drop=True, inplace=True)

# Function to recommend restaurants (with strict filtering)
def recommend_restaurants(cuisine_pref, price_range, online_delivery, top_n=5):
    # Filter based on exact match criteria
    filtered_df = df[
    (df['Cuisines'].str.contains(cuisine_pref, case=False, na=False)) &
    (df['Price range'].astype(str) == price_range) &
    (df['Has Online delivery'].str.lower() == online_delivery.lower())].copy() 
    
    if filtered_df.empty:
        return None

    # Create combined features for similarity check
    filtered_df['combined_features'] = (
        filtered_df['Cuisines'].astype(str) + " " +
        filtered_df['Price range'].astype(str) + " " +
        filtered_df['Has Online delivery'].astype(str)
    )

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer(stop_words='english')
    feature_matrix = vectorizer.fit_transform(filtered_df['combined_features'])

    # Prepare user input vector
    user_input = f"{cuisine_pref} {price_range} {online_delivery}"
    user_vector = vectorizer.transform([user_input])

    # Cosine similarity
    similarity_scores = cosine_similarity(user_vector, feature_matrix)
    top_indices = similarity_scores[0].argsort()[-top_n:][::-1]

    # Return top N recommendations
    return filtered_df.iloc[top_indices][['Restaurant Name', 'Cuisines', 'Price range', 'Has Online delivery', 'Aggregate rating']]

# Interactive input
print("Welcome to the Restaurant Recommendation System!")
user_cuisine = input("Enter preferred cuisine (e.g., North Indian, Chinese): ")
user_price = input("Enter price range (e.g., 1 for low, 2 for medium, 3 for high): ")
user_online = input("Do you prefer online delivery? (Yes/No): ")
recommended = recommend_restaurants(user_cuisine, user_price, user_online)
if recommended is not None:
    print("\nTop Recommended Restaurants for You:\n")
    print(recommended.to_string(index=False))
else:
    print("\nNo matching restaurants found for your preferences.")
