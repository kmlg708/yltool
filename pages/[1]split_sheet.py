import os

import pandas as pd
import streamlit as st
from pages.tool import yltool as yl

st.write(yl.getfiles(yl.commonpath.sheetdir.value, 'xml'))
