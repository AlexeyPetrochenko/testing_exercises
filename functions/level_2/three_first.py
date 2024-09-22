NOT_SET = "NOT_SET"

# Тут не понял, это просто забыли добавить в аннотацию return возможный тип str, или специально ведь в аннотации к default можно передавать строки?
def first(items: list[int], default: int | None | str = NOT_SET) -> int | None:
    if items:
        return items[0]
    if default == NOT_SET:
        raise AttributeError
    return default
