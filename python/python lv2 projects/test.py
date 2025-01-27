class Subjects:

    def __init__(self, chapter, no_of_questions_asked):
        self.chapter = chapter
        self.no_of_questions_asked = no_of_questions_asked
        self.chapter_rating = None  # To store rating for the chapter as a whole

    def get_user_ratings(self):
        while True:
            try:
                rating = int(input(f"\nRate your overall understanding of the chapter '{self.chapter}' (1 to 10): "))  # Ask for overall chapter rating
                if 1 <= rating <= 10:  # Make sure the rating is between 1 and 10
                    self.chapter_rating = rating
                    break
                else:
                    print("Please enter a value between 1 and 10.")
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 10.")

    def calculate_expected_score(self):
        if self.chapter_rating is not None:
            expected_score = self.chapter_rating * self.no_of_questions_asked  # Multiply rating by number of questions expected for that chapter
            return expected_score
        else:
            return 0


# Bulk creation of subjects based on JEE syllabus for Mathematics (all 16 chapters)
subjects_data = {
    "UNIT 1: SETS, RELATIONS AND FUNCTIONS": {
        "no_of_questions_asked": 1
    },
    "UNIT 2: COMPLEX NUMBERS AND QUADRATIC EQUATIONS": {
        "no_of_questions_asked": 2
    },
    "UNIT 3: MATRICES AND DETERMINANTS": {
        "no_of_questions_asked": 2
    },
    "UNIT 4: PERMUTATIONS AND COMBINATIONS": {
        "no_of_questions_asked": 1
    },
    "UNIT 5: BINOMIAL THEOREM AND ITS SIMPLE APPLICATIONS": {
        "no_of_questions_asked": 1
    },
    "UNIT 6: SEQUENCES AND SERIES": {
        "no_of_questions_asked": 1
    },
    "UNIT 7: LIMITS, CONTINUITY, AND DIFFERENTIABILITY": {
        "no_of_questions_asked": 3
    },
    "UNIT 8: INTEGRAL CALCULUS": {
        "no_of_questions_asked": 3
    },
    "UNIT 9: DIFFERENTIAL EQUATIONS": {
        "no_of_questions_asked": 1
    },
    "UNIT 10: COORDINATE GEOMETRY": {
        "no_of_questions_asked": 3
    },
    "UNIT 11: THREE-DIMENSIONAL GEOMETRY": {
        "no_of_questions_asked": 2
    },
    "UNIT 12: VECTOR ALGEBRA": {
        "no_of_questions_asked": 2
    },
    "UNIT 13: STATISTICS AND PROBABILITY": {
        "no_of_questions_asked": 2
    },
    "UNIT 14: TRIGONOMETRY": {
        "no_of_questions_asked": 1
    },
    "UNIT 15: MATHEMATICAL REASONING": {
        "no_of_questions_asked": 1
    },
    "UNIT 16: HEIGHTS AND DISTANCES": {
        "no_of_questions_asked": 1
    }
}

# Create the subject objects
subjects = []
for chapter, data in subjects_data.items():
    subject_obj = Subjects(chapter, data["no_of_questions_asked"])
    subjects.append(subject_obj)

# Display information for all subjects and ask for ratings for each chapter
total_score = 0
total_questions = 0

for subject in subjects:
    subject.get_user_ratings()  # User provides rating for each chapter as a whole
    chapter_score = subject.calculate_expected_score()  # Calculates the expected score based on the rating and number of questions
    total_score += chapter_score
    total_questions += subject.no_of_questions_asked * 10  # Total possible score across all chapters

# Calculate the expected number of questions out of 25
expected_questions = (total_score / total_questions) * 25  # Scaling it to 25 questions
expected_questions = round(expected_questions)  # Round off the result

# Display the final expected questions to attempt
print(f"\nYOU CAN EXPECT TO ATTEMPT AROUND {expected_questions} OUT OF 25 QUESTIONS IN THE EXAM.")
print(f"YOU CAN EXPECT AROUND {expected_questions*5 - 35 } - {(expected_questions*4)} MARKS")
