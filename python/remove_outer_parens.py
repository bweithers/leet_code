def removeOuterParentheses(self, s: str):
    counter = 0
    idx = []

    for i,c in enumerate(s):
        if not counter: idx.append(i)
        counter += c=='('
        counter -= c==')'
        if not counter: idx.append(i)

    s = list(s)
    for i in range(len(idx)): s.pop(idx[i]-i)
    return ''.join(s)
