<p align="center">
  <img src="ScreenShots_model/1-import.png" width="200"/><br>
    pandas: Used for data manipulation and analysis (DataFrames).

    numpy: Used for numerical operations.   
</p>

<p align="center">
  <img src="ScreenShots_model/2-read_datasheet.png" width="200"/><br>
  We load two CSV files: movies contains metadata (budget, genres, etc.), and credits contains information about the cast and crew.
</p>

<p align="center">
  <img src="ScreenShots_model/3-merge_mocr.png" width="200"/><br>
  Since both files share a title column, we merge them into a single DataFrame to have all information in one place.
</p>

<p align="center">
  <img src="ScreenShots_model/4-n_column.png" width="200"/><br>
  We discard unnecessary columns (like budget, popularity, release date) and keep only the features that help define the "content" of a movie for recommendation.
</p>

<p align="center">
  <img src="ScreenShots_model/5-dropna.png" width="200"/><br>
  dropna(): Removes rows with missing values (inplace -> modifies the actual csv file).
</p>

<p align="center">
  <img src="ScreenShots_model/6-StrToList_fun.png" width="200"/><br>
  function that helps to convert every word into list and append in list L then return the list
</p>

<p align="center">
  <img src="ScreenShots_model/7-convertGenKey.png" width="200"/><br>
  converting genres and keyword with the help op convert function
</p>

<p align="center">
  <img src="ScreenShots_model/8-convertCast_fun.png" width="200"/><br>
  function that helps us to detect top 3 charater from the cast and return the list
</p>

<p align="center">
  <img src="ScreenShots_model/9-convertCast.png" width="200"/><br>
  converting the cast data using the convertCast function.
</p>

<p align="center">
  <img src="ScreenShots_model/10-findDirector_fun.png" width="200"/><br>
  helps to find the director from the given data
</p>

<p align="center">
  <img src="ScreenShots_model/11-DirInCrew.png" width="200"/><br>
  crew data is send to the findDirector function and stored the returned data in the crew
</p>

<p align="center">
  <img src="ScreenShots_model/12-splitOverview.png" width="200"/><br>
  splitting the overview data
</p>

<p align="center">
  <img src="ScreenShots_model/13-removeSpace.png" width="200"/><br>
  We remove spaces between names ("Johnny Depp" becomes "JohnnyDepp"). This is crucial so that the vectorizer treats the full name as a single unique entity/tag.
</p>

<p align="center">
  <img src="ScreenShots_model/14-tagsColumn.png" width="200"/><br>
  creating a new column name tags that have overview genres keywords cast crew
</p>

<p align="center">
  <img src="ScreenShots_model/15-new_df.png" width="200"/><br>
  creating new data frame called new_df having movie_id, title, tags
</p>

<p align="center">
  <img src="ScreenShots_model/16-tagsConvertString.png" width="200"/><br>
  converting tags data into string
</p>

<p align="center">
  <img src="ScreenShots_model/17-tagsLowercase.png" width="200"/><br>
  lowercasing the string of the tags
</p>

<p align="center">
  <img src="ScreenShots_model/18-impNLTK.png" width="200"/><br>
  installing nltk and importing nltk
</p>

<p align="center">
  <img src="ScreenShots_model/19-impPorterStemmer.png" width="200"/><br>
  We use stemming to convert words to their root form (e.g., "activities" and "activity" both become "activi"). This prevents the model from treating different forms of the same word as different tags.
</p>

<p align="center">
  <img src="ScreenShots_model/20-stem_fun.png" width="200"/><br>
  stem function helps to merge the same type of words
</p>

<p align="center">
  <img src="ScreenShots_model/21-stemapplytotags.png" width="200"/><br>
  giving tags data to the stem function
</p>

<p align="center">
  <img src="ScreenShots_model/22-impCountVectorizer.png" width="200"/><br>
  importing skit learn to use vectorize calss
</p>

<p align="center">
  <img src="ScreenShots_model/23-tagVectorizing.png" width="200"/><br>
</p>

<p align="center">
  <img src="ScreenShots_model/24-cosineSimilarity.png" width="200"/><br>
  to use cosine_similarity
</p>

<p align="center">
  <img src="ScreenShots_model/25-similarity.png" width="200"/><br>
  assign the value of distance in the similarity
</p>

<p align="center">
  <img src="ScreenShots_model/26-recommend_fun.png" width="200"/><br>
  recommend function
</p>

<p align="center">
  <img src="ScreenShots_model/27-pickle.png" width="200"/><br>
  creating .pkl file to use these file in the streamlit
</p>
