# recommendation_engine.py
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from data_preparation import load_data, prepare_features

# Load and prepare data
ingredients_path = 'ingredients.json'
recipes_path = 'recipes.json'
ingredients, recipes = load_data(ingredients_path, recipes_path)
cocktails_df = prepare_features(ingredients, recipes)

def calculate_similarity():
    similarity_matrix = cosine_similarity(cocktails_df.values)
    return pd.DataFrame(similarity_matrix, index=cocktails_df.index, columns=cocktails_df.index)

def recommend_cocktails(cocktail_name, top_n=5):
    similarity_matrix = calculate_similarity()
    lower_index_map = {name.lower(): name for name in similarity_matrix.index}
    cocktail_name_lower = cocktail_name.lower()
    if cocktail_name_lower not in lower_index_map:
        return f"No data for cocktail named '{cocktail_name}'."
    actual_name = lower_index_map[cocktail_name_lower]
    similarities = similarity_matrix[actual_name]
    recommended = similarities.sort_values(ascending=False)[1:top_n+1]
    return recommended.index.tolist()
