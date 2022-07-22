from cmath import sqrt
from statistics import variance
import pandas as ps
import seaborn as sb
import matplotlib.pyplot as plt
import math
import scipy.stats

ps.set_option('display.max_rows', 500)
ps.set_option('display.max_columns', 500)
ps.set_option('display.width', 1000)

print("please input the file name, thank you!")
filename = input()


df = ps.read_csv("py/storage/"+filename+".csv")

def hypothesis(df, data, test, hyp):
    if(test == "confInt"):
        sample_mean = df[data].mean()
        sample_count = df[data].count()
        sample_var = variance(df[data])
        std_div = sqrt(sample_var)
        conf = 1.96*(std_div/sample_count)
        top = sample_mean+conf
        bottom = sample_mean - conf
        print("There is a 95% chance that the "+data+" lies between "+str(top)+" and "+str(bottom))

while True:
    print("please input your command, input Help to see the list of commands")
    useinput = input()

    if(useinput == "Help"):
        print("Type Mean to see the data mean\nType Standard Deviation to see the standard deviation of the data\nType Correlation Matrix for operations related to the data correlation matrix\nType EDA for EDA data operations\nType Visualize to see some visual representations about the relationship between the different data\nType Distribution to see the histogram distribution of the data")
    if(useinput == "End"):
        break
    if(useinput == "Mean"):
        print("What data would you like to use")
        data = input()
        print(df[data].mean())
    if(useinput == "Standard Deviation"):
        print("What data would you like to use")
        data = input()
        sample_var = variance(df[data])
        std_div = sqrt(sample_var)
        print(std_div)
    if(useinput == "Correlation Matrix"):
        corrMatrix = df.corr()
        print("Would like the visual representation?")
        visinput = input()
        if(visinput == "no"):
            print(corrMatrix)
        if (visinput == "yes"):
            sb.heatmap(corrMatrix, annot=True)
            plt.show()
    if(useinput == "EDA"):
        print("The first 5 columns of the data:\n")
        print(df.head())
        print("The basic data information:\n")
        print(df.info())
        print("The basic description of the data:\n")
        print(df.describe())
        print("The number of null entries:\n")
        print(df.isnull().sum())
    if(useinput == "Visualize"):
        print("What would you like the independent variable to be?")
        ind = input()
        print("What would you like the dependent variable to be?")
        dep = input()
        plt.scatter(df[ind],df[dep])
        plt.xlabel(ind)
        plt.ylabel(dep)
        plt.title("Relationship Between "+ind+" and "+dep+" variables")
        plt.show()
    if(useinput == "Distribution"):
        print("Do you want all distributions?")
        ans = input()
        if(ans == "yes"):
            df.hist()
            plt.show()
        else:
            print("What distribution would you like to see?")
            dis = input()
            df[dis].hist()
            plt.show()
