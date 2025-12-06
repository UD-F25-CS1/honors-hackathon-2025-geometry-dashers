"""
=============================================================================================
IMPORTS
=============================================================================================
"""



from bakery import assert_equal
from drafter import *
from dataclasses import dataclass
#from meta import *



"""
=============================================================================================
SITE METADATA
=============================================================================================
"""



hide_debug_information()
#set_website_framed(False)
set_website_title("Tung Tung Computer Science Trivia")
set_site_information(
    "Francis Mailom & Zayn Richardson",
"""
This is a jeopordy like trivia game hosted by TUNG TUNG TUNG SAHUR!
""",
    [],
    [],
    [],
)



"""
=============================================================================================
DATACLASSES
=============================================================================================
"""



@dataclass
class Player:
    name: str
    score: int


@dataclass
class State:
    player1: Player
    player2: Player
    player3: Player
    player4: Player
    points_won: int
   
   
   
"""
=============================================================================================
HELPER FUNCTIONS
=============================================================================================
"""



def get_active_players(state: State):
    return [p.name for p in [state.player1, state.player2, state.player3, state.player4] if p.name]



"""
=============================================================================================
ROUTES
=============================================================================================
"""



@route
def index(state: State) -> Page:
    return Page(state, ['''<audio controls autoplay>
          <source src="introduction.ogg" type="audio/ogg">
          <source src="introduction.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
        </audio>''', bold("Welcome to Tung Tung Computer Science Trivia!"),
                        "how many players are there?",
                        Image("standingtungforquestions.png", 400,400),
                        Button("2 Players", select2players),
                        Button("3 Players", select3players),
                        Button("4 Players", select4players)
                        ])


@route
def select2players(state: State, p1_name = "", p2_name = "") -> Page: 
    return Page(state, [
                        "Contestants, please enter your names.",
                        "Player 1",
                        TextBox("p1_name"),
                        "Player 2",
                        TextBox("p2_name"),
                        Button("Enter", main_game_2player, p1_name = p1_name, p2_name = p2_name)
                        ])

    
@route
def select3players(state: State, p1_name = "", p2_name = "", p3_name = "") -> Page: 
    return Page(state, ["Contestants, please enter your names.",
                        "Player 1",
                        TextBox("p1_name"),
                        "Player 2",
                        TextBox("p2_name"),
                        "Player 3",
                        TextBox("p3_name"),
                        Button("Enter", main_game_3player, p1_name = p1_name, p2_name = p2_name, p3_name = p3_name)
                        ])
    
    
@route
def select4players(state: State, p1_name = "", p2_name = "", p3_name = "", p4_name = "") -> Page:    
    return Page(state, ["Contestants, please enter your names.",
                        "Player 1",
                        TextBox("p1_name"),
                        "Player 2",
                        TextBox("p2_name"),
                        "Player 3",
                        TextBox("p3_name"),
                        "Player 4",
                        TextBox("p4_name"),
                        Button("Enter", main_game_4player, p1_name = p1_name, p2_name = p2_name, p3_name = p3_name, p4_name = p4_name)
                        ])


@route
def return_to_game(state: State, who_won: str, show_answer: str) -> Page:
    
    if state.player1.name == who_won:
        state.player1.score += state.points_won
    if state.player2.name == who_won:
        state.player2.score += state.points_won
    if state.player3.name == who_won:
        state.player3.score += state.points_won
    if state.player4.name == who_won:
        state.player4.score += state.points_won
    
    if state.player4.name != "":
        return main_game_4player(state,
                                 state.player1.name,
                                 state.player2.name,
                                 state.player3.name,
                                 state.player4.name)
    
    if state.player3.name != "":
        return main_game_3player(state,
                                 state.player1.name,
                                 state.player2.name,
                                 state.player3.name)
    
    return main_game_2player(state,
                             state.player1.name,
                             state.player2.name)


"""
=============================================================================================
MAIN GAME
=============================================================================================
"""



@route
def main_game_2player(state: State, p1_name: str, p2_name: str) -> Page:
    
    if state.player1.score + state.player2.score >= 7500:
        if state.player1.score > state.player2.score:
            return Page(state, [f"Congratulations, {state.player1.name}! You have won the Tung Tung Computer Science Trivia!"
                ])
        if state.player2.score > state.player1.score:
            return Page(state, [f"Congratulations, {state.player2.name}! You have won the Tung Tung Computer Science Trivia!"
                ])
        
    state.player1.name = p1_name
    state.player2.name = p2_name

    return Page(state, [f"{state.player1.name}: {state.player1.score}",
                        f"{state.player2.name}: {state.player2.score}",
                        
                        Row(
                        "Syntax ", "History ", "Debug ", "Return ", "General "
                        ),
                        
                        Row(
                        Button("100", cat1_100),
                        Button("100", cat2_100),
                        Button("100", cat3_100),
                        Button("100", cat4_100),
                        Button("100", cat5_100)
                        ),
                        
                        Row(
                        Button("200", cat1_200),
                        Button("200", cat2_200),
                        Button("200", cat3_200),
                        Button("200", cat4_200),
                        Button("200", cat5_200)
                        ),
                        
                        Row(
                        Button("300", cat1_300),
                        Button("300", cat2_300),
                        Button("300", cat3_300),
                        Button("300", cat4_300),
                        Button("300", cat5_300)
                        ),
                        
                        Row(
                        Button("400", cat1_400),
                        Button("400", cat2_400),
                        Button("400", cat3_400),
                        Button("400", cat4_400),
                        Button("400", cat5_400)
                        ),
                        
                        Row(
                        Button("500", cat1_500),
                        Button("500", cat2_500),
                        Button("500", cat3_500),
                        Button("500", cat4_500),
                        Button("500", cat5_500)
                        ),
                        ])
                        

