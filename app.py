import streamlit as st
from recommendation_engine import recommend_cocktails

st.title('AI Cocktail Assistant')
st.caption('Discover similar cocktails through shared ingredients and cosine similarity. No LLM is called.')

user_preference = st.text_input('Enter an exact cocktail name', placeholder='Negroni',
                                help='Names are case-sensitive in the current engine. Try Negroni.').strip()

if user_preference:
    recommended_cocktails = recommend_cocktails(user_preference)
    if recommended_cocktails and isinstance(recommended_cocktails, list) and recommended_cocktails != []:
        st.subheader('Recommended Cocktails:')
        # Display each recommended cocktail in a bulleted list
        for cocktail in recommended_cocktails:
            st.markdown(f"- {cocktail}")
    elif isinstance(recommended_cocktails, str):
        # Handle the case where a message is returned instead of a list
        st.write(recommended_cocktails)
    else:
        st.write("No recommendations found. Try another cocktail name from recipes.json.")
