---
layout: default
---


# Lucky draw

We will have weekly draws for all the registered participants on every Friday from 19 Apr and your chances accumulate till 7 Jun i.e. a total of 8 lucky draws, and there is no limit to the number of times you can get lucky!

>Lucky draws will take place every Friday at **12 20 pm**

Do visit [classdo.com](https://classdo.com) and witness the lucky draw unfold.


## Source code

To ensure the equalness for every participant, we have decided to share the source code of the 'lucky generator' with all of you.

<a class="btn" href="https://github.com/buildingblocs/2019/blob/master/luckydraw.py">View Code</a>

## Result
{% for week in site.data.awards %}
<h3>Week {{ week.week }}</h3>
<a class="btn" href="{{ site.baseurl }}/pre-event/luckydraw/video#{{week.week}}">Video</a>
<table>
    {% for awards in week.awards %}
    <tr>
        <td width="40%">{{ awards.prize }}</td>
        <td width="60%">{{ awards.winner }}</td>
    </tr>
    {% endfor %}
</table>
{% endfor %}


