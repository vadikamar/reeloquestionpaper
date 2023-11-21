import random
import webbrowser
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def question_paper():
    qd= {
    # Physics
    1: ["What is the speed of light?", "Physics", "Waves", "Easy", 5],
    2: ["What is the formula to calculate speed of light?", "Physics", "Waves", "Medium", 5],
    3: ["Explain the photoelectric effect.", "Physics", "Quantum Mechanics", "Hard", 5],
    4: ["Define Newton's first law of motion.", "Physics", "Mechanics", "Easy", 5],
    5: ["What is the equation for force?", "Physics", "Mechanics", "Medium", 5],
    6: ["Explain the concept of gravitational potential energy.", "Physics", "Gravity", "Hard", 5],
    7: ["Describe the Doppler effect.", "Physics", "Waves", "Medium", 5],
    8: ["What is Ohm's Law?", "Physics", "Electricity", "Easy", 5],
    9: ["Explain the concept of magnetic fields.", "Physics", "Magnetism", "Hard", 5],
    10: ["Define nuclear fission and give an example.", "Physics", "Nuclear Physics", "Medium", 5],

    # Math
    11: ["What is the sum of the angles in a triangle?", "Math", "Geometry", "Easy", 5],
    12: ["Solve for x: 2x + 5 = 15", "Math", "Algebra", "Medium", 5],
    13: ["What is the derivative of f(x) = x^2?", "Math", "Calculus", "Hard", 5],
    14: ["Define the Pythagorean Theorem.", "Math", "Geometry", "Easy", 5],
    15: ["Simplify the expression: (3x + 2)(4x - 1)", "Math", "Algebra", "Medium", 5],
    16: ["Evaluate the integral of sin(x) with respect to x.", "Math", "Calculus", "Hard", 5],
    17: ["What is the area of a circle with radius r?", "Math", "Geometry", "Easy", 5],
    18: ["Solve the system of equations: 2x + y = 8, x - y = 2", "Math", "Algebra", "Medium", 5],
    19: ["Find the limit of (x^2 - 1)/(x - 1) as x approaches 1.", "Math", "Calculus", "Hard", 5],
    20: ["What is the definition of a logarithm?", "Math", "Algebra", "Medium", 5],

    # Chemistry
    21: ["What is the chemical symbol for gold?", "Chemistry", "Elements", "Easy", 5],
    22: ["Balance the chemical equation: H2 + O2 → H2O", "Chemistry", "Chemical Reactions", "Medium", 5],
    23: ["Explain the concept of electronegativity.", "Chemistry", "Bonding", "Hard", 5],
    24: ["Define Avogadro's number.", "Chemistry", "Moles", "Easy", 5],
    25: ["What is the structure of a water molecule?", "Chemistry", "Molecular Structure", "Medium", 5],
    26: ["Discuss the difference between exothermic and endothermic reactions.", "Chemistry", "Thermodynamics", "Hard", 5],
    27: ["What is the pH scale?", "Chemistry", "Acids and Bases", "Medium", 5],
    28: ["Name three types of chemical bonds.", "Chemistry", "Bonding", "Easy", 5],
    29: ["Explain the concept of entropy.", "Chemistry", "Thermodynamics", "Hard", 5],
    30: ["What is the difference between a mixture and a compound?", "Chemistry", "Chemical Composition", "Medium", 5],

    # Additional Questions
    31: ["What is the definition of a prime number?", "Math", "Number Theory", "Easy", 5],
    32: ["Define the concept of velocity.", "Physics", "Mechanics", "Medium", 5],
    33: ["What is the Law of Conservation of Energy?", "Physics", "Energy", "Hard", 5],
    34: ["What is the formula for the area of a rectangle?", "Math", "Geometry", "Easy", 5],
    35: ["Explain the concept of isomerism in chemistry.", "Chemistry", "Organic Chemistry", "Hard",5],
    36: ["What is the concept of half-life in radioactive decay?", "Physics", "Nuclear Physics", "Hard", 5],
    37: ["Describe the concept of heat transfer.", "Physics", "Thermodynamics", "Medium", 5],
    38: ["What is the formula for work in physics?", "Physics", "Mechanics", "Medium", 5],
    39: ["Explain the concept of resonance in chemistry.", "Chemistry", "Chemical Bonding", "Medium", 5],
    40: ["What is the definition of a rational number?", "Math", "Number Theory", "Easy", 5],

    # Math
    41: ["Solve for x: log(base 2)(x) = 3", "Math", "Algebra", "Hard", 5],
    42: ["Balance the chemical equation: C4H10 + O2 → CO2 + H2O", "Chemistry", "Chemical Reactions", "Hard", 5],
    43: ["Define the concept of a derivative in calculus.", "Math", "Calculus", "Medium", 5],
    44: ["What is the chemical formula for sulfuric acid?", "Chemistry", "Acids and Bases", "Easy", 5],
    45: ["What is the formula for the volume of a sphere?", "Math", "Geometry", "Medium", 5],

    # Additional Questions
    46: ["What is the concept of gravitational lensing?", "Physics", "Gravity", "Hard", 5],
    47: ["Explain the concept of quantization in physics.", "Physics", "Quantum Mechanics", "Medium", 5],
    48: ["What is the difference between a scalar and a vector quantity?", "Physics", "Motion", "Easy", 5],
    49: ["Explain the concept of oxidation-reduction reactions in chemistry.", "Chemistry", "Redox Reactions", "Medium", 5],
    50: ["What is the definition of a complex number?", "Math", "Complex Numbers", "Hard", 5],
} 

    def generate_question_paper(total_marks, difficulty_distribution):
        questions = []
        for difficulty, percentage in difficulty_distribution.items():
            number_of_questions = int(total_marks * percentage / 100)
            for _ in range(number_of_questions):
                questions.append(random.choice([q for q in qd.values() if q[3] == difficulty]))
        random.shuffle(questions)
        result = [[i[0],i[-2], i[-1]] for i in questions]
        return result

    d={"Easy":20,"Medium":50,"Hard":30}
    t=20
    question_paper = generate_question_paper(t,d)
    return render_template("question_paper.html", questions=question_paper)

if __name__ == "__main__":
    app.run(debug=True)
