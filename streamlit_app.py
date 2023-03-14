import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Idly')
streamlit.text('Pesarattu Upma')
streamlit.text('Dosa')
streamlit.text('🥑 Avacado toast')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("pick some fruits", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

import requests

streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"Kiwi")


# create a dataframe with pandas using json_normalize api
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display the dataframe on streamlit
streamlit.dataframe(fruityvice_normalized)
