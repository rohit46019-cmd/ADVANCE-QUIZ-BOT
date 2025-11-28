def parse_config_callback(data: str):
    if data.startswith("lang_"):
        return ("language", {"en":"English","hi":"Hindi","bi":"Bilingual"}[data.split("_")[1]])
    if data.startswith("diff_"):
        return ("difficulty", {"easy":"Easy","mod":"Moderate","hard":"Hard","mhard":"Most Hard"}[data.split("_")[1]])
    if data.startswith("timer_"):
        return ("timer", int(data.split("_")[1]))
    if data.startswith("shuffle_"):
        return ("shuffle", data.endswith("yes"))
    if data.startswith("neg_"):
        return ("negative_marking", 0.25 if data.endswith("on") else 0.0)
    return ("unknown", None)
