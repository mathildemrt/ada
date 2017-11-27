# Musical genre identikit

***"When the words fail, music speaks"**, Hans Christian Andersen*

# Abstract
Our goal is to draw an identikit-picture of the different music genres and subgenres. The [Million song](https://labrosa.ee.columbia.edu/millionsong/) dataset provides several criteria like the duration, danceability, loudness, etc... We also want to analyze the most prolific types of music over the time and understand their evolution.

# Research questions
 - What define a musical genre?
 - What is the leading type of music over time?
 - How evoled a musical genre?

# Dataset
We want to use the [Million song](https://labrosa.ee.columbia.edu/millionsong/) dataset. This dataset provides several tags per song whose help us to classify the songs per musical type. The data are available on h5 files and a python [library](https://github.com/tbertinmahieux/MSongsDB/tree/master/PythonSrc) exists to manage them. The data set is pretty huge and we don't know how to work with a cluster so we are looking forward to hearing more about it. [Million song](https://labrosa.ee.columbia.edu/millionsong/) provides some extra datasets whose could help us to enrich our analysis.


# A list of internal milestones up until project milestone 2

 ### Week 1 (7 Nov)

- Access to the database from the cluster.
- Start to Identificate the important metrics.
- Differentiate genres and subgenres.

### Week 2 (14 Nov)

- Create our dataframe with the identified metric.

### Week 3 (21 Nov)

- Start the *music genre* classification (supervised learning)

### Week 4 (28 Nov)

- Analyze the most prolific types of music over the time 
- Analyze the data, find a way to represent the important feature of each *music genre* and visualize the difference between the different *music type*

# Milestone 3
During this milestone we will focus our work on 2 tasks:
- prepare great visualizations
- scale our analysis to the entire dataset

### Visualization
#### Music genre analysis
- Display what define a music genre
- Draw robot portraits of musical genres
#### Music genre evolution over time and location
- Display a music genre propagation over time on an interactive map
- Display the music genres production over time



# Questions for TAs

For Week 1 and 2:
- How works the cluster, and are there other detailed *Tutorials* than the one you already gave us?
- How to handle such a big database without getting a `Memory Error` with python?

For Week 4:
- Is there a common way to represent the result of a classifictation with many feature? Do you have some advice do that?  


