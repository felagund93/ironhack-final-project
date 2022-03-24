import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randint(0, 6, size=(9, 11)),
    columns=['Albert', 'Emilia', 'Florian', 'Francisco', 'Geniva', 'Gonzalo', 'Guillermo', 'Aijay', 'Lydia', 'Pablo', 'Sanja'])

df