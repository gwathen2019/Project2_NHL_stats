// REQUEST THE DATA
const url4 = "http://127.0.0.1:5000/bday_group1";
d3.json(url4).then(function(data) {
    // console.log(data)
    var goals = Object.values(data['goals']['birth_month'])
    console.log(goals);
});

const url3 = "http://127.0.0.1:5000/goals";
d3.json(url3).then(function(data) {
  var goals_data = Object.values(data['goals']);
  // console.log(goals_data);
  // console.log(goals_data[0]);
  
  var USA_goals = Object.values(data['goals']);
  // console.log(USA_goals);
  var CAN_goals = Object.values(data['goals']);
  // console.log(CAN_goals)
  var ATL_goals = Object.values(data['goals']);
  // console.log(ATL_goals)
  var USA_players = Object.values(data['birthmonth']);

  var xx = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']

 var trace1 = {
  x: USA_players,
  y: USA_goals,
  name: 'USA',
  autobinx: true, 
  histnorm: "count", 
  marker: {
    color: "rgba(255, 100, 102, 0.7)", 
     line: {
      color:  "rgba(255, 100, 102, 1)", 
      width: 1
    }
  },  
  opacity: 0.5, 
  type: "histogram", 
  // xbins: {
  //   end: 2.8, 
  //   size: 0.06, 
  //   start: .5
  // }
};
var trace2 = {
  x: USA_players,
  y: CAN_goals, 
  autobinx: true, 
  marker: {
          color: "rgba(255, 200, 102, 0.7)",
           line: {
            color:  "rgba(100, 200, 102, 1)", 
            width: 1
    } 
       }, 
  name: "CANADA", 
  opacity: 0.75, 
  type: "histogram", 
  // xbins: { 
  //   end: 4, 
  //   size: 0.06, 
  //   start: -3.2

  // }
};
var trace3 = {
  x: USA_players,
  y: ATL_goals , 
  autobinx: true, 
  marker: {
          color: "rgba(100, 200, 102, 0.7)",
           line: {
            color:  "rgba(100, 200, 102, 1)", 
            width: 1
    } 
       }, 
  name: "Across the Atlantic", 
  opacity: 0.9, 
  type: "histogram", 
  // xbins: { 
  //   end: 5, 
  //   size: 0.06, 
  //   start: -2.2

  // }
};
var data = [trace1, trace2, trace3];
var layout = {
  bargap: 0.05, 
  bargroupgap: 0.2, 
  barmode: "overlay", 
  title: "GOALS BY BIRTHMONTH AND COUNTRY", 
  xaxis: {title: "BIRTHMONTH"}, 
  yaxis: {title: "Count"}
};
Plotly.newPlot('histogram', data, layout);
});

const url = "http://127.0.0.1:5000/games_played";
d3.json(url).then(function(data) {
  // var goals = Object.values(data)['totalGoals'];
  // console.log(goals)
  var games_data = Object.values(data);
  console.log(games_data);
  var x_data = Object.keys(data);
  console.log(x_data)
  // var players = y_data.split(',').map(Number);
  // console.log(players)
//   Object.entries(data).forEach(key => {
//     goals = values['totalGoals']
//     console.log(goals)
//   });
// });
  // console.log(data)
//****************************************************** */
//   const goals = Object.entries(data).map(
//     element => ({'totalGoals': element['totalGoals']}))
//   console.log(goals);
//   return goals;
// });
//********************************************************* */
//     const goals = data.map(object => object.totalGoals);
//     console.log(goals)
// });
// //************************************************************* */
//  const goals = {};
 

//  Object.entries(data).forEach(([key, value]) => {
//   goals[key['totalGoals']] = value['totalGoals'];
//   // console.log(goals);
//  });

//  const goals2  = goals.map(
//   element => ({'undefined': element['undefined']}));
//   console.log(goals2);


  // var country = []
  // var bday = Object.entries(data).forEach(([key, value]) => {
    


  //     if (key === "birthDate") {
  //       bday.push(value);
  //     };
  // });
    
  // });
  


    // });

      var trace2 = {
        type: "scatter",
        mode: "dots",
        x: x_data,
        y: games_data,
        line: {
          color: "#17BECF"
        }
      };
  
      var graph2 = [trace2];
  
       var layout = {
         title: `Goals`,
         xaxis: {
           autorange: true,
           type: "linear"
         },
         yaxis: {
           autorange: true,
           type: "linear"
         }
       };
  
      Plotly.newPlot("plot_goals", graph2, layout);
    });
    

//#######################################################################  
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
