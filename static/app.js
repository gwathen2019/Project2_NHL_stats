// // REQUEST THE DATA
// const url3 = "http://127.0.0.1:5000/bday_group1";
// d3.json(url3).then(function(data) {
//     console.log(data)

// function find_in_object(data, datetime){

//   return data.filter(function(obj) {
//     return Object.values(datetime).every(function(c) {
//       return obj[c] == bdays[c];
//     });
//   });

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
//#######################################################################  
var trace1 = {
  type: "scatter",
  mode: "dots",
  x: [],
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

  });
  var defaultURL = "http://127.0.0.1:5000/";
d3.json(defaultURL).then(function(data) {
  var data = [data];
  var layout = { margin: { t: 30, b: 100 } };
  Plotly.plot("bar", data, layout);
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