#==============================================================================
#Importing Libraries
#==============================================================================
#Nothing to write to do that

#==============================================================================
#Importing Dataset
#==============================================================================
dataset = read.csv('Data.csv')

#==============================================================================
#Missing Data
#==============================================================================
#dataset$Age takes Age column and handle that column specifically
#ifelse(condn,if true,if false)
#is.na tells whether columns contains NA value or no value
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean (x,na.rm = TRUE)),
                    dataset$Age)

#ave = A way to calculate mean. First argument the column we are gonna pass to the function
#that is going to calculate the mean. Then FUN will give the return value of the function
#that is going to calculate the mean. FUN will be assigned to the row where column value is nadataset$Age = ifelse(is.na(dataset$Age),
dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary, FUN = function(x) mean (x,na.rm = TRUE)),
                     dataset$Salary)
#==============================================================================
# Splitting the dataset into training set and test set
#==============================================================================
#install.packages('caTools')
library(caTools)
#Like random_state in python, we use seed to get same results
set.seed(123)
#First argument is for matrix, second is to tell split ratio for Training dataset
split = sample.split(dataset$Purchased,SplitRatio = 0.8)
#Split is a function we defined which returns true if the observation is
#training set & false if observation is test set
#So for SplitRatio=0.8, 8 will be true and 2 will be false
#To check, call split in console by calling the function

#This will make a subset from dataset, where split returns TRUE,i.e. only for
#observation that are in training set
training_set = subset(dataset,split == TRUE)
test_set = subset(dataset,split == FALSE)