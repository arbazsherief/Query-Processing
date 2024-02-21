import pandas as pd
import numpy as np
np.random.seed(42)
data = np.random.randn(10, 4)
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3', 'Column4'])
def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'
formatted_df = df.applymap(color_negative_red)
print(formatted_df)
