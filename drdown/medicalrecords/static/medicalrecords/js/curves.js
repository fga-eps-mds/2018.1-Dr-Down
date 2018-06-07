
var DATA_TYPES = {
    height: 'Height',
    weight: 'Weight',
    bmi: 'BMI',
    perimeter: 'Perimeter'
}


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

function call_height(time_frame){

    $.ajax({
        type:"GET",
        url:"curves/ajax/",
        data: {
            'username': document.getElementById("_username").value,
            'data_type': 'height',
            'time_frame' : time_frame,
        },
        success: function(response){
            height_data = JSON.stringify(response.data);
            
            google.charts.load('current', {'packages':['corechart']});
            google.charts.setOnLoadCallback(draw_HeigthChart);
        },
        error: function(response){
            console.log(response);
        }
    });

}

function call_weight(time_frame) {

    $.ajax({
        type:"GET",
        url:"curves/ajax/",
        data: {
            'username': document.getElementById("_username").value,
            'data_type': 'weight',
            'time_frame': time_frame,
        },
        success: function(response){
            weight_data = JSON.stringify(response.data);
            
            google.charts.load('current', {'packages':['corechart']});
            google.charts.setOnLoadCallback(draw_WeigthChart);
        },
        error: function(response){
            console.log(response);
        }
    });
    
}

$("#height_time_select").ready(
    function() {
        call_height(time_frame=$("#height_time_select").val())
    }
)

$(document).on('change','#height_time_select',function(){
    call_height(time_frame=$("#height_time_select").val())
});

$(document).on('change','#weight_time_select',function(){
    call_weight(time_frame=$("#weight_time_select").val())
});

$("#weight_time_select").ready(
    function () {
        call_weight(time_frame=$("#weight_time_select").val())    
    }
)

$("#bmi_chart").ready(
    function() {

        $.ajax({
            type:"GET",
            url:"curves/ajax/",
            data: {
                'username': document.getElementById("_username").value,
                'data_type': 'bmi',
                'time_frame': 'months'
            },
            success: function(response){
                bmi_data = JSON.stringify(response.data);
                
                google.charts.load('current', {'packages':['corechart']});
                google.charts.setOnLoadCallback(draw_BMIChart);
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
                'data_type': 'cephalic_perimeter',
                'time_frame': 'months'
            },
            success: function(response){
                perimeter_data = JSON.stringify(response.data);

                google.charts.load('current', {'packages':['corechart']});
                google.charts.setOnLoadCallback(draw_PerimeterChart);
            },
            error: function(response){
                console.log(response);
            }
        });

    }
)

$("#menu7-tab").click(function () {
        var func_to_call = function () {redraw_charts();};
        var time = 3000;

        setTimeout(func_to_call, time);
    }
)

function convertToArray(string) {

    var json_data = JSON.parse(string);

    var array = []

    json_data.graphic.forEach(element => {
        array.push(element)
    });

    array.forEach(element => {

        var item = element.pop()

        if (item == 0 && array.indexOf(element) != 1){
            item = null;
        }

        element.push(item);

    });

    console.log(array)

    return array
}

function defineOptions(data_type, data_array) {

    
    if(data_array != null){
     
        title = data_array[0][data_array[0].length - 1];
        hAxis_title = data_array[0][0];
        vAxis_title = data_array[0][data_array[0].length - 1];

    }else{
   
        title = data_type;
        hAxis_title = data_type;
        vAxis_title = "Ages";
   
    }

    
    var colors = {}

    if (data_type == DATA_TYPES.bmi){
        colors = {
            0: { color: '#f96363' }, // red - 5%
            1: { color: '#f7ae6a' }, // orange  6- 10%
            2: { color: '#ffe06d' }, // yellow - 25%
            3: { color: '#b6ff84' }, // green - 50%
            4: { color: '#ffe06d' }, // yellow - 75%
            5: { color: '#f7ae6a' }, // orange - 85%
            6: { color: '#f96363' }, // red - 80%
            7: { color: '#f96363'},  // extra_red - 95%
            8: { color: '#003791'},  // blue - patient  
        };
    }else{
        colors = {
            0: { color: '#f96363' }, // red - 3%
            1: { color: '#f7ae6a' }, // orange 6- 10%
            2: { color: '#ffe06d' }, // yellow - 25%
            3: { color: '#b6ff84' }, // green - 50%
            4: { color: '#ffe06d' }, // yellow - 75%
            5: { color: '#f7ae6a' }, // orange - 90%
            6: { color: '#f96363' }, // red - 97%
            7: { color: '#003791'},  // blue - patient
        };
    }

    return {
        title: title,
        curveType: 'function',
        hAxis: {
            title: hAxis_title,
            titleTextStyle: {color: '#333'},
        },
        vAxis: {
            title: vAxis_title,
            titleTextStyle: {color: '#333'},
            format: 'decimal',
            viewWindowMode: 'pretty',
        },
        explorer: {
            actions: ['dragToZoom', 'rightClickToReset'],
            axis: 'horizontal',
            keepInBounds: true,
            maxZoomIn: 4.0
        },
        crosshair: { trigger: 'selection' },
        lineWidth: 2,
        series: colors,
        is3D: false,
    };
}

function redraw_charts() {
    
    draw_HeigthChart();
    draw_WeigthChart();
    draw_BMIChart();
    draw_PerimeterChart();

}

function draw_HeigthChart() {

    var height_array = convertToArray(height_data)
    var data_height = google.visualization.arrayToDataTable(height_array);
    var options = defineOptions(data_type=DATA_TYPES.height, data_array=height_array)
    var height_chart = new google.visualization.LineChart(document.getElementById('height_chart'));
    height_chart.draw(data_height, options);

}

function draw_WeigthChart() {

    var weight_array = convertToArray(weight_data)
    var data_weight = google.visualization.arrayToDataTable(weight_array);
    var options = defineOptions(data_type=DATA_TYPES.weight, data_array=weight_array)
    var weight_chart = new google.visualization.LineChart(document.getElementById('weight_chart'));
    weight_chart.draw(data_weight, options);
}

function draw_BMIChart() {

    var bmi_array = convertToArray(bmi_data)
    var data_bmi = google.visualization.arrayToDataTable(bmi_array);
    var options = defineOptions(data_type=DATA_TYPES.bmi, data_array=bmi_array)
    var bmi_chart = new google.visualization.LineChart(document.getElementById('bmi_chart'));
    bmi_chart.draw(data_bmi, options);
}

function draw_PerimeterChart() {

    var perimeter_array = convertToArray(perimeter_data)
    var data_perimeter = google.visualization.arrayToDataTable(perimeter_array);
    var options = defineOptions(data_type=DATA_TYPES.perimeter, data_array=perimeter_array)
    var perimeter_chart = new google.visualization.LineChart(document.getElementById('perimeter_chart'));
    perimeter_chart.draw(data_perimeter, options);

}
