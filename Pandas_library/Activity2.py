import pandas as pd
import numpy as np
df = pd.DataFrame({'Date':['7/10/19', '8/10/19', '9/10/19', '10/10/19', '11/10/19'],
                   'Hours Worked': [7, 7, 7, 7, 7],
                   ' Knowledge acquired on date in percentage': [20, 23, 17, 33 , 7]})
Total_hours = df['Hours Worked'].sum()
df.plot(x ='Date', y= 'Hours Worked', kind = 'bar')
print("You have worked total of ===>", round(Total_hours), "hours")
