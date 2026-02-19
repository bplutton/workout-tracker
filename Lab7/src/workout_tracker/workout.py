from typing import List
from workout_tracker.exercises import Exercise


class Workout:
    def __init__(self):
        """Initialize a Workout with an empty list of exercises."""
        self._exercises: List[Exercise] = []

    def add_exercise(self, exercise: Exercise) -> None:
        if not isinstance(exercise, Exercise):
            raise TypeError("Only Exercise objects can be added to a workout")
        else:
            self._exercises.append(exercise)
    
    def get_exercises(self) -> List[Exercise]:
        """Return a copy of the exercises list."""
        return self._exercises.copy()

    def total_calories(self) -> float:
        """Calculate and return the total calories burned in this workout."""
        return sum(exercise.calculate_calories() for exercise in self._exercises)

    def total_duration(self) -> float:
        """Calculate and return the total duration of all exercises in this workout."""
        return sum(exercise.get_duration() for exercise in self._exercises)
    
    def exercise_count(self) -> int:
        """Return the number of exercises in the workout."""
        return len(self._exercises)

    def get_summary(self) -> str:
        """Return a formatted multi-line string summarizing the workout."""
        if not self._exercises:
            return "Empty workout - no exercises added"
        
        lines = ["=== Workout Summary ==="]
        for i, exercise in enumerate(self._exercises, start=1):
            lines.append(f"{i}. {exercise}")
        lines.append("-" * 40)
        total_calories = self.total_calories()
        total_duration = self.total_duration()
        lines.append(f"Total: {total_calories:,.0f} calories, {total_duration:.0f} minutes")
        return "\n".join(lines)

    def __str__(self) -> str:
        return f"Workout with {self.exercise_count()} exercise(s), {self.total_calories():,.0f} calories"
    
    def __len__(self) -> int:
        return self.exercise_count()
    
    """
    Methods to Implement:
    
    get_summary(self) -> str
    Return a formatted multi-line string.

    If workout is empty:

    Return: "Empty workout - no exercises added"
    If workout has exercises, format like this:

    === Workout Summary ===
    1. Running (3.5 miles, 30 min): 350 calories
    2. Bench Press (135 lbs x 10 reps x 3 sets): 202 calories
    ----------------------------------------
    Total: 552 calories, 39 minutes
    Hints:

    Build a list of strings
    Use enumerate() to number the exercises
    Join strings with newlines
    Format numbers with :.0f to avoid decimals
    __str__(self) -> str
    Return a one-line summary:

    Format: "Workout with 2 exercise(s), 552 calories"
    Include exercise count and total calories
    __len__(self) -> int
    Return the number of exercises
    This allows len(workout) to work on your Workout objects
    """