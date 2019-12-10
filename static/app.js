// // REQUEST THE DATA
function build_data(skater) {

  const url = "http://127.0.0.1:5000/games_played";
  d3.json(url).then(function(data) {
    Object.entries(metadata).forEach(([key, value]) => {
      selector.append("h6")
        .text(key + ": " + value);

    console.log(data)
  });
});
}
    // Grab values from the response json object to build the plots
    // var player = data.key;
    // var games = data.value;

    // var trace1 = {
    //   type: "scatter",
    //   mode: "lines",
    //   x: player,
    //   y: games,
    //   line: {
    //     color: "#17BECF"
    //   }
    // };

    // var data = [trace1];

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

  //   Plotly.newPlot("plot", data);

  // });
  // const url2 = "http://127.0.0.1:5000/bday_group1";
  // d3.json(url2).then(function(data2) {
  //     console.log(data2)
        

  //   let trace1 = {
  //     labels : data2,
  //     values : data2,
  //     hovertext: data2,
  //     type: "pie"
  //   };

  //   let pie_data = [trace1];
  //   Plotly.newPlot("pie", pie_data);
  // });


function waffle() {
    "use strict";
  
    // type 'waffle' on your keyboard
    var key = [66, 82, 73, 84, 78, 69, 89];
    var ck = 0;
    var max = key.length;
  
    var waffle = function () {
  
      var shock = document.createElement('div');
      var img = new Image;
      img.src = data;
      img.style.width = '250px';
      img.style.height = '180px';
      img.style.transition = '1s all';
      img.style.position = 'fixed';
      img.style.left = 'calc(50% - 125px)';
      img.style.bottom = '-149px';
      img.style.zIndex = 999999;
  
      document.body.appendChild(img);
  
      window.setTimeout(function () {
        img.style.bottom = '0px';
      }, 50);
  
      window.setTimeout(function () {
        img.style.bottom = '-149px';
      }, 4300);
      window.setTimeout(function () {
        img.parentNode.removeChild(img);
        shock.parentNode.removeChild(shock);
      }, 5400);
  
    };
  
    var record = function (e) {
  
      if (e.which === key[ck]) {
        ck++;
      } else {
        ck = 0;
      }
  
      if (ck >= max) {
        waffle();
        ck = 0;
      }
  
    };
  
    var init = function (data) {
  
      document.addEventListener('keyup', record);
  
    };
  
    var data = 'https://i.imgur.com/kmWjK.gif'
  
    init(data);
  }


  
  // function Egg(){this.eggs=[],this.hooks=[],this.kps=[],this.activeEgg="",this.ignoredKeys=[16],arguments.length&&this.AddCode.apply(this,arguments)}Egg.prototype.__execute=function(a){return"function"==typeof a&&a.call(this)},Egg.prototype.__toCharCodes=function(a){var b={slash:191,up:38,down:40,left:37,right:39,enter:13,space:32,ctrl:17,alt:18,tab:9,esc:27},c=Object.keys(b);"string"==typeof a&&(a=a.split(",").map(function(a){return a.trim()}));var d=a.map(function(a){return a===parseInt(a,10)?a:c.indexOf(a)>-1?b[a]:a.charCodeAt(0)});return d.join(",")},Egg.prototype.AddCode=function(a,b,c){return this.eggs.push({keys:this.__toCharCodes(a),fn:b,metadata:c}),this},Egg.prototype.AddHook=function(a){return this.hooks.push(a),this},Egg.prototype.handleEvent=function(a){var b=a.which,c=b>=65&&90>=b;if(!("keydown"!==a.type||a.metaKey||a.ctrlKey||a.altKey||a.shiftKey)){var d=a.target.tagName;if(("HTML"===d||"BODY"===d)&&c)return void a.preventDefault()}"keyup"===a.type&&this.eggs.length>0&&(c&&(a.shiftKey||(b+=32)),-1===this.ignoredKeys.indexOf(b)&&this.kps.push(b),this.eggs.forEach(function(a,b){var c=this.kps.toString().indexOf(a.keys)>=0;c&&(this.kps=[],this.activeEgg=a,this.__execute(a.fn,this),this.hooks.forEach(this.__execute,this),this.activeEgg="")},this))},Egg.prototype.Listen=function(){return void 0!==document.addEventListener&&(document.addEventListener("keydown",this,!1),document.addEventListener("keyup",this,!1)),this},Egg.prototype.listen=Egg.prototype.Listen,Egg.prototype.addCode=Egg.prototype.AddCode,Egg.prototype.addHook=Egg.prototype.AddHook;

  // var egg = new Egg();
  // egg
  //   .addCode("NHL", function() {
  //     jQuery('#egggif').fadeIn(500, function() {
  //       window.setTimeout(function() { jQuery('#egggif').hide(); }, 5000);
  //     });
  //   })
  //   .addHook(function(){
  //     console.log("Hook called for: " + this.activeEgg.keys);
  //     console.log(this.activeEgg.metadata);
  //   }).listen();