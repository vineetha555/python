# Reverse Dictionary mapping

ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}

rev_dict=dict(reversed(list(ascii_dict.items())))
print(rev_dict)