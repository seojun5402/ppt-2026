def get_bmi(weight:float, height:float) -> float:
    bmi = weight / (height ** 2)
    return bmi

def test_get_bmi() :
    weight = 84
    height = 1.81

    b = get_bmi(weight, height)
    print(f"키({weight}) 몸무게({height})의 bmi는 {b}입니다")

    if __name__ == "__main__":
        test_get_bmi()