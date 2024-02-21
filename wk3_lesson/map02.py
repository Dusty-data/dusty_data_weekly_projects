weather_predictions = [ 
    
    ("Ankara", 29), 
    ("Berlin", 18), 
    ("Paris", 22), 
    ("Londra", 15), 
    ("Tokyo", 27), 
    ("Roma", 26), 
    ("Atina", 24), 
    ("Pekin", 31), 
    ("Washington, D.C.", 32), 
    ("Kahire", 35) 
    
]

c_to_f = lambda x : (x[0] , x[-1]*9/5 +32)

print(list(map(c_to_f, weather_predictions)))                 
#[i for i in a]

#print(list(map(lambda x : (x[0] + (x[-1] * 9/5 + 32, weather_predictions )))))