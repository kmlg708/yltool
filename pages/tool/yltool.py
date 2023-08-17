import os

import pandas as pd
import streamlit as st
from enum import Enum


class commonpath(Enum):

    path = "F:\\"
    sheetdir = 'F:\\config'


def getfiles(path,filetpye):
    pathlist=[]
    for root, dirlist, files in os.walk(path):
        for filename in files:
            pathlist.append(os.path.join(root, filename))
    pathlist=[s for s in pathlist if s.endswith(filetpye)]
    return pathlist
