import argparse
import time

from sjsolver.grid_gen import generate_grid
from sjsolver.solver import search_all_words
from sjsolver.utilities import get_words


def main(h, w, chars):
    grid1 = list(chars)

    print("Provided grid:")
    for y in range(h):
        for x in range(w):
            print(grid1[w*y + x]+ " ", end="")
        print("\n", end="")

    nodes = generate_grid(w, h , grid1)
    print(f"{w} x {h} with {len(nodes)*len(nodes[0])} nodes")

    words = get_words()
    words = words[words.str.len() <= h * w]

    found_words = set()

    start_time = time.time()
    search_all_words(nodes, found_words, words)
    end_time = time.time()

    print(f"Found {len(found_words)} words!")

    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.4f} seconds")

    score = 0

    for word in found_words:
        score += len(word)**1.5
    print(f"Score: {score:.1f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--chars", default="huytresavnmkjilopuytr")
    parser.add_argument("--height", default=4)
    parser.add_argument("--width", default=4)

    args = parser.parse_args()
    try:
        w = int(args.width)
        h = int(args.height)
    except Exception as e:
        raise AssertionError(f"{e!s}")
    
    c = args.chars

    assert len(c) == h*w, f"Number of characters ({len(c)}) should equal to product of height ({h}) and width ({w})" 

    main(h, w, c)