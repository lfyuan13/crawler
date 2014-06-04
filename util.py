
def to_unicode(sent):
    if isinstance(sent, str):
        return sent.decode('utf-8')
    if isinstance(sent, list):
        for idx, item in enumerate(sent):
            sent[idx] = to_unicode(item)
        return sent
    if isinstance(sent, dict):
        for k in sent:
            sent[k] = to_unicode(sent[k])
        return sent
