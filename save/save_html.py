from resources import dias_da_semana, horarios_manha, horarios_tarde


def gerar_tabela_html_do_cromossomo(cromossomo, caso):
    if caso == 1:
        periodos = [1, 3, 5, 7]
    elif caso == 2:
        periodos = [2, 4, 6, 8]
    else:
        raise ValueError("Caso deve ser 1 ou 2")

    html = ""

    for periodo in periodos:
        html += f"<h2>Período {periodo}</h2>\n"
        html += "<table border='1'>\n<tr><th>Horário</th>"
        for dia in dias_da_semana:
            html += f"<th>{dia}</th>"
        html += "</tr>\n"

        for slot in range(len(horarios_manha + horarios_tarde)):
            horario = horarios_manha[slot] if slot < len(horarios_manha) else horarios_tarde[slot - len(horarios_manha)]
            html += f"<tr><td>{horario}</td>"

            for dia in dias_da_semana:
                aulas = cromossomo[periodo][dia][slot]
                aula_str = "<br>".join(
                    f"{disciplina}<br>{professor}" + (f"<br><b>Lab: {lab_tipo}</b>" if lab_tipo else "")
                    for disciplina, professor, lab_tipo in aulas
                )
                html += f"<td>{aula_str}</td>"

            html += "</tr>\n"

        html += "</table>\n"

    return html
def salvar_html(html, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as file:
        file.write(html)
    print(f"Arquivo '{nome_arquivo}' salvo com sucesso.")
