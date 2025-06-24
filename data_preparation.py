import json
import pandas as pd
import numpy as np

def load_data(ingredients_path, recipes_path):
    with open(ingredients_path, encoding='utf-8') as file:
        ingredients = json.load(file)
    with open(recipes_path, encoding='utf-8') as file:
        recipes = json.load(file)
    return ingredients, recipes

def prepare_features(ingredients, recipes):
    all_ingredients = list(ingredients.keys())
    cocktails_features = {recipe['name']: np.zeros(len(all_ingredients), dtype=int) for recipe in recipes}
    for recipe in recipes:
        for ingredient in recipe['ingredients']:
            if 'ingredient' in ingredient and ingredient['ingredient'] in all_ingredients:
                index = all_ingredients.index(ingredient['ingredient'])
                cocktails_features[recipe['name']][index] = 1
    return pd.DataFrame.from_dict(cocktails_features, orient='index', columns=all_ingredients)


def save_features(df, path='cocktail_features.csv'):
    df.to_csv(path)

if __name__ == "__main__":
    ingredients_path = 'ingredients.json'
    recipes_path = 'recipes.json'
    ingredients, recipes = load_data(ingredients_path, recipes_path)
    features_df = prepare_features(ingredients, recipes)
    save_features(features_df)
