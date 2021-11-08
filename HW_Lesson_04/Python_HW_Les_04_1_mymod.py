def salary(hours, bonus):
    rusult = hours * 3000
    if bonus == "да":
        rusult += 15000
    return rusult
