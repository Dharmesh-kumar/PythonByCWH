# NOTE:- double quote ke andrt double quote lgane ke liye print(f" \"<name>\" ")ka use hotaa hai usike andr quotes ke
'''search engine:
you are given a few sentences of the list (python list of sentences). take a query string as input by the user .you have to pull out the sentences matching the sentences matching this query inputted
by the user in decreasing order of the relevance after converting every word in the query and the sentence in the lowercase. Most relevant sentence is thwe one with the maximum number if matching words with the query

sentences=["This is good","python is good","python is not python snake"]

input:
please input the query string

"python is"

output:
about 3 results found in (0.30 seconds)
1."This is good"
2. "python is good"
3."python is not python snake"'''
import time
def matchingwords(sentence1, sentence2):
    words1=sentence1.split(" ")  #split by space in the particular list element
    words2=sentence2.split(" ")
    score = 0   #how many matching words in the sentence
    for word1 in words1:
        for word2 in words2:
            # print(f"matching {word1} with {words2}")  #this is for checking the loop process
            if word1.lower() == word2.lower():
               score += 1
    return score

if __name__ == '__main__':
   # print(matchingwords("This is good","python is good"))
   sentences = ["python is good","This is a snake","Manu is a good boy","subscribe to LET'S GET KNOW"]   #this is the main list
   query =input("Please enter the query string: ")   #query is the string which we want top search in the sentences
   scores=[matchingwords(query, sentence) for sentence in sentences]   #scores ek list hai jo matchingwords function mai query se input l;ega or jo ki argument paass krega as a sentence1 or fir vha uska words se classification hga aise hi same sentencejo sentence hai vo element hai list sentences hai jo seach krega particularly in the sentences
   # print(scores)
   sortedSentScore=[sentScore for sentScore in sorted(zip(scores, sentences), reverse=True)]   #zip means EX:scores ka pehla element or sentence kew pehle element ko ek sath combine krke returbn krdega e
   #and then it sort the list by the first element scores by default and reverse true is because we want sorted as the reverse of the scores which comes max time
   # print(sortedSentScore)  #here it print the maximum nuymber of times the words in which sentence of the sentences list
   #we want sentence only
   print(f"{len(sortedSentScore)} results found in {time.process_time()} seconds\n")
   for score ,item in sortedSentScore:
       print(f"\"{item}\": with the score of {score}")