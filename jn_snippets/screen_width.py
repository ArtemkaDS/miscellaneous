from pathlib import Path

# Data manipulation
import pandas as pd
import numpy as np
import re
from pprint import pprint

# Options for pandas
pd.set_option('max_colwidth', 200)
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 30)
pd.options.display.precision = 4  # избавиться от научной нотации

# Visualizations
import matplotlib as plt
from matplotlib.pyplot import figure
from IPython.display import display, HTML, Image
display(HTML("<style>.container { width:85% !important; }</style>"))
import warnings
warnings.filterwarnings('ignore')



#path_dir = Path("../data/data_calculated/")
#df_main = pd.read_parquet(Path(path_dir, '20220706_df_main.parquet'))
