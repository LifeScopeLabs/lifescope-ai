# [LIFESCOPE-AI](https://github.com/LifeScopeLabs/lifescope-ai)

## [Repository](https://github.com/LifeScopeLabs/lifescope-ai)

(concept phase, low priority)

This repository contains a suite of tools for reporting and machine learning workflow from LIFESCOPE data. Reporting is focused on building approachable dashboard visualizations and infographics.

Machine learning models based on LIFESCOPE data are currently focused on behavior modeling, correlation, prediction, suggestion, and impersonation.

# Reporting 
(concept phase, low priority)

## Requirements

- **MVP**: Infographic reports individuals can run on demand.
- Weekly email of reports.
- Custom reporting.
- Reporting on groups.

## Dependencies

- [Tau Charts](https://www.taucharts.com/)
- [Plot.ly](https://plot.ly/plotly-js-scientific-d3-charting-library/)
- [Chart.js](http://www.chartjs.org/samples/latest/)

## Examples

Create infographics and reports for LIFESCOPE users based on their data. 

### Personal Infographic Examples

**Finance Overview Bubble Chart**
{Merchants x Item Count x Total Price]

**Social Overview Line Chart**
[Social platform (Twitter, Linked In, Facebook) x Mentions & Likes x Time ]

![infographics1]

**Time Vertical Gantt Chart**
[Week x Event Type]

**Messaging Bar Chart** 
[% to vs From]

![infographics2]

**Heat Map of Activity**
[Location x Time]

![heatmap]

**Network Visualizations of Deep Learning Training**
[Adversarial Match]

![deepviz]

# Machine Learning 
(concept phase, low priority)

## Conversational Agents


### Requirements
- **Persona-based model**. Condition responses on a certain author of messages (User ID) to make responses lexically similar to them and mimic someone’s linguistic style in a conversation. Use new or pre-trained models to run a chatbot that maintains a conversation in a certain emotional state. 
- **Emotional chatting machine** with your own set of emotions. There are so many emotions that you can use as condition labels in your dataset. CakeChat only uses five basic emotions (anger, sadness, joy, fear and neutral). 
- **Topic-centric model**. Instead of emotions, you can use a set of topics that will condition the model’s responses. As a result, you can build an agent that sticks to a given topic in a conversation. For example, you can build a model that talks about weather, food, kids or mortgage at any given moment.
### Dependencies

- [CakeChat Framework](https://cakechat.replika.ai/) 
 -[Tenorflow Research Models for (Speech, Text, Video, Geodata](https://github.com/tensorflow/models/tree/master/research)

### Examples

- [Replika](https://replika.ai/) is an AI friend that is always there for you. Grow your own.
	- This. https://www.reddit.com/r/replika/



## Geolocation Based Models

**Geospatial Anomaly Map Example**

![mlgeo]

Prediction and anomaly detection based on location history.
  
#### [Using the NuPIC Geospatial Tracking Application](http://www.youtube.com/watch?v=M4dD9wCQLkA)
[![NuPIC Geospatial Tracking Application Tutorial](http://img.youtube.com/vi/M4dD9wCQLkA/hqdefault.jpg)](http://www.youtube.com/watch?v=M4dD9wCQLkA)

#### [Geospatial Coordinate Encoder Explained](http://www.youtube.com/watch?v=KxxHo-FtKRo)
[![Geospatial Coordinate Encoder](http://img.youtube.com/vi/KxxHo-FtKRo/hqdefault.jpg)](http://www.youtube.com/watch?v=KxxHo-FtKRo)

### Proposed Technology and Examples
- [Numenta Geospatioal](https://numenta.com/assets/pdf/whitepapers/Geospatial%20Tracking%20White%20Paper.pdf)
- [Numenta Geospatioal Github Example](https://github.com/numenta/nupic.geospatial)

### Others 
(Tensorflow)
- [Tenorflow Research Models for (Speech, Text, Video, Geodata](https://github.com/tensorflow/models/tree/master/research)

[heatmap]:https://lifescopelabs.github.io/assets/maps/heat-map.png
[infographics1]:https://lifescopelabs.github.io/assets/screenshots/infographics1.png
[infographics2]:https://lifescopelabs.github.io/assets/screenshots/infographics2.png
[deepviz]:https://lifescopelabs.github.io/assets/wireframes/DeepLearningViz.png
[webviz]:https://lifescopelabs.github.io/assets/wireframes/3d-graph.jpg
[mlgeo]:https://raw.githubusercontent.com/numenta/nupic.geospatial/master/images/viewer.png
