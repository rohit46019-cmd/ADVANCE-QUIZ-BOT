import json, os

DATA_SAVED = "data/saved_questions.json"
DATA_STORED = "data/stored_quizzes.json"

class Storage:
    @staticmethod
    def _load(path):
        if not os.path.exists(path): return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def _dump(path, data):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @staticmethod
    def save_question(user_id, qdict):
        data = Storage._load(DATA_SAVED)
        uid = str(user_id)
        data.setdefault(uid, [])
        data[uid].append(qdict)
        Storage._dump(DATA_SAVED, data)

    @staticmethod
    def get_saved(user_id):
        data = Storage._load(DATA_SAVED)
        return data.get(str(user_id), [])

    @staticmethod
    def store_quiz_summary(user_id, session):
        data = Storage._load(DATA_STORED)
        uid = str(user_id)
        data.setdefault(uid, [])
        summary = {
            "mode": session.mode,
            "total": session.total,
            "stats": session.stats,
            "config": session.config,
            "time": session.elapsed_time()
        }
        data[uid].append(summary)
        Storage._dump(DATA_STORED, data)

    @staticmethod
    def get_stored_quizzes():
        data = Storage._load(DATA_STORED)
        return data
