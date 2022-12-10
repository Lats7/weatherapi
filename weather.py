# This line imports the "requests" and "json" modules from the "dependencies" folder
from dependencies import json

import requests


# This is the main function of the program, and it is called when the program is executed
def main():
  # This line uses the print function to output a message to the console
  print("The 'requests' module has been imported successfully!")

  # This line imports the "api_key" module from the "dependencies" folder
  from dependencies.apiKey import apiKey

  # This line uses the requests module to make a request to an external API
  response = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/melbourne?unitGroup=metric&contentType=json", headers={
  "Authorization": f"Bearer {apiKey}"
})


  # This line prints the response from the API to the console
  print(response.text)

  # This line checks the status code of the response to see if the request was successful
  if response.status_code == 200:
    # This line uses the print function to output a message to the console
    print("The request was successful and the API key was valid!")

    # This line uses the JSON module to parse the response from the API
    data = json.loads(response.text)

    # This line uses the print function to output the data from the API to the console
    print(data)
  else:
    # This line uses the print function to output a message to the console
    print("The request failed or the API key was invalid.")

# This line tells the Python interpreter to call the main function when the program is executed
if __name__ == "__main__":
  main()