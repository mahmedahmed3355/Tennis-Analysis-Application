class MiniCourt:
    def __init__(self, court_length, court_width):
        self.court_length = court_length
        self.court_width = court_width

    def display_dimensions(self):
        return f"Court Length: {self.court_length} meters, Court Width: {self.court_width} meters"

    def is_ball_in_court(self, ball_position):
        x, y = ball_position
        return 0 <= x <= self.court_length and 0 <= y <= self.court_width

    def simulate_ball_movement(self, initial_position, velocity, time):
        x0, y0 = initial_position
        vx, vy = velocity
        x = x0 + vx * time
        y = y0 + vy * time
        return (x, y) if self.is_ball_in_court((x, y)) else None

def main():
    mini_court = MiniCourt(10, 5)
    print(mini_court.display_dimensions())
    ball_position = (3, 2)
    print("Is the ball in court?", mini_court.is_ball_in_court(ball_position))
    new_position = mini_court.simulate_ball_movement((3, 2), (1, 0.5), 2)
    print("New ball position:", new_position)

if __name__ == "__main__":
    main()