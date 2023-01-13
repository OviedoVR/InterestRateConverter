import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Interest rate Conversion', 
    page_icon='computer', 
    layout="centered", 
    initial_sidebar_state="collapsed", 
    menu_items=None
)

st.markdown('# :dollar: Interest rate conversion')
st.image('cover_pic.png', use_column_width=True)

st.markdown('---')
st.markdown('### :notebook: Equation')
st.latex(r'''(1+i_y)^{1y} = (1+i_m)^{12 m}''')    

st.markdown('---')
st.markdown('### :arrows_counterclockwise: Conversion')

left_col, right_col = st.columns(2)

with left_col:
    selection = st.radio('Convertion type:',
    ('Year to Month', 'Month to Year'), key='option')

with right_col:
    if selection == 'Year to Month':
        number = st.number_input('Enter the interest rate (e.g., 10 % per year):')
        year_rate = float(number/100)

        monthly_rate = round(( (1+year_rate)**(1/12)-1 ) * 100, 2)
        st.markdown(f'Monthly interest rate is: **{monthly_rate} %**')

    elif selection == 'Month to Year':
        number = st.number_input('Enter the interest rate (e.g., 0.7 % per month):')    
        year_rate = float(number/100)

        yearly_rate = round(( (1+year_rate)**(12)-1 ) * 100, 2)
        st.markdown(f'Yearly interest rate is: **{yearly_rate} %**')     

st.sidebar.write('---')
st.sidebar.write(':computer: Developed by Vinícius Oviedo')
st.sidebar.write('2023/01/12')
st.sidebar.write('---')