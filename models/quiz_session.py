import time
from models.storage import Storage

class QuizSession:
    def __init__(self, user_id, mode="ai"):
        self.user_id = user_id
        self.mode = mode
        self.active = True
        self.questions = []
        self.index = 0
        self.total = 0
        self.stats = {"attempted":0,"correct":0,"wrong":0,"skipped":0,"saved":0}
        self.config = {"language":"English","difficulty":"Moderate","timer":15,"shuffle":True,"negative_marking":0.0}
        self.prompt = ""
        self.state = "idle"
        self.start_time = time.time()

    def load_questions(self, qlist):
        import random
        self.questions = qlist[:]
        if self.config.get("shuffle", True):
            random.shuffle(self.questions)
        self.total = len(self.questions)
        self.index = 0

    def current_question(self):
        return self.questions[self.index]

    def next(self):
        if self.index + 1 < len(self.questions):
            self.index += 1
            return True
        return False

    def elapsed_time(self) -> float:
        return time.time() - self.start_time

    def is_config_ready(self) -> bool:
        return all(k in self.config for k in ["language","difficulty","timer","shuffle","negative_marking"])

class SessionManager:
    _sessions = {}

    @classmethod
    def ensure_user(cls, user_id):
        cls._sessions.setdefault(user_id, None)

    @classmethod
    def start(cls, user_id, mode="ai") -> QuizSession:
        s = QuizSession(user_id, mode)
        cls._sessions[user_id] = s
        return s

    @classmethod
    def get(cls, user_id):
        return cls._sessions.get(user_id)

    @classmethod
    def has_active(cls, user_id) -> bool:
        s = cls.get(user_id)
        return bool(s and s.active)

    @classmethod
    def end(cls, user_id):
        s = cls.get(user_id)
        if s:
            s.active = False
            Storage.store_quiz_summary(user_id, s)

    @classmethod
    def save_current(cls, user_id):
        s = cls.get(user_id)
        if s and s.questions:
            Storage.save_question(user_id, s.current_question().to_dict())
