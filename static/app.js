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
  

  var xx = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']

 var trace1 = {
  type : "scatter",
  mode: "dots",
  x: b_months,
  y: goals,
  labels: firstname + lastname,
  name: 'Goals',
  // autobinx: true, 
  // histnorm: "count", 
  // marker: 
  //   color: "rgba(255, 100, 102, 0.7)" //  line: {
  //   //   color:  "rgba(255, 100, 102, 1)", 
  //   //   // width: 1
  //   // }
  // },  
  opacity: 0.5, 
  // type: "scatter", 
  // mode: "dots",
  // xbins: {
  //   end: 2.8, 
  //   size: 0.06, 
  //   start: .5
  // }
};
var trace2 = {
  x: b_days,
  y: assists, 
  // autobinx: true, 
  marker: {
          color: "rgba(155, 200, 222, 0.7)",
           line: {
            color:  "rgba(100, 150, 102, 1)", 
            // width: 1
    } 
       }, 
  name: "assists", 
  opacity: 0.75, 
  type: "scatter", 
  mode: "dots",
  // xbins: { 
  //   end: 4, 
  //   size: 0.06, 
  //   start: -3.2

  // }
};
var trace3 = {
  x: b_days,
  y: games_played , 
  autobinx: true, 
  marker: {
          color: "rgba(225, 170, 255, 0.7)",
           line: {
            color:  "rgba(215, 200, 102, 1)", 
            width: 1
    } 
       }, 
  name: "games_played", 
  opacity: 0.9, 
  type: "bar",
  mode: "dots", 
  xbins: { 
    end: 5, 
    size: 0.06, 
    start: -2.2

  }
};
var data = [trace1];
var layout = {
  // bargap: 1, 
  // bargroupgap: 1, 
  // barmode: "overlay", 
  title: "Stats by Birthday all Skaters", 
  // xaxis: {title: "Birth Day"}, 
  yaxis: {title: "Values"}
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
         type: "linear"
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
