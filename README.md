# 🍽️ Restaurant Recommendation System Project 

This is a content-based restaurant recommendation system built for the Cognifyz Machine Learning Internship.

## 🎯 Objective

To recommend restaurants based on user preferences such as:
- Cuisine (e.g., North Indian, Chinese)
- Price Range (1 = Low, 2 = Medium, 3 = High)
- Online Delivery (Yes/No)

## 📂 Dataset

The dataset includes details like:
- Restaurant Name
- Cuisines
- Price range
- Has Online Delivery
- Aggregate Ratings

## ⚙️ Technologies Used

- Python 3.x
- pandas
- scikit-learn (TF-IDF, Cosine Similarity)

## 🛠️ How it Works

1. Prompts user for their preferences.
2. Filters the dataset based on exact matches.
3. Combines relevant fields into a single feature.
4. Uses TF-IDF vectorization and cosine similarity to find top 5 similar restaurants.
5. Displays the most relevant matches.

🚀 Running the Project

git clone https://github.com/ruthikan/-Restaurant_Recommendation
cd Restaurant_Recommendation
python maincode.py

🧪 Sample Output

Enter preferred cuisine (e.g., North Indian, Chinese): Italian
Enter price range (e.g., 1, 2, 3): 2
Do you prefer online delivery? (Yes/No): Yes

Top Recommended Restaurants for You:
...

📝 Author

Ruthika Nalajala
Intern at Cognifyz Technologies
LinkedIn: https://www.linkedin.com/in/ruthika-nalajala-73127628b/

🔖 Tags
#cognifyz #machinelearning #recommendationsystem #internshipproject
