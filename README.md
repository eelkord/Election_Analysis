# Election_Analysis
Analysis using Python
Written Analysis of the Election Audit:
 

                                          1.     Overview of Election Audit: 
 
 
Purpose of this election audit analysis is to provide conclusion analysis of the data by providing the total number of votes per county and
the total number of votes for all counties. Then determining the winning voted county and determine the number of votes the winning county
has received and what percentage of votes compared to each other county.

 
 
2.     Election-Audit Result: 

 	   - How many votes were cast in this congressional election? 

        1.	Total Number of votes: 369,711 

	   - Provide a breakdown of the number of votes and the percentage of total votes for each county in this precinct 

        1.	Jefferson County received 38,855 votes with a percentage of 10.5%
        2.	Denver County received 306,055 votes with a percentage of 82.8%
        3.	Arapahoe County received 24,801 votes with a percentage of 6.7%

3.	Which county had the largest number of votes: 

        1.	Largest number of votes were given to Denver County

4.	Provide a breakdown of the number of votes and the percentage of the total votes each candidate received 

        1.	Charles Casper Stockham: 23.0% (85,213)
        2.	Diana DeGette: 73.8% (272,892)
        3.	Raymon Anthony Doane: 3.1% (11,606)

5.	Which candidate won the election, what was their vote count, and what was their percentage of the total votes? 

        1.	Candidate Diana Degette won the highest number of votes 
        2.	Diana Degette received 272,892 votes
        3.	Diana Degette received 73.8% of the total percentage

3.     Election-Audit Summary: 

	The code can be used for any election bearing in mind the column number can be changed depending on the data for the candidate_name
  or the county_name

# Get the candidate name from each row.
  
        candidate_name = row[2]

        # 3: Extract the county name from each row.//
        county_name = row[1]



The output file can be changed with the below code:

	The code can also be outputted to a deferent file name using a deferent path similar to file_to_save_election_results = os.path.join("analysis", "election_results.txt")

  Also a similar For loop can be provided if the measurements and the analysis if there were to be produced per city or per province


  for county_name in county_list: 
        # 6b: Retrieve the county vote count.
        countyVotes = county_votes.get(county_name)
        
        # 6c: Calculate the percentage of votes for the county.
        Percentage = float(countyVotes)/ float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (f"{county_name}: {Percentage:.1f}% ({countyVotes:,})\n")

         # 6e: Save the county votes to a text file.
              
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (countyVotes > number_votes_county) and (Percentage > winning_county_percentage):
            number_votes_county = countyVotes
            winning_county = county_name
            winning_county_percentage = Percentage 

![image](https://user-images.githubusercontent.com/100106554/159395408-78c9651d-ab32-4437-a36d-4349d152a975.png)
