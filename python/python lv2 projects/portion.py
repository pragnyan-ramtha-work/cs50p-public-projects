class Subjects:

    def __init__(self,chapter,list_of_topics,no_of_questions_asked):
        self.chapter = chapter
        self.list_of_topics = list_of_topics
        self.no_of_questions_asked = no_of_questions_asked
        self.level = []




    def show_chapter_info(self):
           print(f"{self.chapter} has")
           for topic in range(len(self.list_of_topics)):
                print(f"{topic + 1}){self.list_of_topics[topic]}")
                level = input(f"how much do u know {self.list_of_topics[topic]} ? " )


syllabus1 = Subjects("UNIT 1: SETS, RELATIONS AND FUNCTIONS",["Sets and their representation", "Union", "Intersection", "Complement of sets", "Types of relations", "Functions"],1)           

syllabus1.show_chapter_info()


    
#subject = chaptername,no of questions
math = {
    "UNIT 1: SETS, RELATIONS AND FUNCTIONS": {
        "topics": ["Sets and their representation", "Union", "Intersection", "Complement of sets", "Types of relations", "Functions"],
        "number of questions": 1
    },
    "UNIT 2: COMPLEX NUMBERS AND QUADRATIC EQUATIONS": {
        "topics": ["Complex numbers in Cartesian and polar form", "Properties of complex numbers", "Quadratic equations and their solutions"],
        "number of questions": 2
    },
    "UNIT 3: MATRICES AND DETERMINANTS": {
        "topics": ["Types of matrices", "Matrix operations", "Determinants and their properties", "Solving linear equations using matrices"],
        "number of questions": 2
    },
    "UNIT 4: PERMUTATIONS AND COMBINATIONS": {
        "topics": ["Basic counting principles", "Factorial notation", "Permutations", "Combinations"],
        "number of questions": 1
    },
    "UNIT 5: BINOMIAL THEOREM AND ITS SIMPLE APPLICATIONS": {
        "topics": ["Binomial expansion", "Properties of binomial coefficients", "Applications of the binomial theorem"],
        "number of questions": 1
    },
    "UNIT 6: SEQUENCES AND SERIES": {
        "topics": ["Arithmetic progression", "Geometric progression", "Special series"],
        "number of questions": 1
    },
    "UNIT 7: LIMITS, CONTINUITY, AND DIFFERENTIABILITY": {
        "topics": ["Concept of limits", "Continuity of functions", "Differentiability of functions"],
        "number of questions": 3
    },
    "UNIT 8: INTEGRAL CALCULUS": {
        "topics": ["Integration as an inverse of differentiation", "Definite integrals", "Applications of integrals"],
        "number of questions": 3
    },
    "UNIT 9: DIFFERENTIAL EQUATIONS": {
        "topics": ["Formation of differential equations", "Solution of differential equations", "Applications"],
        "number of questions": 1
    },
    "UNIT 10: COORDINATE GEOMETRY": {
        "topics": ["Straight lines", "Circles", "Conic sections (parabola, ellipse, hyperbola)"],
        "number of questions": 3
    },
    "UNIT 11: THREE-DIMENSIONAL GEOMETRY": {
        "topics": ["Planes", "Lines", "Angles between them", "Distances"],
        "number of questions": 2
    },
    "UNIT 12: VECTOR ALGEBRA": {
        "topics": ["Vectors and their operations", "Scalar and vector products"],
        "number of questions": 2
    },
    "UNIT 13: STATISTICS AND PROBABILITY": {
        "topics": ["Measures of central tendency and dispersion", "Probability theorems", "Bayes' theorem", "Probability distributions"],
        "number of questions": 2
    },
    "UNIT 14: TRIGONOMETRY": {
        "topics": ["Trigonometric ratios", "Identities", "Equations", "Inverse functions", "Heights and distances"],
        "number of questions": 1
    },
    "UNIT 15: MATHEMATICAL REASONING": {
        "topics": ["Logical reasoning", "Statements", "Truth tables", "Implications and equivalence"],
        "number of questions": 1
    },
    "UNIT 16: HEIGHTS AND DISTANCES": {
        "topics": ["Applications of trigonometry to measure heights and distances"],
        "number of questions": 1
    }
}

