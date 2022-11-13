import csv

with open('/Users/lili/Desktop/Cursos/Data science with python/q1jaewUQR_KY2nsFEEfypQ_842f5df9823742e991f00673b547ebf1_Course-1---Notebook-Resources-1-/resources/datasets/mpg.csv') as csvfile:
  mpg =list(csv.DictReader(csvfile))
  
mpg[:3] # we have to run the code in a interactive window to show us de csv file

len(mpg) # to know the lenght of the csv file
mpg[0].keys() #by using the key method we can get the colum names

#to work with numbers of the mpg file, first we have to transform the strings into numbers (float)
sum(float(d['cty'])for d in mpg)/ len(mpg)
sum(float(d['hwy'])for d in mpg)/len(mpg) 

cylinders = set(d['cyl']for d in mpg)
cylinders #to get the cylinders of the mgp file 

CtyMpgByCyl = []

for c in cylinders: # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg: # iterate over all dictionaries
        if d['cyl'] == c: # if the cylinder level type matches,
            summpg += float(d['cty']) # add the cty mpg
            cyltypecount += 1 # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')

CtyMpgByCyl.sort(key=lambda x: x[0]) # we start with the highestvalue
CtyMpgByCyl #we can see that the fuel decreses in order that the cylinders increase

#now me want to know the car models
vehicleclass = set(d["class"] for d in mpg) #we convert the data into values
vehicleclass

#We compare the data and the analytics
HwyMpgByClass = [] #we create the empy list where our data is going to be stored

for t in vehicleclass: #iterate over all the vehicle classes
  summpg = 0
  vclasscount = 0 # we initialize the variables where the data is going to be stored
  for d in mpg: 
    if d ["class"] == t:
      summpg += float(d["hwy"])
      vclasscount += 1 #increment the count by 1
  HwyMpgByClass.append((t, summpg / vclasscount)) # to get the avarage
HwyMpgByClass.sort(key=lambda x: x[1]) # we start with the lower value
HwyMpgByClass
  