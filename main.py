
# 1) Принять у пользователя строку и вывести
# - Количество символов 
# - Количество цифр
# - Количество чисел
# - Количество букв 
# - Количество букв в верхнем регистре
# - Количество букв в нижнем регистре
# - Количество пробелов
# После чего заменить все пробелы на символ '-' и пересохранить строку
# Далее вывести каждое слово отдельно и вывести количество таковых слов


# txt = input("Enter data -> ")

# if len(txt) > 0:
#     amount_dig = 0
#     amount_nums = 0
#     amount_upper = 0
#     amount_alpha = 0
#     amount_lower = 0
#     amount_spacing = 0

#     for i in txt:
#         amount_dig += i.isdigit()
#         amount_nums += i.isnumeric()
#         amount_alpha += i.isalpha()
#         amount_upper += i.isupper()
#         amount_lower += i.islower()
#         amount_spacing += i.isspace()

  # print("length of txt",len(txt))
  # print("amount of digits", amount_dig)
  # print("amount of nums",amount_nums)
  # print("amount of letters", amount_alpha)
  # print("amount of uppercased letters",amount_upper)
  # print("amount of lowercased letters",amount_lower)
  # print("amount of spacing",amount_spacing)

  # replaced_txt = txt.replace(' ','-')
  # print("Words separated with - symbol between each other -> ", replaced_txt)
  # words = replaced_txt.split('-')
  # print("Words -> ", end=" ")
  # if len(words) > 0:
        # for i  in words:
        #     if i != len(words)-1:
        #      print(i, end=", ")
        #     else:
        #         print(i)
    #     print(len(words), "words.")
    # else:
    #     print("Length of words is 0")



import turtle

screen = turtle.Screen()
screen.title("Text Analyzer")

def analyze_txt(txt):
    # txt = input("Enter data -> ")

    if len(txt) > 0:
        amount_dig = 0
        amount_nums = 0
        amount_upper = 0
        amount_alpha = 0
        amount_lower = 0
        amount_spacing = 0

        for i in txt:
            amount_dig += i.isdigit()
            amount_nums += i.isnumeric()
            amount_alpha += i.isalpha()
            amount_upper += i.isupper()
            amount_lower += i.islower()
            amount_spacing += i.isspace()

    turtle.clear()

    turtle.penup()
    turtle.goto(-200, 250)
    turtle.pendown()
    turtle.color("red")
    turtle.write("Length of txt: " + str(len(txt)), align="left", font=("Arial", 16, "normal"))
    turtle.penup()
    turtle.goto(-200, 200)
    turtle.pendown()
    turtle.color("orange")
    turtle.write("Amount of digits: " + str(amount_dig), align="left", font=("Arial", 16, "normal"))
    turtle.penup()
    turtle.goto(-200, 150)
    turtle.pendown()
    turtle.color("yellow")
    turtle.write("Amount of nums: " + str(amount_nums), align="left", font=("Arial", 16, "normal"))
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.color("green")
    turtle.write("Amount of letters: " + str(amount_alpha), align="left", font=("Arial", 16, "normal"))
    turtle.penup()
    turtle.goto(-200, 50)
    turtle.pendown()
    turtle.color("blue")
    turtle.write("Amount of uppercased letters: " + str(amount_upper), align="left", font=("Arial", 16, "normal"))
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    turtle.color("purple")
    turtle.write("Amount of lowercased letters: " + str(amount_lower), align="left", font=("Arial", 16, "normal"))
    turtle.penup()
    turtle.goto(-200, -50)
    turtle.pendown()
    turtle.color("pink")
    turtle.write("Amount of spacing: " + str(amount_spacing), align="left", font=("Arial", 16, "normal"))

    turtle.penup()
    turtle.goto(-200, -100)
    turtle.pendown()
    replaced_txt = txt.replace(' ', '-')
    turtle.color("black")
    turtle.write("Words separated with - symbol between each other:", align="left", font=("Arial", 16, "normal"))
    turtle.penup()
    turtle.goto(-200, -150)
    turtle.pendown()
    turtle.color("green")
    turtle.write(replaced_txt, align="left", font=("Arial", 16, "normal"))

    words = replaced_txt.split('-')
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.pendown()
    turtle.color("black")
    turtle.write("Words:", align="left", font=("Arial", 16, "normal"))
    turtle.penup()
    turtle.goto(-200, -250)
    turtle.pendown()
    turtle.color("orange")
    turtle.write(", ".join(words) + ". Amount of words -> " + str(len(words)), align="left",
                 font=("Arial", 16, "normal"), move=True)


def get_user_input():
    turtle.penup()
    turtle.goto(-50,-450)
    turtle.pendown()
    txt = turtle.textinput("Text Analyzer", "Enter data -> ")

    analyze_txt(txt)

turtle.setup(width=800, height=800)
get_user_input()
turtle.done()
turtle.mainloop()



