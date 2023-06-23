import streamlit as st
import pandas as pd

if st.button("CLICK ME"):
    df = pd.DataFrame({
        "Name": ["John", "Mary"],
        "Age": [23, 34]
    })
    st.dataframe(df, use_container_width=True)