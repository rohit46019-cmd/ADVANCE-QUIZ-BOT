class Question:
    def __init__(self, serial, text, options, answer, explanation):
        self.serial = serial
        self.text = text
        self.options = options  # {"A": "...", "B": "...", "C": "...", "D": "..."}
        self.answer = answer    # "A"/"B"/"C"/"D"
        self.explanation = explanation

    def to_dict(self):
        return {
            "serial": self.serial,
            "question": f"**{self.text}**",
            "options": self.options,
            "answer": self.answer,
            "explanation": self.explanation
        }
