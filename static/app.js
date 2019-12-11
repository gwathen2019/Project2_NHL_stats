// // REQUEST THE DATA

const url = "http://127.0.0.1:5000/bday_group1";
d3.json(url).then(function(data) {
    console.log(data)
   
    var bdays = d3.values(data["8448208"][5])
    console.log(bdays)
    var games = d3.values(data["8448208"][6])
    console.log(games)
    stats = Object.entries(data).forEach(([key, value]) => {
      country = value[2]
      bday = value[1]
      console.log(country)
      console.log(bday)
      ; 
    });
    // Grab values from the response json object to build the plots

    var trace1 = {
      type: "scatter",
      mode: "lines",
      x: country,
      y: bday,
      line: {
        color: "#17BECF"
      }
    };

    var graph = [trace1];

  //   // var layout = {
  //   //   title: `this`,
  //   //   xaxis: {
  //   //     range: [startDate, endDate],
  //   //     type: "date"
  //   //   },
  //   //   yaxis: {
  //   //     autorange: true,
  //   //     type: "linear"
  //   //   }
  //   // };

    Plotly.newPlot("plot", graph);

  });

  const url2 = "http://127.0.0.1:5000/games_played";
  d3.json(url2).then(function(data) {
      console.log(data)

      var Jan_March = d3.values(data)
      console.log(Jan_March)
  });