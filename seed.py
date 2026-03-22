from app import app, db  # 1. You MUST import 'app' here
from app import HealthData
from datetime import datetime, timedelta
import random

# 2. Wrap EVERYTHING in this 'with' block
with app.app_context():
    # Clear the database
    db.drop_all()
    db.create_all()

    # Generate dummy data for the past 3 months
    start_date = datetime.now() - timedelta(days=90)
    for i in range(90):
        date = (start_date + timedelta(days=i)).date()
        exercise = random.randint(0, 120)
        meditation = random.randint(0, 60)
        sleep = round(random.uniform(4, 10), 1)
        
        data = HealthData(date=date, exercise=exercise, meditation=meditation, sleep=sleep)
        db.session.add(data)

    db.session.commit()
    print("Database seeded successfully!")