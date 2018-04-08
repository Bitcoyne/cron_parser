cron_expression = "*/15 0 1,15 * 1-5 /usr/bin/find"

seconds_allowed_values = list(range(0, 60))
minutes_allowed_values = list(range(0, 60))
hours_allowed_values = list(range(0, 24))
day_of_month_allowed_values = list(range(1, 32))
month_allowed_values = list(range(0, 12))
day_of_week_allowed_values = list(range(1, 8))


expression_split = cron_expression.split(" ")

look_up = {0: seconds_allowed_values,
           1: minutes_allowed_values,
           2: hours_allowed_values,
           3: day_of_month_allowed_values,
           4: month_allowed_values,
           5: day_of_week_allowed_values}


def is_correct_cron_expression(expression):
    if len(expression) == 6:
        print("TRUE")
    else:
        print("FALSE")


def star(expression_index):
    print(look_up[expression_index])


star(expression_split.index(expression_split[1]))


