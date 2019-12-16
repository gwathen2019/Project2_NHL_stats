const url = "http://127.0.0.1:5000/bday_group1";
d3.json(url).then(function(data) {

            
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December'],
			datasets: [{
				label: 'USA',
				// backgroundColor: window.chartColors.red,
				stack: 'Stack 0',
				data: [
                   
                ],
                backgroundColor: [
                    'rgba(155, 199, 32, 0.2)'
                   
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)'
                    
                ],
                borderWidth: 1
            
			}, {
				label: 'CANADA',
				// backgroundColor: window.chartColors.blue,
				stack: 'Stack 1',
				data: [
					35,27,45,34,45,24,76,23,43,34,56,34 
                ],
                backgroundColor: [
                    'rgba(105, 69, 192, 0.2)',
                    'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
                     
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)'                    
                ],
                borderWidth: 1
			}, {
                label: 'ACROSS THE ATLANTIC',
				// backgroundColor: window.chartColors.green,
				stack: 'Stack 2',
				data: [
					53,64,43,62,16,37,15,65,3,65,35,27
                ],
                backgroundColor: [
                    'rgba(225, 125, 115, 0.2)'
                   
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)'
                    
                ],
                borderWidth: 1
			}]

        };
    });
		window.onload = function() {
			var ctx = document.getElementById('myChart').getContext('2d');
			window.myBar = new Chart(ctx, {
				type: 'bar',
				data: barChartData,
				options: {
					title: {
						display: true,
						text: 'Points by Birthmonth group'
					},
					tooltips: {
						mode: 'index',
						intersect: false
					},
					responsive: true,
					scales: {
						xAxes: [{
							stacked: true,
						}],
						yAxes: [{
							stacked: true
						}]
					}
				}
			});
		};

		document.getElementById('country_data').addEventListener('click', function() {
			barChartData.datasets.forEach(function(dataset) {
				dataset.data = dataset.data.map(function() {
					return data();
				});
			});
			window.myBar.update();
		});
	