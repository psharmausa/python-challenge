data = """Wood [m2],Polygon,Area [m2]
15,A,50
10,A,50
12,B,30
10,C,30
05,D,50
10,D,50"""
 
dataLines = data.split("\n")
dd = {}
for line in dataLines[1:]:
    items = line.split(",")
    dd.setdefault(items[1], []).append((float(items[0]), float(items[2])))
 
keys = sorted(dd.keys())
for key in keys:
    print ("Polygon %s: \nPercentage: %0.0f%%" %
           (key, sum((item[0] for item in dd[key]))/dd[key][0][1]*100))
    print ("========================")