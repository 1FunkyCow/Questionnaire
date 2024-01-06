def confession_game():
  print("Welcome to the Confession Game!\nAnswer the following questions with 'yes' or 'no':")

  questions = [
      "Have you ever had a crush on someone?",
      "Do you believe in love at first sight?",
      "Have you ever written a love letter?",
      "Would you go on a spontaneous romantic adventure?",
      "Have you ever serenaded someone?",
      "Do you enjoy watching romantic movies?",
      "Have you participated in a couple's dance?",
      "Do you believe in soulmates?",
      "Would you write your own wedding vows?",
      "Do you think love conquers all?"
  ]

  answers = [input(question).lower() for question in questions]

  print("\nProcessing your answers...")

  # Create a confession based on the answers
  confession = ""
  yes_count = answers.count("yes")

  if yes_count == 10:
      confession = "You're a true romantic at heart, embracing every aspect of love with passion!"
  elif yes_count >= 5:
      confession = "Your answers suggest a romantic side. Love has a special place in your heart."
  else:
      confession = "Your responses indicate a more reserved approach to matters of the heart. That's perfectly okay!"

  print("\nHere's your confession:")
  print(confession)

  # Personal confession
  print("\nNow, it's my turn...")

  your_response = input("Do you have feelings for me? (yes/no) ").lower()

  if your_response == "yes":
      print("\nWow, that's incredible! I must confess, I have feelings for you too.")
      print("Let's see where this journey takes us!")
  else:
      print("\nThank you for your honesty. Regardless of the answer, I appreciate our connection.")
      print("Let's continue being friends!")

# Call the function to play the game
confession_game()
