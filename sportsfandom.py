"""
Name: Keith Crawford
Date: 03/16/23
"""
"""
This is going to be a program 
that quizzes people on different sports questions to 
assess their level of sports fandom. 
It will at the end take all of their correct answers, 
and give out an answer as to their level of sports fandom. 

"""
from string import ascii_lowercase


def main():
    #calling functions here
    kcquestions_dict=make_quiz()
    print_intro()
    press_enter_to_begin()
    kcanswers=loop_through_quiz(kcquestions_dict)
    kcscore=calculate_score(kcanswers)
    print_outro(kcscore)

def press_enter_to_begin():
    """
    User must press enter to begin the quiz. 
    Keep it in a loop until they press enter.
    """
    print()
    while (True):
        kcuser_input= input("Press enter to begin quiz")
        if kcuser_input==(""):
            break
        else:
            print(f"Invalid response!")
# kcflag=True
# kcflag=False
def debug(strvar):
    if kcflag:
        print(strvar)

def print_intro():
    """
    The welcoming message to the quiz. 
    """
    print(f"---------------------------------")
    print(f"Welcome to THE Sports Fandom Quiz")
    print(f"---------------------------------")
    print(f"You will be asked a series of questions ")
    print(f"ranging from easy, to stuff that only ")
    print(f"a true sports geek could know. At the")
    print(f"end you will be given your sports fandom level.")

def calculate_score(kclist):
    """Take the list of answers and calculate it's number to help 
    determine sports level.
    Parameters: kclist= a list of the user's correct answers
    Return: kcnum_correct= number of correct answers
    """
    kcnum_correct= len(kclist)
    return kcnum_correct

def make_quiz():
    """Create quiz questions here, and return it as a dictionary to main.
    Parameters: none.
    Return: kc_questions= A dictionary of the questions along with their
            multiple choice answers.
    """
    kc_questions= {
        "Who is MJ?":["A former basketball star player", "King of pop", "Rival to Larry Bird", "Creed actor"],
        "How many rings did Tom Brady win?": ["7", "10", "3", "8"],
        "Who did Jeremy Lin play for when he became known as 'Linsanity'": ["NY Knicks", "Houston Rockets", "LA Lakers", "Brooklyn Nets"],
        "What is the real name of soccer?": ["Football", "Soccer", "Kickball", "Americano Futbol"],        
        "How do you win in most sports?": ["Score the most points", "Least amount of points", "Best sportsmanship", "Best looking players"],
        "Who has the most rings in NBA history?": ["Bill Russell", "Wilt Chamberlain", "Michael Jordan", "Lebron James"],
        "Which RB broke the record at the time for most catches by a RB in NFL History in 2014?": ["Matt Forte", "Jamaal Charles", "Leveon Bell", "Lesean McCoy"],
        "Who owns the highest career BA in MLB history?": ["Ty Cobb", "Willie Mays", "Albert Pujols", "Mike Trout"],
        "Who hit the game winning goal for Spain in the FIFA World Cup final in 2010?": ["Andres Iniesta", "Lionel Messi", "David Villa", "Diego Maradona"],
        "Who is the youngest player to ever win the NBA MVP award?": ["Derrick Rose", "Kobe Bryant", "Giannis Antetokounmpo", "Wes Unseld"],
        "Which 2 players own the record for most goals in English Premier League history?": ["Alan Shearer/Andy Cole", "Gordon Beckham/Wayne Rooney", "Harry Kane/Thierry Henry", "Robbin Van Persie/Robbie Keane"],
        "What is the real name of the legendary MLB player 'Babe Ruth'?": ["George Herman Ruth", "Babe Hitman Ruth", "Babe George Ruth", "George Henry Ruth"],
        "How long do Cricket games usually last?": ["3-5 days", "2-3 hours", "A week", "30 minutes"],
        "Who owns the most majors in Golf history?": ["Jack Nicklaus", "Tiger Woods", "Rory McIlroy", "Phil Mickelson"],
        "Who owns the most Grand Slams in Tennis history between men and women?": ["Margaret Court", "Serena Williams", "Maria Sharapova", "Venus Williams"],
        "What's the fastest recorded pitch in MLB history?": ["108.1 MPH", "105.2 MPH", "110.8 MPH", "106.5 MPH"],
        "What is the most watched sports event of all-time?": ["The 2008 Beijing Olympics", "1994 FIFA World Cup", "Super Bowl XIV", "Tour De France 2022"],
        "Which of the 4 major US sports came first?": ["MLB", "NBA", "NFL", "MLS"],
        "What is the oldest sport in the world?": ["Running", "Cricket", "Wrestling", "Archery"],
        "How many NHL records does Wayne Gretzky hold?": ["61", "34", "23", "100"],
        "What was Tom Brady's 40 time in 2000?": ["5.28", "4.86", "6.12", "5.82"]
    }   
    return kc_questions

