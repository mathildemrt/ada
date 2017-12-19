#  Evolution of music genres

***"When the words fail, music speaks"**, Hans Christian Andersen*

## Links
* [Data Story](https://mathmout.github.io/ada/project/)
* [Notebook viewer](https://nbviewer.jupyter.org/github/mathmout/ada/blob/master/project/project.ipynb?flush_cache=true)

## Abstract

Our goal was originally to draw an identikit-picture of the different music genres and subgenres. The [Million song](https://labrosa.ee.columbia.edu/millionsong/) dataset provides several criteria like the duration, danceability, loudness, etc... We also wanted to analyze the most prolific types of music over time and understand their evolution.

Since Milestone 1, our idea has evolved. A closer look at the dataset revealed that some information that we wanted to be part of our identikit, such as the energy and the danceability, was missing for a lot of songs in the dataset. Conversely, the location of the song and the date are well defined so we decided to make full use of this information. The goal now, would be to analyse the music genre evolution both geographically and over time. The idea is to show the most popular genre in a certain region at a given year.

The original idea of drawing the portrait of a genre has not been completly dropped but it has became a secondary concern. After having analysed the evolution of genre we will try to find if there is a correlation between the genre and the hotesness or familiarity of the artist.

## Dataset
We want to use the [Million song](https://labrosa.ee.columbia.edu/millionsong/) dataset. This dataset provides several tags per song whose help us to classify the songs per musical type. The data are available on h5 files and a python [library](https://github.com/tbertinmahieux/MSongsDB/tree/master/PythonSrc) exists to manage them. The data set is pretty huge and we don't know how to work with a cluster so we are looking forward to hearing more about it. [Million song](https://labrosa.ee.columbia.edu/millionsong/) provides some extra datasets whose could help us to enrich our analysis.

## Research questions

### Milestone 1 
 - What define a musical genre?
 - What is the leading type of music over time?
 - How evoled a musical genre?
 
### Milestone 2
- How music genre has evolved over time and location?
- Find for each genre, where and when did it first appeared ?
- Which genre is the most prolific genre ? e.g.: What was the most prolific genre of music in Texas in the 20's?
- Is there a link between a genre and the hotesness and the popularity of an artist?


### A list of internal milestones up until project milestone 2

 #### Week 1 (7 Nov)

- [x] Access to the database from the cluster. *[Thibaut, Mathilde]*
- [x] Start to Identificate the important metrics. *[Mathilde, Noé]*
- [x] Differentiate genres and subgenres. Definition of genre *[Thibaut, Mathilde, Noé]*. Create the first dictionnary  subgenre/genre with beautiful soup *[Mathilde]*. Enrich the dictionnary  subgenre/genre *[Noé]*.

#### Week 2 (14 Nov)

- [x] Create our dataframe with the identified metric. `get_genre()`, `create_data_frame()`  functions *[Noé]*. `get_location()`function *[Thibaut]*


#### Week 3 (21 Nov)

- [x] Start the *music genre* analysis *[Thibaut,Mathilde,Noé]*

#### Week 4 (28 Nov)

- [x] Analyze the most prolific types of music over time *[Thibaut, Mathilde, Noé]*
- [x] Analyze the data, find a way to represent the important feature of each *music genre* and visualize the difference between the different *music type* *[Thibaut, Mathilde, Noé]*

### A list of internal milestones up until project milestone 3

During this milestone we will focus our work on 3 tasks:
- prepare great visualizations
- scale our analysis to the entire dataset
- create a data story

#### Week 5 ( 5 Dec)
- [x] Create our dataframe with the entire dataset *[Thibaut, Mathilde]*
- [x] Start Visualisation function on the subset *[Thibaut, Mathilde, Noé]*

#### Week 6 ( 12 Dec) 
- [x] Finish the visualizations : - World heat map *[Thibaut, Mathilde]*
                                  - Music timeline *[Noé]*
                                  - Artist familiarity and hotttnesss analysis + bokeh plots *[Noé]*
                                  
- [x] Do the analysis *[Thibaut, Mathilde, Noé]*
- [x] Start the data story *[Mathilde]*

#### Week 7 ( 19 Dec) 
- Finish the data story *[Thibaut, Mathilde, Noé]*


## Visualizations

#### Music genre evolution over time and location
- Display a music genre propagation over time on an interactive map
- Display the music genres production over time

#### Music genre analysis:
- look at the most familiar, and hotttest Artist, most hotttest songs according to different feature.
- Identidy genre those are up and coming, getting buzz or fading away...

#### Bokeh app:
- different interactive visualisation were done with bokeh:`genre_pie.py`, `most_h`, `artist_hf`. To view the app directly from a Bokeh server, navigate to the parent directory project/bokeh_app, and execute the command: `bokeh serve --show app_name.py`

## Questions for TAs

For Week 1 and 2:
- How works the cluster, and are there other detailed *Tutorials* than the one you already gave us?
- How to handle such a big database without getting a `Memory Error` with python?

For Week 4:
- Is there a common way to represent the result of a classifictation with many feature? Do you have some advice do that?  


## Final presentation & poster *[Thibaut, Mathilde, Noé]*
