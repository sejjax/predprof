from data import NAME, PREP, DATE, COMP, preps, allo_fakers, allo_origin

# Читаем данные из файла
with open("scientist_origin.txt", 'w', encoding='utf-8') as f:
    f.write("ScientistName#preparation#date#components\n")
    f.write(
        "\n".join(map(lambda r: f"{r[NAME]}#{r[PREP]}#{str(r[DATE])}#{' '.join(r[COMP])}", preps))
    )
s = f"""Разработчиками Аллопуринола были такие люди\n"""
s += "\n".join(map(lambda r: f"{r[NAME]} - {r[DATE]}", allo_fakers))
s += f"\nОригинальный рецепт принадлежит: {allo_origin[NAME]}”"

# Создаем отчет полиции
with open("police_report.txt", 'w', encoding='utf-8') as f:
    f.write(s)
print(s)
