from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from list_realms.models import TodoList, TodoItem

from list_realms.service.create_list import (
    create_todo_list,
    add_item,
)

from list_realms.service.delete_list import (
    delete_item,
    delet_list,
)

from list_realms.service.marca import (
    toggle_item,
)

from list_realms.service.search_progress import (
    get_list_items,
    get_list_statistics,
)

from list_realms.service.today import (
    get_today_tasks,
)


class TodoServiceTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="kau",
            password="123456"
        )

        self.todo_list = create_todo_list(
            user=self.user,
            title="Estudos",
            color="#ffffff"
        )

    # =====================================
    # CREATE LIST
    # =====================================

    def test_create_todo_list(self):

        self.assertEqual(
            TodoList.objects.count(),
            1
        )

        self.assertEqual(
            self.todo_list.title,
            "Estudos"
        )

        self.assertEqual(
            self.todo_list.user,
            self.user
        )

    def test_create_list_without_title(self):

        with self.assertRaises(ValueError):

            create_todo_list(
                user=self.user,
                title=""
            )

    # =====================================
    # ADD ITEM
    # =====================================

    def test_add_item(self):

        item = add_item(
            todo_list=self.todo_list,
            title="Aprender Django",
            category="study",
            xp_reward=50
        )

        self.assertEqual(
            TodoItem.objects.count(),
            1
        )

        self.assertEqual(
            item.title,
            "Aprender Django"
        )

        self.assertEqual(
            item.category,
            "study"
        )

    def test_add_item_without_title(self):

        with self.assertRaises(ValueError):

            add_item(
                todo_list=self.todo_list,
                title=""
            )

    # =====================================
    # DELETE ITEM
    # =====================================

    def test_delete_item(self):

        item = add_item(
            todo_list=self.todo_list,
            title="Excluir"
        )

        delete_item(item.id)

        self.assertFalse(
            TodoItem.objects.filter(
                id=item.id
            ).exists()
        )

    # =====================================
    # DELETE LIST
    # =====================================

    def test_delete_list(self):

        delet_list(self.todo_list)

        self.assertFalse(
            TodoList.objects.filter(
                id=self.todo_list.id
            ).exists()
        )

    # =====================================
    # TOGGLE ITEM
    # =====================================

    def test_toggle_item_complete(self):

        item = add_item(
            todo_list=self.todo_list,
            title="Concluir tarefa"
        )

        toggle_item(item.id)

        item.refresh_from_db()

        self.assertTrue(item.is_done)
        self.assertIsNotNone(item.completed_at)

    def test_toggle_item_uncomplete(self):

        item = add_item(
            todo_list=self.todo_list,
            title="Concluir tarefa"
        )

        toggle_item(item.id)
        toggle_item(item.id)

        item.refresh_from_db()

        self.assertFalse(item.is_done)
        self.assertIsNone(item.completed_at)

    # =====================================
    # GET ITEMS
    # =====================================

    def test_get_list_items(self):

        add_item(
            todo_list=self.todo_list,
            title="Item 1"
        )

        add_item(
            todo_list=self.todo_list,
            title="Item 2"
        )

        items = get_list_items(
            self.todo_list
        )

        self.assertEqual(
            items.count(),
            2
        )

    # =====================================
    # STATISTICS
    # =====================================

    def test_get_list_statistics(self):

        item1 = add_item(
            todo_list=self.todo_list,
            title="Item 1"
        )

        add_item(
            todo_list=self.todo_list,
            title="Item 2"
        )

        toggle_item(item1.id)

        stats = get_list_statistics(
            self.todo_list
        )

        self.assertEqual(
            stats["total"],
            2
        )

        self.assertEqual(
            stats["concluidas"],
            1
        )

        self.assertEqual(
            stats["pendentes"],
            1
        )

        self.assertEqual(
            stats["percentual"],
            50.0
        )

    # =====================================
    # TODAY TASKS
    # =====================================

    def test_get_today_tasks(self):

        today = timezone.now().date()

        add_item(
            todo_list=self.todo_list,
            title="Hoje",
            task_date=today
        )

        add_item(
            todo_list=self.todo_list,
            title="Amanhã",
            task_date=today + timezone.timedelta(days=1)
        )

        tasks = get_today_tasks(
            self.user
        )

        self.assertEqual(
            tasks.count(),
            1
        )

        self.assertEqual(
            tasks.first().title,
            "Hoje"
        )