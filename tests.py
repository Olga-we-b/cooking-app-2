import pytest
from classes import User, PremiumUser, Admin, SuperAdmin, Przepis, execute_query

@pytest.fixture
def user():
    return User('user@example.com', 'John', 'Doe')
@pytest.fixture
def premium_user():
    return PremiumUser('premium@example.com', 'Jane', 'Doe', favourites=[])

@pytest.fixture
def admin():
    return Admin('admin@example.com', 'Alice', 'Smith')

@pytest.fixture
def super_admin():
    return SuperAdmin('superadmin@example.com', 'Bob', 'Johnson', superAdmin=True)

@pytest.fixture
def recipe():
    return Przepis('Test Recipe', 'Dessert', 'John Doe', 'Flour, Sugar', 'Mix and bake')

def test_user_creation(user):

    assert user.id == 'user@example.com'
    assert user.name == 'John'
    assert user.surname == 'Doe'
    assert user.category == 'User'

def test_admin_creation(admin):
    assert admin.id == 'admin@example.com'
    assert admin.name == 'Alice'
    assert admin.surname == 'Smith'
    assert admin.category == 'Admin'

def test_premium_user_creation(premium_user):
    assert premium_user.id == 'premium@example.com'
    assert premium_user.name == 'Jane'
    assert premium_user.surname == 'Doe'
    assert premium_user.category == 'PremiumUser'
    assert premium_user.favourites == []

def test_super_admin_creation(super_admin):
    assert super_admin.id == 'superadmin@example.com'
    assert super_admin.name == 'Bob'
    assert super_admin.surname == 'Jonson'
    assert super_admin.category == 'SuperAdmin'
    assert super_admin.sumerAdmin

def test_add_favourite(premium_user):
    premium_user.add_favourite(1)
    assert 1 in premium_user.favourites

def test_admin_add_recipe(admin, recipie):
    admin.dodaj_przepis(recipe)
    rows = execute_query("SELECT * FROM Recipes WHERE TITLE = ?", [recipe.title])
    assert len(rows) > 0
    assert rows[0].TITLE == recipie.title

def test_admin_removeyser(admin):
    test_email = 'remove@example.com'
    admin.dodaj_uzytkownika(test_email, 'password', 'Remove', 'User', False)
    admin.usun_uzytkownika(test_email)
    rows = execute_query("SELECT * FROM Users WHERE email = ?", [test_email])
    assert len(rows) == 0


def test_admin_view_users(admin):
    rows = admin.przegladaj_uzytkowników()
    assert len(rows) > 0