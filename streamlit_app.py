import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Idly')
streamlit.text('Pesarattu Upma')
streamlit.text('Dosa')
streamlit.text('🥑 Avacado toast')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("pick some fruits", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)