@route
def main_game_3player(state: State, p1_name: str, p2_name: str, p3_name: str) -> Page:
    
    # WIN CHECK (same structure as 2 player)
    total = state.player1.score + state.player2.score + state.player3.score
    if total >= 7500:
        # find highest score
        scores = {
            state.player1.name: state.player1.score,
            state.player2.name: state.player2.score,
            state.player3.name: state.player3.score
        }
        winner = max(scores, key=scores.get)
        return Page(state, [f"🎉 Congratulations, {winner}! You have won the Tung Tung Computer Science Trivia!"])
    
    # normal game display
    state.player1.name = p1_name
    state.player2.name = p2_name
    state.player3.name = p3_name
    
    return Page(state, [f"{state.player1.name}: {state.player1.score}",
                        f"{state.player2.name}: {state.player2.score}",
                        f"{state.player3.name}: {state.player3.score}",
                        
                        Row(
                        "Syntax ", "History ", "Debug ", "Return ", "General "
                        ),
                        
                        Row(
                        Button("100", cat1_100),
                        Button("100", cat2_100),
                        Button("100", cat3_100),
                        Button("100", cat4_100),
                        Button("100", cat5_100)
                        ),
                        
                        Row(
                        Button("200", cat1_200),
                        Button("200", cat2_200),
                        Button("200", cat3_200),
                        Button("200", cat4_200),
                        Button("200", cat5_200)
                        ),
                        
                        Row(
                        Button("300", cat1_300),
                        Button("300", cat2_300),
                        Button("300", cat3_300),
                        Button("300", cat4_300),
                        Button("300", cat5_300)
                        ),
                        
                        Row(
                        Button("400", cat1_400),
                        Button("400", cat2_400),
                        Button("400", cat3_400),
                        Button("400", cat4_400),
                        Button("400", cat5_400)
                        ),
                        
                        Row(
                        Button("500", cat1_500),
                        Button("500", cat2_500),
                        Button("500", cat3_500),
                        Button("500", cat4_500),
                        Button("500", cat5_500)
                        ),
                        ])


@route
def main_game_4player(state: State, p1_name: str, p2_name: str, p3_name: str, p4_name: str) -> Page:
    
    # WIN CHECK
    total = state.player1.score + state.player2.score + state.player3.score + state.player4.score
    if total >= 7500:
        scores = {
            state.player1.name: state.player1.score,
            state.player2.name: state.player2.score,
            state.player3.name: state.player3.score,
            state.player4.name: state.player4.score
        }
        winner = max(scores, key=scores.get)
        return Page(state, [f"🎉 Congratulations, {winner}! You have won the Tung Tung Computer Science Trivia!"])
    
    # normal game display
    state.player1.name = p1_name
    state.player2.name = p2_name
    state.player3.name = p3_name
    state.player4.name = p4_name
    
    return Page(state, [f"{state.player1.name}: {state.player1.score}",
                        f"{state.player2.name}: {state.player2.score}",
                        f"{state.player3.name}: {state.player3.score}",
                        f"{state.player4.name}: {state.player4.score}",
                        Row(
                        "Syntax ", "History ", "Debug ", "Return ", "General "
                        ),
                        
                        Row(
                        Button("100", cat1_100),
                        Button("100", cat2_100),
                        Button("100", cat3_100),
                        Button("100", cat4_100),
                        Button("100", cat5_100)
                        ),
                        
                        Row(
                        Button("200", cat1_200),
                        Button("200", cat2_200),
                        Button("200", cat3_200),
                        Button("200", cat4_200),
                        Button("200", cat5_200)
                        ),
                        
                        Row(
                        Button("300", cat1_300),
                        Button("300", cat2_300),
                        Button("300", cat3_300),
                        Button("300", cat4_300),
                        Button("300", cat5_300)
                        ),
                        
                        Row(
                        Button("400", cat1_400),
                        Button("400", cat2_400),
                        Button("400", cat3_400),
                        Button("400", cat4_400),
                        Button("400", cat5_400)
                        ),
                        
                        Row(
                        Button("500", cat1_500),
                        Button("500", cat2_500),
                        Button("500", cat3_500),
                        Button("500", cat4_500),
                        Button("500", cat5_500)
                        ),
                        ])



