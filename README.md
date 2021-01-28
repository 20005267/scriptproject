# Mathematical Calculations using JavaScript
## AIM:
To design a website to calculate the area of a circle and volume of a cylinder using JavaScript.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Write JavaScript to perform calculations.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 6:
Publish the website in the given URL.


## PROGRAM:

## CYLINDERVOLUME.HTML:
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <title>VOLUME OF THE CYLINDER</title>
    <link rel="stylesheet" href="{% static 'css/cylindervolumescript.css' %}">
</head>

<body>
    <div class="container">
        <div class="formview">
            <div class="banner">
                VOLUME OF THE CYLINDER
            </div>
            <div class="content">
                <form action="/cylindervolume/" method="POST">
                    {% csrf_token %}
                    <div class="forminput">
                        <label for="value_radius">Radius=</label>
                        <input type="text" name="value_radius" id="value_radius" value="{{radius}}">
                    </div>
                    <div class="forminput">
                        <label for="value_height">Height=</label>
                        <input type="text" name="value_height" id="value_height" value="{{height}}">
                    </div>
                    <div class="forminput">
                        <button type="button" name="button_volume" id="button_volume">Calculate Volume</button>
                    </div>
                    <div class="forminput">
                        <label for="value_result">V=</label>
                        <input type="text" name="value_result" id="value_result" readonly>
                    </div>             
                    <div class="forminput">
                        {{result}}
                    </div>
                </form>
            </div>
        </div>
    </div>
    <script src="/static/js/cylindervolumescript.js"></script>
</body>

</html>

```
## CYLINDERVOLUME.JS
```
volumeBtn = document.querySelector('#button_volume');

volumeBtn.addEventListener('click',function(e){

    txtRadius = document.querySelector('#value_radius');
    txtHeight = document.querySelector('#value_height');
    txtResult = document.querySelector('#value_result');

    let V;

    V = 3.14*parseFloat(txtRadius.value)*parseFloat(txtRadius.value)*parseFloat(txtHeight.value);

    txtResult.value = V;
});
```
## RECTANGLEAREA.HTML:
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <title>AREA OF RECTANGLE</title>
    <link rel="stylesheet" href="{% static 'css/rectangleareascript.css' %}">
</head>

<body>
    <div class="container">
        <div class="formview">
            <div class="banner">
               AREA OF RECTANGLE 
            </div>
            <div class="content">
                <form action="/rectanglearea/" method="GET">
                    {% csrf_token %}
                    <div class="forminput">
                        <label for="value_a">Length=</label>
                        <input type="text" name="value_a" id="value_a">
                    </div>
                    <div  class="forminput">
                        <label for="value_b">Breadth=</label>
                        <input type="text" name="value_b" id="value_b">
                    </div>                    
                    <div class="forminput">
                        <button type="button" name="button_calculate" id="button_calculate">calculate</button>
                    </div>
                    <div  class="forminput">
                        <label for="value_c">Area=</label>
                        <input type="text" name="value_c" id="value_c" readonly>
                    </div>                    
                </form>
            </div>
        </div>
    </div>
    <script src="/static/js/rectangleareascript.js"></script>
</body>

</html>
```

## RECTANGLEAREA.JS:
```
addBtn = document.querySelector('#button_calculate');

addBtn.addEventListener('click',function(e){

    txtA = document.querySelector('#value_a');
    txtB = document.querySelector('#value_b');
    txtC = document.querySelector('#value_c');

    let c;

    c = parseFloat(txtA.value) * parseFloat(txtB.value);

    txtC.value = c;
});
```

## OUTPUT:

![output](.static/img/output1.jpg)

![output](.static/img/output2.jpg)


## CODE VALIDATION REPORT:

![output](.static/img/report1.jpg)

![output](.static/img/report2.jpg)


## RESULT:

Thus a website is designed for the calculation of volume of cylinder using JavaScript and is hosted in the URL http://kayalvizhi.student.saveetha.in:8000/cylindervolume/. HTML code is validated.
 
Thua a website is designed ffor the calculation off area of rectangle using JavaScript and hosted in the URL http://kayalvizhi.student.saveetha.in:8000/
rectanglearea/. HTML code is vaalidated.

