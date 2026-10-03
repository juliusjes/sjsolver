import pandas as pd


def find_words(node, current_word, path, visited, found_words:set, words: pd.DataFrame):
    '''
    Find words using dfs
    '''
    current_word += node.char

    if current_word.lower() in words.str.lower().values:
        if current_word not in found_words:
            print(current_word)
        found_words.add(current_word)
        return

    if words[words.str.startswith(current_word)].empty: # pruning
        return

    # mark the current node as visited
    visited.add(node)
    path.append(node.pos)

    # search in all available neighbors
    for neighbor in [node.n, node.nw, node.ne, node.e, node.s, node.sw, node.se, node.w]:
        if neighbor and neighbor not in visited:
            find_words(neighbor, current_word, path, visited, found_words, words)

    # remove the node from path and unmark it as visited
    visited.remove(node)
    path.pop()

def search_all_words(grid, found_words, words):
    visited = set()
    path = []
    for row in grid:
        for node in row:
            find_words(node, "", path, visited, found_words, words)
