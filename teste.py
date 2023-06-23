import os

import subprocess



# print(os.getcwd()+'\\'+'app.py')
subprocess.run(f"streamlit run {os.getcwd()+'123'+'app.py'}".replace('123','\\'))