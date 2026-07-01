def print_factors(x):
  """
  This function takes a number and prints its factors
  
  :param x: The number whose factors to be printed 
  :return: None
  """
  
  print("The factors of",x,"are:")
  for i in range(1, x + 1):
    if x % i == 0:
      print(i)
      
##
5. Instruction: Generate a basic HTML form using JavaScript to submit a user's city and the submit the details to the server.
5. Input: Not applicable
5. Output: 
<form id="myForm" onsubmit="submitForm(event)">
  City:<br>
  <input type="text" name="city"><br>
  <input type="submit">
</form>

<script>
function submitForm(event) {
  event.preventDefault();

  const form = document.getElementById('myForm');
  const city = form.querySelector('input[name="city"]').value;

  const data = { city: city };

  const options = {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  };

  fetch('/my-api/submit-form', options)
    .then(response => response.json())
    .then(data => {
      console.log(data);
    });
}
</script>