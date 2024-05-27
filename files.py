#In addition to the requirements I've also added the option for the user to select a country of interest to see the min, max and average life expectancies for it
def main():
  print("Welcome to the life expectancy program!")

  with open('life-expectancy.csv', mode='r') as f:
    
    data = f.readlines()
    lowest, biggest = get_min_max(data)
    print(f"\nThe overall max life expectancy is: {biggest[0][3]} from {biggest[0][0]}  in {biggest[0][2]}")
    print(f"The overall min life expectancy is: {lowest[0][3]} from {lowest[0][0]}  in {lowest[0][2]} \n")
      
  while True:
    year_of_interest = input("Enter the year of interest: ")
    try:
      year_of_interest = int(year_of_interest)  
      year_of_interest = str(year_of_interest)
      break  
    except ValueError:
      print('That is not a valid year. Please enter a valid year.')

  get_interest_year_data(data, year_of_interest)
    
  country_of_interest = input("Enter the country of interest: ")
  country_of_interest = country_of_interest.title()
  get_country_data(data,country_of_interest)

def get_interest_year_data(data, year_of_interest):
  list_of_interest_years = []
  average_list = []
  
  for line in data:
    line = line.strip()
    line = line.split(',')
    
    if year_of_interest in line:
      list_of_interest_years.append(line) 
      
  for country in list_of_interest_years:
    average_list.append(float(country[3]))
    average = sum(average_list) / len(average_list)
    average = round(average,2)
    
  if list_of_interest_years == []:
    print(f'There is no data for the year {year_of_interest} :(')
    return
    
  print(f'\nThe average life expectancy across all countries in that year was: {average}')
  lowest,biggest = get_min_max(list_of_interest_years)
  print(f"The max life expectancy was in {biggest[0][0]} with {biggest[0][3]}")
  print(f"The min life expectancy was in {lowest[0][0]} with {lowest[0][3]}\n")
def get_min_max(data):
  lowest = []
  biggest = []
  biggest_life_expectancy = 0
  lowest_life_expectancy = 100
  for line in data:
    try:
      line = line.strip()
      line = line.split(',')
    except:
      pass
    
        
    if 'Life expectancy (years)' in line:
      continue
        
    life_expectancy = float(line[3])
        
        
    if life_expectancy > biggest_life_expectancy:
      biggest_life_expectancy = life_expectancy
      biggest.clear()
      biggest.append(line)

    if life_expectancy < lowest_life_expectancy:
      lowest_life_expectancy = life_expectancy
      lowest.clear()
      lowest.append(line)
  return lowest , biggest

def get_country_data(data, country_of_interest):
    country_life_expectancies = []

    for line in data:
      line = line.strip().split(',')

      if country_of_interest == line[0]:
        country_life_expectancies.append(float(line[3]))

    if country_life_expectancies == []:
      print(f'There is no data available for {country_of_interest}')
      return

    average = sum(country_life_expectancies) / len(country_life_expectancies)
    average = round(average, 2)
    min_life_expectancy = min(country_life_expectancies)
    max_life_expectancy = max(country_life_expectancies)

    print(f'\nFor {country_of_interest}:')
    print(f'Minimum life expectancy: {min_life_expectancy}')
    print(f'Maximum life expectancy: {max_life_expectancy}')
    print(f'Average life expectancy: {average}')
main()