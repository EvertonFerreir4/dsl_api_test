from model import ApiSpec

def slugify(text: str) -> str:
    import re
    text = text.lower()
    text = re.sub(r"[^\w]+", "_", text)
    text = re.sub(r"_+", "_", text)
    return text.strip("_")

def generate_test_code(spec: ApiSpec) -> str:
    lines = []

    lines.append('# MODO DEMONSTRAÇÃO: sem chamadas HTTP reais')
    lines.append('BASE_URL = "{}"'.format(spec.base_url or ""))
    lines.append("")

    all_funcs = []

    for scen in spec.scenarios:
        scen_slug = slugify(scen.name)

        for case in scen.cases:
            case_slug = slugify(case.name)
            func_name = f"test_{scen_slug}_{case_slug}"
            all_funcs.append(func_name)

            path = case.request.get("path") or "/"
            query = case.request.get("query") or {}

            status = case.expect.get("status")
            json_has = case.expect.get("json_has") or []
            json_eq = case.expect.get("json_eq") or {}

            lines.append("")
            lines.append(f"def {func_name}():")
            lines.append(f'    print("Rodando {func_name}...")')
            lines.append(f'    url = BASE_URL + "{path}"')
            lines.append(f"    params = {repr(query)}")
            lines.append('    print("URL simulada:", url)')
            lines.append('    print("Parâmetros simulados:", params)')

            lines.append(f"    resp_status = {status if status is not None else 200}")
            lines.append("    data = {}  # aqui poderia vir um JSON real")
            lines.append('    print("Status code simulado:", resp_status)')
            lines.append('    print("JSON simulado:", data)')

            if status is not None:
                lines.append(f"    assert resp_status == {status}")

            for field in json_has:
                lines.append(f'    print("Campo esperado presente (json_has): {field}")')

            for field, value in json_eq.items():
                lines.append(f'    print("Expectativa json_eq: {field} == {value!r}")')

    lines.append("")
    lines.append("")
    lines.append("if __name__ == '__main__':")
    if not all_funcs:
        lines.append("    print('Nenhum teste definido na especificação.')")
    else:
        for fn in all_funcs:
            lines.append(f"    {fn}()")
        lines.append("    print('Todos os testes (modo demo) executados.')")

    return '\n'.join(lines)
