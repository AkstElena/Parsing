from lxml import etree


def print_tree(element, depth=0):
    """Рекурсивная печать древовидной структуры элемента HTML"""
    # Вывод текущего элемента с соответствующим отступом
    print("-" * depth + element.tag)

    # Рекурсивная печать дочерних элементов с увеличенным отступом
    for child in element.iterchildren():
        print_tree(child, depth + 1)


# Парсинг HTML-документа
tree = etree.parse("src/web_page.html")

# Получение корневого элемента дерева
root = tree.getroot()

# Вывод структуры дерева
print_tree(root)
