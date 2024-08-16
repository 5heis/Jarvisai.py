import datetime
import requests
from bs4 import BeautifulSoup
import wolframalpha

def main():
    print("Welcome! Please type 'wake up' to activate the assistant.")
    
    # Initialize Wolfram Alpha client
    wolfram_app_id = 'WOLFRAM_APP_ID'
    client = wolframalpha.Client(wolfram_app_id)
    
    while True:
        try:
            query = input("Enter your query: ").lower()
        except EOFError:
            print("\nNo input provided. Exiting the program.")
            break
        
        if "wake up" in query:
            print("Assistant activated. How can I help you?")
            
            while True:
                try:
                    query = input("Enter your query: ").lower()
                except EOFError:
                    print("\nNo input provided. Exiting the program.")
                    break
                
                if "go to sleep" in query:
                    print("Assistant deactivated. You can call me anytime by typing 'wake up'.")
                    break
                
                elif "calculate" in query:
                    try:
                        equation = query.replace("calculate", "").strip()
                        res = client.query(equation)
                        answer = next(res.results).text
                        print(f"The answer to '{equation}' is {answer}")
                    except Exception as e:
                        print(f"Error calculating equation: {e}")
                
                elif "weather" in query:
                    try:
                        search = "temperature in Lagos, Nigeria"
                        url = f"https://www.google.com/search?q={search}"
                        r = requests.get(url)
                        r.raise_for_status()  # Check if the request was successful
                        data = BeautifulSoup(r.text, "html.parser")
                        temp = data.find("div", class_="BNeawe").text
                        print(f"Current {search} is {temp}")
                    except requests.exceptions.RequestException as e:
                        print(f"Error fetching weather data: {e}")
                
                elif "set an alarm" in query:
                    alarm_time = input("Please enter the alarm time (HH:MM): ")
                    print(f"Alarm set for {alarm_time}.")
                    # implement the alarm functionality.
                
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    print(f"The current time is {strTime}")
                
                elif "remember that" in query:
                    remember_message = input("What would you like me to remember? ")
                    try:
                        with open("Remember.txt", "a") as remember_file:
                            remember_file.write(remember_message + "\n")
                        print("I will remember that.")
                    except IOError as e:
                        print(f"Error writing to file: {e}")
                
                elif "what do you remember" in query:
                    try:
                        with open("Remember.txt", "r") as remember_file:
                            memories = remember_file.read()
                        if memories:
                            print(f"You asked me to remember: {memories}")
                        else:
                            print("I don't have anything to remember.")
                    except FileNotFoundError:
                        print("I don't have anything to remember.")
                    except IOError as e:
                        print(f"Error reading from file: {e}")
                
                elif "shutdown system" in query:
                    confirm_shutdown = input("Are you sure you want to shutdown the system? (yes/no): ").lower()
                    if confirm_shutdown == "yes":
                        print("Shutting down the system...")
                        
                        os.system("shutdown /s /t 1")
                    else:
                        print("Shutdown canceled.")

if __name__ == "__main__":
    main()
