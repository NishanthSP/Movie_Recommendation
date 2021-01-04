from preprocessing import recommend_movies
import pandas as pd

movie = input()
x = int(input("Enter the number of top movies to be recommended : "))

recommend = recommend_movies(movie)
recommend = recommend.index.tolist()[0:x+1]
recommend = pd.DataFrame(recommend, columns=['Recommended Movies'])
print("The following list is the recommended movies with respect to  : ", movie)
print((recommend['Recommended Movies']).to_string(index=False))
