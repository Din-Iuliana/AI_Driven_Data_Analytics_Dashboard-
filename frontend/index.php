<!-- Main dashboard page - AI-Driven Data Analytics Dashboard -->
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>AI Data Analytics Dashboard</title>
  </head>
  <body>
      <h1>AI-Driven Data Analytics Dashboard</h1>
      <p>Backend status: Loading...</p>

      <script>
          fetch('http://localhost:8000/')
              .then(response => response.json())
              .then(data => {
                  document.querySelector('p').textContent = 'Backend status: ' + data.status;
              })
              .catch(error => {
                  document.querySelector('p').textContent = 'Backend status: Not connected';
              });
      </script>
  </body>
  </html>