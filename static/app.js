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

<<<<<<< HEAD
// }
const url = "http://127.0.0.1:5000/bday_group1";
d3.json(url).then(function(data) {
    console.log(data)
   
    // var bdays = d3.values(data["8448208"][5])
    // console.log(bdays)
    // var games = d3.values(data["8448208"][6])
    // console.log(games)
    stats = Object.entries(data).forEach(([key, value]) => {
      country = value[2]
      bday = value[1]
      // console.log(country)
      // console.log(bday)
      ; 
    });
    // Grab values from the response json object to build the plots
    var months = ["Jan","Feb","Mar","Apr","May","June","July","August","September","October","November","December"] 
    var b_days_USA = [280,270,230,285,225,180,140,175,145,80,130,145]
    var b_days_CAN = [280,270,230,285,225,180,140,175,145,80,130,145]
    var b_days_CHE = [280,270,230,285,225,180,140,175,145,80,130,145]
    
=======
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
>>>>>>> 7961ef5d3c371f662422565a55e32e087427663a
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
<<<<<<< HEAD
       title: `birthday_effect`,
=======
       title: `Toggle Between Countries of Birth`,
>>>>>>> 7961ef5d3c371f662422565a55e32e087427663a
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

<<<<<<< HEAD
  });
  ////histogram
  var data = [{
    type: "sunburst",
    ids: [
      "January", "February", "March", "April", "May",
      "June", "July", "August",
      "September","October", "November",
      "December", 
    ],
    labels: [
      "January", "February", "March", "April", "May",
      "June", "July", "August",
      "September","October", "November",
      "December", 
    ],
    parents: [
      "", "", "", "North America", "North America", "North America", "Europe",
      "Europe", "Europe","Australia", "Australia - Football", "Australia - Football",
      "Australia - Football", "Australia - Football", "Australia - Rugby",
      "Australia - Rugby"
    ],
    outsidetextfont: {size: 20, color: "#377eb8"},
    // leaf: {opacity: 0.4},
    marker: {line: {width: 2}},
  }];
  
  var layout = {
    margin: {l: 0, r: 0, b: 0, t:0},
    sunburstcolorway:["#636efa","#ef553b","#00cc96"],
  };
  
  
  Plotly.newPlot('myDiv', data, layout);
//////////

const url2 = "http://127.0.0.1:5000/games_played";
d3.json(url2).then(function(data) {
    console.log(data)

    var Jan_March = d3.values(data)
    console.log(Jan_March)
});

var defaultURL = "http://127.0.0.1:5000/";
d3.json(defaultURL).then(function(data) {
=======
  var defaultURL = "http://127.0.0.1:5000/";
 d3.json(defaultURL).then(function(data) {
>>>>>>> 7961ef5d3c371f662422565a55e32e087427663a
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
<<<<<<< HEAD
  });
}
  
=======
  
 });
}

>>>>>>> 7961ef5d3c371f662422565a55e32e087427663a
