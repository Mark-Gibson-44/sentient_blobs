player = dict(
    base_radius=15,
    food_detection = 10,
    player_detection = 10,
    base_speed = 3,
    min_speed = 0.6,
    eat_player_threshold = 0.10, # Dictates how much bigger a player must be to eat another player
    score_reduction = 0.002, # Dictates how much of the player's score is reduced every frame
    score_consumption = 0.45, # Dictates what percentage of the other players score this player absorbs when eating them
)

food = dict(
    value=1
)

game = dict(
    padding = 50,
    fps = 30,
    num_food = 250,
    max_score = 1000,
    frame_limit = 600
)

neat = dict(
    max_score = 1000,
    max_gen = 100,
)