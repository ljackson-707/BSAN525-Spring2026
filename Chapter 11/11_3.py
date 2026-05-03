# In pandas, a data set is represented as a data frame
# which consists of a set of columns and rows and includes
# many operations that support data analysis

# Each column in a pandas data frame is represented as a series.
# You can find the mean, median, and standard deviation of a column of data


#%%
import pandas as pd
import matplotlib.pyplot as plt

data = {"Course":["CSCI112", "CSCI312", "PHIL258"], "Enrollment":[40, 32, 19]}
frame = pd.DataFrame(data)
print(frame)
frame.plot(marker = 'o', xlabel = "Course", ylabel = "Enrollment")
plt.show()
# %%

