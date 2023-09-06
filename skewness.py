def skewness(data):
     n=len(data)
     mean=sum(data)/n
     p=sum([(x-mean)**3 for x in data])
     standard_deviation=(sum([(x-mean)**2 for x in data])/n)**0.5
     skew= p/(n*((standard_deviation)**3))
     return skew
data=[12, 32, 41, 11, 1, 2, 3, 4]
skew=skewness(data)
print("Skewness",skew)
