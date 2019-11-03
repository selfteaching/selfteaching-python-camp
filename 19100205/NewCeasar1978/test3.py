import pandas as pd

for i in range(10):
    locals()['df' + str(i)] = pd.DataFrame()
    print(locals()['df' + str(i)].shape)