"""
=============================================================================================
QUESTIONS
=============================================================================================
"""



#100=============================================================================================
@route
def cat1_100(state: State) -> Page:
    state.points_won = 100
    return Page(state, ["Question here!",
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat2_100(state: State) -> Page:
    state.points_won = 100
    return Page(state, ['''<audio controls autoplay>
          <source src="history100.ogg" type="audio/ogg">
          <source src="history100.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
        </audio>''', "What programming language is named after a coffee?",
                        SelectBox("show_answer", ["Show answer!", "Java"]),
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat3_100(state: State) -> Page:
    state.points_won = 100
    return Page(state, ["Question here!",
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat4_100(state: State) -> Page:
    state.points_won = 100
    return Page(state, ["Question here!",
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat5_100(state: State) -> Page:
    state.points_won = 100
    return Page(state, ['''<audio controls autoplay>
          <source src="gen_knowledge100.ogg" type="audio/ogg">
          <source src="gen_knowledge100.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
        </audio>''', "How many megabytes are in a gigabyte?",
                        SelectBox("show_answer", ["Show answer!", "1000"]),
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
#200=============================================================================================
@route
def cat1_200(state: State) -> Page:
    state.points_won = 200
    return Page(state, ["Question here!",
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat2_200(state: State) -> Page:
    state.points_won = 200
    return Page(state, ['''<audio controls autoplay>
          <source src="history200.ogg" type="audio/ogg">
          <source src="history200.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
        </audio>''', "Who made python?",
                        SelectBox("show_answer", ["Show answer!", "Guido van Rossum"]),
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat3_200(state: State) -> Page:
    state.points_won = 200
    return Page(state, ["Question here!",
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat4_200(state: State) -> Page:
    state.points_won = 200
    return Page(state, ["Question here!",
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat5_200(state: State) -> Page:
    state.points_won = 200
    return Page(state, ["What software dev. company has an octocat for the logo?",
                        SelectBox("show_answer", ["Show answer!", "GitHub"]),
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
#300=============================================================================================
@route
def cat1_300(state: State) -> Page:
    state.points_won = 300
    return Page(state, ["Question here!",
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat2_300(state: State) -> Page:
    state.points_won = 300
    return Page(state, ['''<audio controls autoplay>
          <source src="history300.ogg" type="audio/ogg">
          <source src="history300.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
        </audio>''', "What show inspired pythons name?",
                        SelectBox("show_answer", ["Show answer!", "Monty Python's Flying Circus"]),
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat3_300(state: State) -> Page:
    state.points_won = 300
    return Page(state, ["Question here!",
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat4_300(state: State) -> Page:
    state.points_won = 300
    return Page(state, ["Question here!",
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat5_300(state: State) -> Page:
    state.points_won = 300
    return Page(state, ["What does HTTP stand for?",
                        SelectBox("show_answer", ["Show answer!", "Hypertexy Transfer Protocol"]),
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
#400=============================================================================================
@route
def cat1_400(state: State) -> Page:
    state.points_won = 400
    return Page(state, ["Question here!",
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat2_400(state: State) -> Page:
    state.points_won = 400
    return Page(state, ['''<audio controls autoplay>
          <source src="history400.ogg" type="audio/ogg">
          <source src="history400.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
        </audio>''', "Who made binary?",
                        SelectBox("show_answer", ["Show answer!", "Gottfried Wilhelm Leibniz"]),
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat3_400(state: State) -> Page:
    state.points_won = 400
    return Page(state, ["Question here!",
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat4_400(state: State) -> Page:
    state.points_won = 400
    return Page(state, ["Question here!",
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat5_400(state: State) -> Page:
    state.points_won = 400
    return Page(state, ["What does URL stand for?",
                        SelectBox("show_answer", ["Show answer!", "Uniform Resource Locator"]),
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
#500=============================================================================================
@route
def cat1_500(state: State) -> Page:
    state.points_won = 500
    return Page(state, ["Question here!",
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat2_500(state: State) -> Page:
    state.points_won = 500
    return Page(state, ['''<audio controls autoplay>
          <source src="history500.ogg" type="audio/ogg">
          <source src="history500.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
        </audio>''', "What was the first electronic computer called?",
                        SelectBox("show_answer", ["Show answer!", "ENIAC/Atenaoff-Berry"]),
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat3_500(state: State) -> Page:
    state.points_won = 500
    return Page(state, ["Question here!",
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat4_500(state: State) -> Page:
    state.points_won = 500
    return Page(state, ["Question here!",
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])
@route
def cat5_500(state: State) -> Page:
    state.points_won = 500
    return Page(state, ["What famous sandbox game is Java based?",
                        SelectBox("show_answer", ["Minecraft"]),
                        SelectBox("who_won", get_active_players(state), "Who won?"),
                        Button("Back", return_to_game)
                    ])



"""
=============================================================================================
START SERVER
=============================================================================================
"""



start_server(State(Player("", 2000), Player("", 0), Player("", 0), Player("", 0), 0))
