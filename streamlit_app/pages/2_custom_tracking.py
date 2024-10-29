import streamlit as st

st.set_page_config()#layout='wide')

options = [
    '1_Auto Privado', 
    '13_Bus',
    '11_Camioneta rural',
    '12_Microbus', 
    '4_Mototaxi', 
    '5_Moto lineal', 
    '9_Omnibus Interprovincial',
    '10_Auto colectivo', 
    '14_Articulado', 
    '2_Cam. PickUp', 
    '3_Taxi',
    '6_Bicicletas',
    '7_Scooter',
    '8_TransportenEscolar Personal',
    '15_TC_Ligeros',
    '16_TC Pesados',
    '17_TC SemiTrailler Trailer',
    '18_Triciclo',
    '19_Ambulancia',
]

st.header("Split Train-Test dataset")
st.image("../data/train_test.png")

st.header("Select Classes")

cols = st.columns(4)

# Display selected options
st.write("Selected options:")

checkbox_states = {}
for i,option in enumerate(options):
    col_index = i % 4
    checkbox_states[option] = cols[col_index].checkbox(option, value=True, key=option)

st.write(checkbox_states.keys())

