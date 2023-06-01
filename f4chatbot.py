def greet():
    print("Hello! How can I assist you today?")

def get_customer_name():
    print("May I know your name, please?")
    name = input()
    print(f"Nice to meet you, {name}!")

def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")

def age():
    print("May I know your age, please?")
    age = input()
    print(f"Hello! Your age is {age}.")
def handle_customer_inquiry():
    print("What can I help you with?")
    inquiry = input()
    print(f"I'm sorry, {inquiry} is beyond my capabilities.")

def thank_customer():
    print("Thank you for reaching out. Have a great day!")

# Chatbot main function
def chatbot():
    greet('Sbot', '2021')
    get_customer_name()
    age()
    handle_customer_inquiry()
    thank_customer()

# Run the chatbot
chatbot()

"""
def hospital_management_system():
    print("Welcome to the Hospital Management System.")

    # Symptom input
    print("Please enter your symptoms, one at a time (type 'done' when finished):")
    symptoms = []
    while True:
        symptom = input()
        if symptom.lower() == 'done':
            break
        symptoms.append(symptom)

    # Diagnosis based on symptoms
    if 'fever' in symptoms and 'cough' in symptoms:
        diagnosis = 'You may have a common cold.'
    else:
        diagnosis = 'Unable to diagnose your condition based on provided symptoms.'

    # Treatment recommendation based on diagnosis
    if 'common cold' in diagnosis:
        treatment = 'Get plenty of rest, drink fluids, and take over-the-counter cold medication.'
    else:
        treatment = 'Please consult a doctor for further evaluation and treatment.'

    # Display diagnosis and treatment recommendation
    print("Diagnosis:", diagnosis)
    print("Treatment Recommendation:", treatment)

    print("Thank you for using the Hospital Management System.")

hospital_management_system()

"""