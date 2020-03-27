---
layout: default
published: true
---

## Conference Schedule (7 Jun 2019 at NUS School of Computing)

{% for day in site.data.schedule %}
{% if site.data.schedule.size > 1 %}<h2>Day {{ day.day }}</h2>{% endif %}
<table>
    {% for activity in day.activities %}
    <tr>
        <td>{{ activity.time }}</td>
        <td width="80%">{{ activity.title }}</td>
    </tr>
    {% endfor %}
</table> 
{% endfor %}
	

## Grouping for event:
<a class="btn" href="https://docs.google.com/spreadsheets/d/1d04PgjLW7Uv2xsFUm5r1WwvjMiSpoik27xoNOG-iYGk/edit?usp=sharing">View Grouping</a>

## Winpetition

### DataCamp Outreach
Description: 
In conjunction with the theme of 'Building an AI Smart Nation', BuildingBloCS has partnered with AI Singapore to provide DataCamp access to students and teachers for free until end October 2019!

Under the AI4BuildingBloCS AI for Students programme, students can complete a variety of DataCamp courses and exercises before the actual conference on June 7. Not only can they earn certification for course completion, any participant with strong participation stats stands to win prizes too (that is why we call it a winpetition)! Students can also do exercises on the DataCamp mobile app to gain XP. They can also complete interesting AI projects within/beyond DataCamp and have them featured on the BuildingBloCS website.

Students that complete DataCamp courses/exercises/projects and earn XP will have bonus points credited to their teams for the onsite winpetition. Students that complete a significant number of courses/exercises/projects and with high XP will also be awarded prizes during the conference.

Some of the recommended courses include:
- [Introduction to Python](https://www.datacamp.com/courses/intro-to-python-for-data-science): Master the basics of using Python for data science. Expand your skill set by learning scientific computing with NumPy, a library commonly used in data science and machine learning.
- [Introduction to Matplotlib](https://www.datacamp.com/courses/introduction-to-matplotlib): Learn how to create, customise, and share data visualizations using Matplotlib. Matplotlib is a powerful Python data visualization library to create rich visualizations of many different kinds of datasets.

### Machine Learning
Description:
On the day of the conference, participants will learn the basics of supervised machine learning. They will build a classification model using the learning algorithm k-Nearest Neighbours (k-NN) and calculate the accuracy using an evaluation method.

During the winpetition, participants will use their skills learnt for k-Nearest Neighbours (k-NN) algorithm to build and fine-tune their model to solve real-world classification problems. They will also be required to pre-process and manipulate the data to enhance the performance of their model built.

Prerequisites: Basic Python programming knowledge such as lists, loops and functions.

## Updates

Maituliao. [Click here]({{ site.baseurl }}/register#event) to register now!
Follow [@buildingblocs18](https://instagram.com/buildingblocs18) for quick notifications on event updates :)

<!--

## Fringe Games

We have **8 exciting games** lined up for you in BuildingBloCS 2018- From decoding secret passages, to solving puzzles, the possibilities are boundless! 
Participants will be pushed to work together and compete against other teams in a race against time.

Details and instructions of the fringe games will be released on the day itself for an element of surprise. **The Best Performing Team will win attractive prizes ;)**

# Photos

<a class="btn" href="https://photos.app.goo.gl/cntLndL2gY9cu0jK2">View Album</a>
-->
## More details of main event will be released soon :)
