from django.db import migrations

INITIAL_TAGS = [
    {'color': '#FFA500', 'name': 'Завтрак', 'slug': 'breakfast'},
    {'color': '#00FFFF', 'name': 'Обед', 'slug': 'lunch'},
    {'color': '#BF40BF', 'name': 'Ужин', 'slug': 'dinner'},
]


def add_tags(apps, schema_editor):
    Tag = apps.get_model('recipes', 'Tag')
    for tag in INITIAL_TAGS:
        new_tag = Tag(**tag)
        new_tag.save()


def remove_tags(apps, schema_editor):
    Tag = apps.get_model('recipe', 'Tag')
    for tag in INITIAL_TAGS:
        Tag.objects.get(slug=tag['slug']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_add_ingredients'),
    ]

    operations = [
        migrations.RunPython(
            add_tags,
            remove_tags
        ),
    ]
