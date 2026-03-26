  <!-- Main dashboard page - AI-Driven Data Analytics Dashboard -->
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>AI Data Analytics Dashboard</title>
      <link rel="stylesheet" href="css/style.css">
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
      <!-- Chart area: displays data as a visual chart -->
      <div id="chartArea" style="max-width: 800px; margin: 30px auto;">
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
                      labelKey = keys[i];
                  } else if (typeof results[0][keys[i]] === 'number') {
                      valueKey = keys[i];
                  }
              }

              if (!labelKey || !valueKey) return;

              var labels = results.map(function(row) { return row[labelKey]; });
              var values = results.map(function(row) { return row[valueKey]; });

              // Destroy previous chart if it exists
              if (currentChart) {
                  currentChart.destroy();
              }

              var ctx = document.getElementById('myChart').getContext('2d');
              currentChart = new Chart(ctx, {
                  type: 'bar',
                  data: {
                      labels: labels,
                      datasets: [{
                          label: valueKey,
                          data: values,
                          backgroundColor: '#00d4ff',
                          borderColor: '#00b4d8',
                          borderWidth: 1
                      }]
                  },
                  options: {
                      responsive: true,
                      plugins: {
                          legend: { labels: { color: '#e0e0e0' } }
                      },
                      scales: {
                          x: { ticks: { color: '#b0b0b0' } },
                          y: { ticks: { color: '#b0b0b0' }, beginAtZero: true }
                      }
                  }
              });
          }

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
                                        '<pre>' + JSON.stringify(data.results, null, 2) + '</pre>';
                  buildChart(data.results);
              })
              .catch(function(error) {
                  resultDiv.innerHTML = '<p>Connection error: ' + error.message + '</p>';
              });
          });
      </script>
  </body>
  </html>