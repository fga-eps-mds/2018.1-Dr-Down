
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var csrftoken = getCookie('csrftoken');

var height_data;
var weight_data;
var bmi_data;
var perimeter_data;

$("#height_chart").ready(
    function() {

        $.ajax({
            type:"GET",
            url:"curves/ajax/",
            data: {
                'username': document.getElementById("_username").value,
                'data_type': 'height'
            },
            success: function(response){
                height_data = JSON.stringify(response.data);
                ready();
            },
            error: function(response){
                console.log(response);
            }
        });

    }
)

$("#weight_chart").ready(
    function() {

        $.ajax({
            type:"GET",
            url:"curves/ajax/",
            data: {
                'username': document.getElementById("_username").value,
                'data_type': 'weight'
            },
            success: function(response){
                weight_data = JSON.stringify(response.data);
                ready();
            },
            error: function(response){
                console.log(response);
            }
        });

    }
)

$("#bmi_chart").ready(
    function() {

        $.ajax({
            type:"GET",
            url:"curves/ajax/",
            data: {
                'username': document.getElementById("_username").value,
                'data_type': 'bmi'
            },
            success: function(response){
                bmi_data = JSON.stringify(response.data);
                ready();
            },
            error: function(response){
                console.log(response);
            }
        });

    }
)

$("#perimeter_chart").ready(
    function() {

        $.ajax({
            type:"GET",
            url:"curves/ajax/",
            data: {
                'username': document.getElementById("_username").value,
                'data_type': 'cephalic_perimeter'
            },
            success: function(response){
                perimeter_data = JSON.stringify(response.data);
                ready();
            },
            error: function(response){
                console.log(response);
            }
        });

    }
)

function ready(){

    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart);

}

function convertToArray(string) {

    var json_data = JSON.parse(string);

    var array = []

    json_data.graphic.forEach(element => {
        array.push(element)
    });

    array.forEach(element => {

        var item = element.pop()

        if (item == 0){
            item = null;
        }

        element.push(item);

    });

    //populatePatientCurve(array)

    console.log(array)

    return array
}

function defineOptions(title) {
    return {
        title: title,
        hAxis: {
            title: 'Age',
            titleTextStyle: {color: '#333'},
            minValue: 25
        },
        vAxis: {
            title: 'Height',
            titleTextStyle: {color: '#333'},
            minValue: 0,
            format: 'decimal',
        },
        explorer: {
            actions: ['dragToZoom', 'rightClickToReset'],
            axis: 'horizontal',
            keepInBounds: true,
            maxZoomIn: 4.0
        },
        crosshair: { trigger: 'selection' },
        lineWidth: 2,
        series: {
            0: { color: '#e2431e' },
            1: { color: '#e7711b' },
            2: { color: '#f1ca3a' },
            3: { color: '#6f9654' },
            4: { color: '#1c91c0' },
            5: { color: '#e7711b' },
            6: { color: '#e2431e' },
        },
        is3D: true
    };
}

function drawChart() {

    var height_array = convertToArray(height_data)
    var data_height = google.visualization.arrayToDataTable(height_array);
    var options = defineOptions(title='Height')
    var height_chart = new google.visualization.AreaChart(document.getElementById('height_chart'));
    height_chart.draw(data_height, options);

    var weight_array = convertToArray(weight_data)
    var data_weight = google.visualization.arrayToDataTable(weight_array);
    var options = defineOptions(title='Weight')
    var weight_chart = new google.visualization.AreaChart(document.getElementById('weight_chart'));
    weight_chart.draw(data_weight, options);

    var bmi_array = convertToArray(bmi_data)
    var data_bmi = google.visualization.arrayToDataTable(bmi_array);
    var options = defineOptions(title='BMI')
    var bmi_chart = new google.visualization.AreaChart(document.getElementById('bmi_chart'));
    bmi_chart.draw(data_bmi, options);

    var perimeter_array = convertToArray(perimeter_data)
    var data_perimeter = google.visualization.arrayToDataTable(perimeter_array);
    var options = defineOptions(title='Perimeter')
    var perimeter_chart = new google.visualization.AreaChart(document.getElementById('perimeter_chart'));
    perimeter_chart.draw(data_perimeter, options);

}
