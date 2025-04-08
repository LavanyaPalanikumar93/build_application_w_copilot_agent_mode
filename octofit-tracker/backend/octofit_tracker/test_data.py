# Test data for the OctoFit Tracker application

test_users = [
    {"id": "1", "email": "student1@example.com", "name": "Student One"},
    {"id": "2", "email": "student2@example.com", "name": "Student Two"},
]

test_teams = [
    {"id": "1", "name": "Team Alpha", "members": ["1", "2"]},
]

test_activities = [
    {"id": "1", "user_id": "1", "type": "Running", "duration": 30, "date": "2025-04-07"},
    {"id": "2", "user_id": "2", "type": "Cycling", "duration": 45, "date": "2025-04-07"},
]

test_leaderboard = [
    {"id": "1", "team_id": "1", "points": 100},
]

test_workouts = [
    {"id": "1", "name": "Push-ups", "description": "Do 20 push-ups"},
    {"id": "2", "name": "Sit-ups", "description": "Do 30 sit-ups"},
]
