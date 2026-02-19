"""Exercise classes for the workout tracker."""

from datetime import datetime


class Exercise:
    """Base class for all exercise types.
    
    Attributes:
        name (str): The name of the exercise
        date (str): The date the exercise was performed (YYYY-MM-DD format)
    """
    
    def __init__(self, name: str, date: str = None):
        """Initialize an Exercise.
        
        Args:
            name: The name of the exercise
            date: The date performed (defaults to today if not provided)
        """
        self.name = name
        if date is None:
            self.date = datetime.now().strftime("%Y-%m-%d")
        else:
            self.date = date
    
    def calculate_calories(self) -> float:
        """Calculate calories burned for this exercise.
        
        Subclasses must override this method.
        
        Returns:
            float: Estimated calories burned
        """
        # This is a base implementation that subclasses will override
        return 0.0
    
    def get_duration(self) -> float:
        """Get the duration of the exercise in minutes.
        
        Subclasses must override this method.
        
        Returns:
            float: Duration in minutes
        """
        # This is a base implementation that subclasses will override
        return 0.0
    
    def __str__(self) -> str:
        """Return a string representation of the exercise."""
        # Use self.calculate_calories() to get the calories
        return f"{self.name}: {self.calculate_calories:,.0f} calories"


class CardioExercise(Exercise):
    """Cardio exercise with distance and time tracking.
    
    Attributes:
        name (str): Exercise name
        date (str): Date performed
        distance (float): Distance covered in miles
        duration (float): Time spent in minutes
    """
    
    def __init__(self, name: str, distance: float, duration: float, date: str = None):
        """Initialize a CardioExercise.
        
        Args:
            name: Exercise name (e.g., "Running", "Cycling")
            distance: Distance covered in miles
            duration: Time spent in minutes
            date: Date performed (optional)
        """
        super().__init__(name, date)
        self.distance = distance
        self.duration = duration
    
    def calculate_calories(self) -> float:
        """Calculate calories burned based on distance.
        
        Formula: distance * 100
        
        Returns:
            float: Estimated calories burned
        """
        return self.distance * 100.0
    
    def get_duration(self) -> float:
        """Get the duration of the cardio exercise.
        
        Returns:
            float: Duration in minutes
        """
        return self.duration
    
    def __str__(self) -> str:
        """Return detailed string representation."""
        # Include self.name, self.distance, self.duration, and self.calculate_calories()
        return f"{self.name} ({self.distance:.1f} miles, {self.duration:.0f} min): {self.calculate_calories():,.0f} calories"

class StrengthExercise(Exercise):
    """
    Additional Attributes:

    weight (float) - Pounds lifted
    reps (int) - Repetitions per set
    sets (int) - Number of sets
    Constructor:

    Method signature: def __init__(self, name: str, weight: float, reps: int, sets: int, date: str = None):
    Call parent constructor
    Store weight, reps, and sets
    Override These Methods:

    calculate_calories()
    Formula: weight * reps * sets * 0.05

    get_duration()
    Formula: sets * 3 (assumes 3 min per set including rest)

    __str__()

    Format: "Bench Press (135 lbs x 10 reps x 3 sets): 202 calories"
    Include name, weight, reps, sets, and calculated calories
    """

    def __init__(self, name: str, weight: float, reps: int, sets: int, date: str = None):
        super().__init__(name, date)
        self.weight = weight
        self.reps = reps
        self.sets = sets
        
    def calculate_calories(self):
        return self.weight * self.reps * self.sets * 0.05
    
    def get_duration(self):
        return self.sets * 3

    def __str__(self):
        return f"{self.name} ({self.weight} lbs x {self.reps} reps x {self.sets} sets): {self.calculate_calories():,.0f} calories"