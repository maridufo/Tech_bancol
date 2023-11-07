from fuzzywuzzy import fuzz

s1 = "calle 53 # 55 a 67"
s2 = "calle 53 Nro 55 a 67"


def run():
    similarity = fuzz.ratio(s1, s2)
    print(f"Similarity percentage: {similarity}%")


if __name__ == "__main__":
    run()
