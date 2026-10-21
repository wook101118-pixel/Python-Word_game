userName = input("당신의 이름을 알고 싶습니다. 이름을 입력해주세요: ")
print(f"반갑습니다, {userName}님! 반려동물 이야기를 만들어 볼까요?")

animal = input("반려동물을 입력하세요: ")
name = input("반려동물의 이름을 입력하세요: ")
if (name[-1] == ('이' or '고')):
    name = name[:-1]

adjective1 = input("형용사를 입력하세요(00(이)고): ")
if (adjective1[-1] == ('이' or '고')):
    adjective1 = adjective1[:-1]

color1 = input("색깔을 입력하세요(00색): ")
if (color1[-1] == ('색')):
    color1 = color1[:-1]

adjective2 = input("형용사를 입력하세요(000합니다): ")
if (adjective2[-3] == ('합') and adjective2[-2] == ('니') and adjective2[-1] == ('다')):
    adjective2 = adjective2[:-3]

noun1 = input("명사를 입력하세요: ")
noun2 = input("명사를 입력하세요: ")
noun3 = input("명사를 입력하세요: ")
adjective3 = input("형용사를 입력하세요(00은): ")
if (adjective3[-1] == ('은')):
    adjective3 = adjective3[:-1]

color2 = input("색깔을 입력하세요(00색): ")
if (color2[-1] == ('색')):
    color2 = color2[:-1]

noun4 = input("명사를 입력하세요: ")


print("다음은 여러분이 만든 이야기입니다.")
print()
print(f"저의 반려동물은 {animal}이며 이름은 {name}입니다.")
print(f"{adjective1}(이)고 {color1}색이며 {adjective2}합니다.")
print(f"{name}는 {noun1}, {noun2}, {noun3}을(를) 먹습니다.")
print(f"가장 좋아하는 장난감은 {adjective3}은 {color2}색 {noun4}입니다.")