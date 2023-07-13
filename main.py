# Создайте макроопределение для отображения списка пользователей в HTML-документе.
# У вас есть список пользователей в переменной users, каждый пользователь представлен в виде словаря с ключами name и email. Используйте цикл for и условие if для отображения пользователей, у которых почта кончается на gmail.com

# from jinja2 import Environment, FileSystemLoader
#
#
# file_loader = FileSystemLoader('templates')
#
# env = Environment(loader=file_loader)
#
# tm = env.get_template('main.html')
#
# persons = [
#     {'name': 'Маша', 'email': '111@mail.ru'},
#     {'name': 'Саша', 'email': 'abc@gmail.com'},
#     {'name': 'Даша', 'email': 'a1@ya.ru'},
#     {'name': 'Паша', 'email': 'b2@gmail.com'},
# ]
#
# msg = tm.render(users=persons)
# print(msg)



### 2. Создайте макроопределение для отображения списка продуктов в HTML-документе. У вас есть список продуктов в переменной products, каждый продукт представлен в виде словаря с ключами name и price. Используйте цикл for и условие elif для отображения цены в зависимости от диапазона:
# Если цена меньше 10, то пишем, что продукт доступный
# Если цена меньше 20, то пишем, что продукт имеет среднюю цену
# И если цена больше, то пишем, что продукт дорогой

# from jinja2 import Template
#
#
# products = [
#     {'name': 'картошка', 'price': 8},
#     {'name': 'морковь', 'price': 25},
#     {'name': 'капуста', 'price': 12},
#     {'name': 'огурцы', 'price': 30},
#     {'name': 'редис', 'price': 5}
# ]
#
# html = '''
# {% macro list_users(users) %}
# <ul>
#     {% for u in users -%}
#         {% if u.price <= 10 -%}
#         <li>{{ u.name }}  доступный продукт</li>
#         {% elif u.price <= 20 and u.price > 10 -%}
#         <li>{{ u.name }}  продукт имеет среднюю цену</li>
#         {% else -%}
#         <li>{{ u.name }}  дорогой продукт</li>
#         {% endif -%}
#     {% endfor -%}
# </ul>
# {% endmacro %}
#
# {{ list_users(users) }}
# '''
#
# tm = Template(html)
# msg = tm.render(users=products)
# print(msg)