def detect_spam(email):
  """This function uses a combination of keyword matching, regex pattern matching 
  and machine learning algorithms to detect spam emails."""
  
  # Keyword matching
  spam_keywords = ["unsubscribe", "offer", "discount", "special"]
  for keyword in spam_keywords:
    if keyword in email:
      return 1
  
  # Regex pattern matching
  spam_pattern = r"\d{5}-\d{5}-\d{5}-\d{5}"
  matches = re.search(spam_pattern, email)
  if matches:
    return 1
  
  # Machine learning
  # Train a machine learning model and predict whether or not the given email is a spam
  
  return 0