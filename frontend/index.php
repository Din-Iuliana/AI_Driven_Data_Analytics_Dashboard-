  <!-- Main dashboard page - AI-Driven Data Analytics Dashboard -->
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>AI Data Analytics Dashboard</title>
      <link rel="stylesheet" href="css/style.css?v=4">
      <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  </head>
  <body>
      <h1>AI Data Analytics Dashboard</h1>

      <!-- Chat form: user types a question in natural language -->
      <form id="queryForm">
          <label for="question">Ask a question about your data:</label>
          <br>
          <input type="text" id="question" name="question"
                 placeholder="e.g. Who are the top 5 customers by sales?"
                 required>
          <button type="submit">Send</button>
      </form>

      <!-- Response area: shows the result from the backend -->
      <div id="result">
          <p>Ask a question to see results here.</p>
      </div>
      <!-- Optimize button: asks AI to analyze query performance -->                                                                                                                                           
      <div id="optimizeArea" style="max-width: 800px; margin: 10px auto; display: none;">                                                                                                                      
          <button id="optimizeBtn" type="button">Analyze Performance</button>
          <div id="optimizeResult"></div>                                                                                                                                                                      
      </div>
      <!-- Chart area: displays data as a visual chart -->
      <div id="chartArea" style="max-width: 500px; margin: 30px auto;">
          <canvas id="myChart"></canvas>
      </div>
      <script>
          var currentChart = null;

          function buildChart(results) {
              if (!results || results.length === 0) return;

              var keys = Object.keys(results[0]);

              // Find a text column (labels) and a number column (values)
              var labelKey = null;
              var valueKey = null;

              for (var i = 0; i < keys.length; i++) {
                  if (typeof results[0][keys[i]] === 'string') {
                      if (!labelKey) labelKey = keys[i];
                  } else if (typeof results[0][keys[i]] === 'number') {
                      valueKey = keys[i];
                  }
              }

              if (!labelKey || !valueKey) return;

              var labels = results.map(function(row) { return row[labelKey]; });
              var values = results.map(function(row) { return row[valueKey]; });

              // Auto-detect chart type
              var chartType = 'bar';
              var isTimeBased = labels.some(function(label) {
                  return /^\d{4}[-\/]/.test(label) || /^(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\b/i.test(label);
              });

              if (isTimeBased) {
                  chartType = 'line';
              } else if (results.length <= 5) {
                  chartType = 'pie';
              }

              // Generate colors for pie chart
              var colors = ['#00d4ff', '#ff6384', '#ffce56', '#4bc0c0', '#9966ff',
                            '#ff9f40', '#36a2eb', '#c9cbcf', '#7bc67e', '#e77c8e'];

              // Destroy previous chart if it exists
              if (currentChart) {
                  currentChart.destroy();
              }

              var ctx = document.getElementById('myChart').getContext('2d');
              currentChart = new Chart(ctx, {
                  type: chartType,
                  data: {
                      labels: labels,
                      datasets: [{
                          label: valueKey,
                          data: values,
                          backgroundColor: chartType === 'pie'
                              ? colors.slice(0, values.length)
                              : '#00d4ff',
                          borderColor: chartType === 'line' ? '#00d4ff' : '#00b4d8',
                          borderWidth: chartType === 'line' ? 2 : 1,
                          tension: 0.3,
                          fill: false
                      }]
                  },
                  options: {
                      responsive: true,
                      plugins: {
                          legend: { labels: { color: '#e0e0e0' } },
                          tooltip: {
                              callbacks: {
                                  label: function(context) {
                                      if (chartType !== 'pie') return context.dataset.label + ': ' + context.raw;
                                      var total = context.dataset.data.reduce(function(a, b) { return a + b; }, 0);
                                      var percent = ((context.raw / total) * 100).toFixed(1);
                                      return context.label + ': ' + percent + '%';
                                  }
                              }
                          }
                      },
                      scales: chartType === 'pie' ? {} : {
                          x: { ticks: { color: '#b0b0b0' } },
                          y: { ticks: { color: '#b0b0b0' }, beginAtZero: true }
                      }
                  }
              });
          }
          function buildTable(results) {
              if (!results || results.length === 0) return '<p>No results found.</p>';

              var keys = Object.keys(results[0]);
              var html = '<table><thead><tr>';

              for (var i = 0; i < keys.length; i++) {
                  html += '<th>' + keys[i] + '</th>';
              }
              html += '</tr></thead><tbody>';

              for (var j = 0; j < results.length; j++) {
                  html += '<tr>';
                  for (var k = 0; k < keys.length; k++) {
                      html += '<td>' + results[j][keys[k]] + '</td>';
                  }
                  html += '</tr>';
              }
              html += '</tbody></table>';
              return html;
          }
                    var lastSQL = '';

          document.getElementById('optimizeBtn').addEventListener('click', function() {
              var optimizeResult = document.getElementById('optimizeResult');
              optimizeResult.innerHTML = '<p>Analyzing...</p>';

              fetch('http://localhost:8000/api/optimize', {
                  method: 'POST',
                  headers: {'Content-Type': 'application/json'},
                  body: JSON.stringify({sql: lastSQL})
              })
              .then(function(response) { return response.json(); })
              .then(function(data) {
                  if (data.error) {
                      optimizeResult.innerHTML = '<p>Error: ' + data.error + '</p>';
                      return;
                  }
                  optimizeResult.innerHTML = '<pre>' + data.suggestion + '</pre>';
              })
              .catch(function(error) {
                  optimizeResult.innerHTML = '<p>Connection error: ' + error.message + '</p>';
              });
          });

          document.getElementById('queryForm').addEventListener('submit', function(e) {
              e.preventDefault();

              var question = document.getElementById('question').value;
              var resultDiv = document.getElementById('result');

              resultDiv.innerHTML = '<p>Loading...</p>';

              fetch('http://localhost:8000/api/query', {
                  method: 'POST',
                  headers: {'Content-Type': 'application/json'},
                  body: JSON.stringify({question: question})
              })
              .then(function(response) { return response.json(); })
              .then(function(data) {
                  if (data.error) {
                      resultDiv.innerHTML = '<p>Error: ' + data.error + '</p>';
                      return;
                  }
                  resultDiv.innerHTML = '<p>SQL: ' + data.sql + '</p>' +                                                                                                                                       
                                        buildTable(data.results);
                  buildChart(data.results);
                  lastSQL = data.sql;
                  document.getElementById('optimizeArea').style.display = 'block';
                  })
              .catch(function(error) {
                  resultDiv.innerHTML = '<p>Connection error: ' + error.message + '</p>';
              });
          });
      </script>
  </body>
  </html>