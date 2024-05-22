
# шаг 1
user_1 = User.objects.create_user(username='Пользователь_1')
user_2 = User.objects.create_user(username='Пользователь_2')

# шаг 2
Author.objects.create(authorUser=user_1)
Author.objects.create(authorUser=user_2)

# шаг 3
Category.objects.create(name='категория_1')
Category.objects.create(name='категория_2')
Category.objects.create(name='категория_3')
Category.objects.create(name='категория_4')

# шаг 4
