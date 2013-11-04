collaborative_filtering_recomm_sys
==================================





Collaborative Filtering Recommender System
(Implementation Details)
==============================================

	For this project we have a dataset that contains 100,000 movie ratings. These are real ratings by real people gathered by the Group Lens research group at the University of Minnesota (http://www.grouplens.org). The dataset is made available with permission from Group Lens. 
The data was collected through the Movie Lens web site (movielens.umn.edu) during the seven-month period from September 19th, 1997 through April 22nd, 1998. This data has been cleaned up for users who had less than 20 ratings or did not have complete demographic information were removed from this data set.
The ultimate goal of the project is to take a user (specified by an ID) and make movie recommendations for this user based on the rating history of this user and all the others in the provided data set
DETAILED DESCRIPTIONS OF DATA SET
==============================================
Here is a brief descriptions of the data.

u.data -- The file u data set 100000 ratings by 943 users on 1682 items. Each user has rated at least 20 movies.  Users and items are  numbered consecutively from 1.  The data is randomly ordered. This is a tab separated list of  user id | item id | rating | timestamp. The time stamps are Unix seconds since 1/1/1970 UTC   

u.info -- The number of users, items, and ratings in the u.data set.

u.item -- Information about the items (movies). This is a tab separated  list of  movie id | movie title | release date | video release date |  IMDb URL | unknown | Action | Adventure | Animation Children's | Comedy | Crime | Documentary | Drama | Fantasy |Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |Thriller | War | Western | The last 19 fields are the genres, a 1 indicates the movie is of that genre, a 0 indicates it is not; movies can be in several genres at once.      

u.genre -- A list of the genres.

u.user  -- Demographic information about the users. This is a tab separated list of  user id | age | gender | occupation | zip code The user ids are the ones used in the u.data data set.

u.occupation -- A list of the occupations of the users

Implementation- Phase 1 

Creation of appropriate data structures to store the data files.

createUserList():
This data structure reads from the le u.user and returns a list containing all  the details of the user. For example, a  line in u.user is  1|24|M|technician|85711


createMovieList():
It reads from the file u.item and returns a list containing all of the information pertaining to movies given in the file. For example,  a line in u.list is

 1|Toy Story (1995)|01-Jan-1995||http://us.imdb.com/M/title%20exact?Toy%20Story%20(1995)|0|0|0|1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0


createRatingsList(numUsers, numMovies):

It reads from the file u.data and returns two lists containing all 100,000 ratings provided in u.data. The function takes as arguments the number of users and the number of movies in the data set. Suppose we call this function as [rLu, rLm] = createRatingsList(numUsers, numMovies). Then rLu is a list, with one element per user, of all the ratings provided by each user. Similarly, rLm is a list, with one element per movie, of all the ratings received by each movie.


createGenreList():

It reads from the file u.genre and returns the list of movie genres listed in the file. The genres should appear in the order in which they are listed in the file.

Phase 2(Implementation of Collaborative Filtering Algorithm)
=====================================================================
We implement algorithms that predict users tastes in movies based on the available ratings data, demographic data, etc.

The Collaborative Filtering Algorithm

The  algorithm we  implement predicts ratings of a given user i by taking into account ratings of users whose tastes are similar to i's tastes. The algorithm largely depends on the following definitions.

The similarity between two users i and j is defined as:

Here C is the set of movies that both i and j have rated, rim is user i's rating of movie m, rjm is user j's rating of movie m, and ri is user i's mean rating and rj is user j's mean rating. This  definition guarantees that sim(i,j) will always be between -1 and +1.This definition of sim(i,j) views the similarity of users i and j as a correlation between their ratings. If it turns out that user i and j have similar tastes and they have both rated common movies in a similar manner, then sim(i,j) will be close to 1,on the other hand if their tastes are opposite  then sim(i,j) will be closer to -1.

 
                           ?m?C(Ri,j-Ri).(Rj,m-Rm)
	Sim(i,j)=     ----------------------------------------------
	              (Sqrt(?m?C(Ri,m-Ri)^2). (Sqrt(?m?C(Rj,m-Rj)^2)



Note that if C is empty then it means that we have no basis for figuring out the correlation between users i and j and in this case we assume that i and j are uncorrelated and will set sim(i, j) to be 0. Also, if the denominator in the above expression is 0, it means that the numerator will also be 0 and in this case also we set sim(i, j) to be 0.

Once similarity between users is defined as above, we can predict the rating that a user i gives to a movie m by taking the weighted average of ratings that movie m has received from users who are similar to i. Specially, for a user i and a movie m, defines the predicted rating of movie m by user i as:   



			   ?j?U(Rj,m-Rj).sim(i,j)
p(i,m)=   Ri + ----------------------------------------
				?j?Usim(i,j)

                                              							
Here U is the set of users that have rated movie m and are very similar to i. To define this more precisely, let N(j, k) be the k users that are most similar to i. Think of N(j,k) as user i's k best friends, namely those k users whose tastes in movies is closest to i's tastes. Then, for an appropriately chosen positive constant, U is the subset of users in N(i, k) that have rated movie m.


Phase 3(Evaluation of  the Prediction Algorithm)
==============================================
The standard approach to test the algorithm that we will be using if we an complete the above mentioned tasks on time is called cross-validation. The main idea here is that we take a fraction of the rating data, say 20%, and call it our testing set. The remaining 80% of the rating data will form our training set. We will then train our prediction algorithm on our training set and test it on our testing set. More specifically, we will hide our testing set and come up with predicted ratings based on our training set alone. We will then walk through our test set, come up with a predicted rating for every item in the test set and compare the predicted rating with the actual rating

































