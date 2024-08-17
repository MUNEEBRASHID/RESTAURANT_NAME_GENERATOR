import streamlit as st

st.title("Restaurant Name Generator")

Cuisine=st.sidebar.selectbox("Pick a cuisine",("Italian","Mexican","American","Indian","Continental","Chinese","French","Korean","African","Russian","Arabic"))

import langchain_help

if Cuisine:
    response=langchain_help.restaurant_name_and_items_generator(Cuisine)
    st.header(response['restaurant_name'].strip())
    


    st.subheader("Menu")
    menu_items = response['menu_items'].strip().split("\n\n")
    for item in menu_items:
        lines = item.split("\n")
        if len(lines) >= 2:
             # Display item name
            st.markdown(f"**{lines[0].split(': ')[1]}**")
            
            # Display ingredients with colored text
            ingredients_line = lines[1].split(': ')
            if len(ingredients_line) == 2:
                ingredients_keyword = ingredients_line[0]
                ingredients = ingredients_line[1]
                st.markdown(f"<span style='color:yellow;'>{ingredients_keyword}:</span> <span style='color:green;'>{ingredients}</span>", unsafe_allow_html=True)
        
        st.write("")
         

    

