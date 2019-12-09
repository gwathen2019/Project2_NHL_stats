// // REQUEST THE DATA
// function build_data(skater) {

//   // @TODO: Complete the following function that builds the metadata panel
//   const url = "/games_played/";
//   let selector = d3.select("#skater_games");
//   selector.html("");
//   d3.json(url).then((skater) => {
//     Object.entries(skater).forEach(([key, value]) => {
//       selector.append("h6")
//         .text(key + ": " + value);

//     });
//   });
// }
const url = "http://127.0.0.1:5000/games_played";
d3.json(url).then(function(data) {
    console.log(data)
    // Grab values from the response json object to build the plots
    var player = data.key;
    var games = data.value;

    var trace1 = {
      type: "scatter",
      mode: "lines",
      x: player,
      y: games,
      line: {
        color: "#17BECF"
      }
    };

    var data = [trace1];

    // var layout = {
    //   title: `this`,
    //   xaxis: {
    //     range: [startDate, endDate],
    //     type: "date"
    //   },
    //   yaxis: {
    //     autorange: true,
    //     type: "linear"
    //   }
    // };

    Plotly.newPlot("plot", data);

  });
  const url2 = "http://127.0.0.1:5000/bday_group1";
  d3.json(url2).then(function(data2) {
      console.log(data2)
        

    let trace1 = {
      labels : data2,
      values : data2,
      hovertext: data2,
      type: "pie"
    };

    let pie_data = [trace1];
    Plotly.newPlot("pie", pie_data);
  });
