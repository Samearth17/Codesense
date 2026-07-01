<!DOCTYPE html>
<html>

<head>
 <title>HTML and Python</title>
 <script>
  // Function to submit data to python program
  function submitData() {
   let myForm = document.getElementById("myForm");
   let formData = new FormData(myForm);
   formData.append("inputData", document.getElementById("inputData").value);

   fetch('/submit', {
    method: 'POST',
    body: formData
   });
  }
 </script>
</head>

<body>
 <form id="myForm" action="/submit" method="POST">
  <input type="text" id="inputData"/>
  <input type="submit" value="Send data" onclick="submitData()">
 </form>
</body>
</html>