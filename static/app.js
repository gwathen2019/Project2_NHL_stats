// REQUEST THE DATA


const url3 = "http://127.0.0.1:5000/bday_group1";
d3.json(url3).then(function(data) {
  // console.log(data)
  var b_months = Object.values(data['birth_month'])
  console.log(b_months)
  var b_days = Object.values(data['bday'])
  console.log(b_days)
  var id = Object.values(data['id'])
  var goals = Object.values(data['goals'])
  console.log(goals)
  var assists = Object.values(data['assists'])
  console.log(assists)
  var points = Object.values(data['points'])
  var firstname = Object.values(data['first_name'])
  var lastname = Object.values(data['last_name'])
  var games_played = Object.values(data['games'])
  var nationality = Object.values(data['nation'])
 
  
  // var trace1 = {
  //   x: b_days,
  //   y: games_played,
  //   // mode: 'line',
  //   opacity: .5,
  //   type: 'bar',
  //   name: 'goals',
  //   text: firstname,
  //   marker: { size: 8 }
  // };
  
  var trace2 = {
    x: b_days,
    y: games_played,
    mode: 'markers',
    opacity : .5,
    type: 'bar',
    name: 'games played',
    text: lastname,
    marker: { color : 'Black',
      size: 7,
      line: {
        color: 'MediumPurple',
        width: 1
      }
      }
  };
  
  var trace3 = {
    x: b_days,
    y: points,
    mode: 'markers',
    opacity : .9,
    type: 'scatter',
    name: 'points',
    text: firstname,
    marker: { color : 'LightSkyBlue',
      size: 12,
      line: {
        color: 'MediumPurple',
        width: 1
      }
      }
  };
  var data = [ trace2, trace3 ];
  
  var layout = {
    xaxis: {
      range: [ -20, 135 ]

    },
    yaxis: {
      range: [0, 650],
      title: 'Goals + Assists'
    },
    title:'Top Scoring Skaters by Birthday'
  };
  

Plotly.newPlot('histogram', data, layout);
});

//####################################################################### 
//GRAPH THAT UPDATES ON SELECTION: 
    var trace1 = {
      type: "scatter",
      mode: "dots",
      x: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December'],
      y: [],
      line: {
        color: "#17BECF"
      }
    };

    var graph = [trace1];

     var layout = {
       title: `Toggle Between Countries of Birth`,
       xaxis: {
         autorange: true,
         type: "months"
        
       },
       yaxis: {
         autorange: true,
         type: "linear",
         title: "# players in NHL"
       }
     };

    Plotly.newPlot("plot", graph, layout);

  var defaultURL = "http://127.0.0.1:5000/";
 d3.json(defaultURL).then(function(data) {
  var data = [data];
  var layout = { margin: { t: 30, b: 100 } };
  Plotly.plot("scatter", data, layout);
});

function updatePlotly(newdata) {
  Plotly.restyle("plot", "x", [newdata.x]);
  Plotly.restyle("plot", "y", [newdata.y]);
}
  
  // Get new data whenever the dropdown selection changes
function getData(route) {
  console.log(route);
  d3.json(`/${route}`).then(function(data) {
  console.log("newdata", data);
  updatePlotly(data);
  
 });
}