def get_answer(kcquestion, kcalternatives):
    """Creating the quiz format with the question, and then the multiple choice answers
    Parameters: kcquestion= the questions
                kcalternatives= the multiple choice answers
    Return: kclabeled_alternatives[kcanswer_label]= the user's answer
    """
    print(f"{kcquestion}")
    kclabeled_alternatives= dict(zip(ascii_lowercase, sorted(kcalternatives)))
    for kclabel, kcalternative in kclabeled_alternatives.items():
        print(f" {kclabel}) {kcalternative} ")
    #If user enters an invalid answer, keep the loop going
    while (kcanswer_label := input("\nChoice? ")) not in kclabeled_alternatives:
        print(f"Please answer one of {', '.join(kclabeled_alternatives)}")
    return kclabeled_alternatives[kcanswer_label]

def loop_through_quiz(kclist):
    """
    Loop through the questions, asking the user for their answer, 
    and making a list of their answers. 
    Parameters: kclist= the list of questions with their possible answers
    Return: kcanswers_list= A list of the user's correct answers
    """
    kcanswers_list= []
    #looping through the dictionary
    for kcnum, (kcquestion, kcalternatives) in enumerate(kclist.items(), start=1):
        print(f"\nQuestion {kcnum}:")
        kccorrect_answer=kcalternatives[0]
        kcanswer= get_answer(kcquestion, kcalternatives)
        #if the user is correct, tell them and add the answer to the list to help count correct answers
        if kcanswer== kccorrect_answer:
            print(f"Correct!")
            kcanswers_list.append(kcanswer)
        else:
            print(f"The answer is {kccorrect_answer!r} Not {kcanswer!r}")
    return kcanswers_list
        

def print_outro(kcscore):
    """Print the outro with the user's sports fandom level shown.
    Parameters: kcscore-Number of correct answers from the user.
    Return: nothing
    """
    print()
    print(f"Your sports fandom level is:")
    if (kcscore <= 2):
        print(f"Michael Jordan Fan Club- When you only know famous sports players because of word of mouth.")
    elif (kcscore >=3) and (kcscore <=6):
        print(f"College fanboy- You're into college sports because of the vibe, that's it.")
    elif (kcscore >=7) and (kcscore <=9):
        print(f"Linsanity's VIP- Hey this is a start, you're in tune enough to be aware of one hit wonders.")
    elif (kcscore >=10) and (kcscore <=12):
        print(f"Matt Forte's punching bag-Is my Chicago bias showing? You're at least not a beginner when it comes to sports.")
    elif (kcscore >=13) and (kcscore <=14):
        print(f"Andres Iniesta's boy club-You must not be American since you care about more than Basketball and Football.")
    elif (kcscore >=15) and (kcscore <=16):
        print(f"Serena Williams' the GOAT club-You're a true sports fan, you gulf up all sports knowledge, with no respect of persons/gender.")
    elif (kcscore >=17) and (kcscore <=19):
        print(f"The Cricket heard around the world- You're approaching GOAT sports fan territory, I don't even really know Cricket.")
    elif (kcscore >=20) and (kcscore <=21):
        print(f"TOM BRADY Forever- I don't even know what to say except you are the GOAT.")
    
#Prevents main from running when a separate test function is being run.
if __name__=="__main__":
    main()
