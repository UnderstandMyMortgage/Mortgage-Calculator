// This is a sample script file for the Flask application

// Function to display a message
function showMessage(message) {
  alert(message);
}

// Function to make an AJAX request
function makeRequest(url, method, data, callback) {
  var xhr = new XMLHttpRequest();
  xhr.open(method, url, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      callback(xhr.responseText);
    }
  };
  xhr.send(JSON.stringify(data));
}