<!DOCTYPE html>
<html>
<head>
 <title>Form Example</title>
</head>
<body>
 <h1>Form Example</h1>
 <form action="submit.php" method="post">
 <label for="nameInput">Name:</label>
 <input type="text" id="nameInput" name="name" />
 
 <label for="languageSelect">Favorite Language:</label>
 <select id="languageSelect" name="language">
 <option value="java">Java</option>
 <option value="javascript">Javascript</option>
 <option value="python">Python</option>
 </select>
 
 <input type="submit" value="Submit" />
 </form>
</body>
</html>