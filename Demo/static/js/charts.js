$(document).ready(function () {
   $.ajax({url: '/getpopular', success: function (data) {
       var popular = $.parseJSON(data);

       $('#popular').highcharts({
        chart: {
            type: 'bar',
            margin: 75,
            options3d: {
				enabled: true,
                alpha: 15,
                beta: 15,
                depth: 110
            }
        },
        title: {
            text: 'Most popular currencies of today'
        },
        xAxis: {
        categories: popular['currencies'],
        title: {
            text: null
        }
    },
     yAxis: {
        min: 0,
        title: {
            text: 'Frequency of occurrence',
            align: 'high'
        },
        labels: {
            overflow: 'justify'
        }
    },
    tooltip: {
        valueSuffix: ''
    },
    colors: ['#006699'],
        plotOptions: {
            column: {
                depth: 40,
                stacking: false,
                grouping: false,
                groupZPadding: 10
            }
        },
        legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'top',
        x: -40,
        y: 80,
        floating: true,
        borderWidth: 1,
        backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
        shadow: true
    },
        series: [{
            name: 'Frequency',
            data: popular['scores'],
            stack: 0,
        }]
    });

   }});
});