import requests 
from bs4 import BeautifulSoup
import pandas as pd 

#1. open the website " browser " in the background 
url= "https://www.scrapethissite.com/pages/forms"
print(f"Opening {url}...")
response = requests.get(url)

#2.Start 'reading' the HTML code of the page 
soup= BeautifulSoup(response.text, 'html.parser')

#3. Find all the team names (they are in 'td' tags with class 'name')
team_elements = soup.find_all('td', class_='name')

#4. Clean up the text and put it in a list
team_names = [team.text.strip() for team in team_elements]  

#5. Turn it into a table and save it 
df = pd.DataFrame(team_names, columns=['Hockey Team Name'])

print("n---Project 2 : SUCCESSFUL!---")
print(df.head(10)) # Print the first 10 teams found 

df.to_csv("Scraped_Hockey_Teams.csv", index=False)
print("\nFile saved as: Scraped_Hockey_Teams.csv")