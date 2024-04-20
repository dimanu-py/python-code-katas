import pytest

from parallel_change.src import method, field


class TestAuthenticator:

    def test_administrator_is_always_authenticated(self):
        service = method.AuthenticationService()
        admin_id = 12345
        assert service.is_authenticated(admin_id) == True

    def test_normal_user_is_not_authenticated_initially(self):
        service = method.AuthenticationService()
        normal_user_id = 11111
        assert service.is_authenticated(normal_user_id) == False


class TestShoppingCart:

    @pytest.fixture
    def shopping_cart(self):
        return field.ShoppingCart()

    def test_cart_may_just_have_a_single_item(self, shopping_cart):
        shopping_cart.add(10)
        assert shopping_cart.number_of_products() == 1

    def test_the_total_price_of_the_cart_is_total_of_its_contents(self, shopping_cart):
        shopping_cart.add(10)
        assert shopping_cart.calculate_total_price() == 10

    def test_has_discount_when_contains_at_least_one_premium_item(self, shopping_cart):
        shopping_cart.add(100)
        assert shopping_cart.has_discount() == True

    def test_doesnt_have_discount_when_all_its_items_are_cheap(self, shopping_cart):
        shopping_cart.add(10)
        assert shopping_cart.has_discount() == False

    def test_cart_can_have_multiple_items(self, shopping_cart):
        shopping_cart.add(10)
        shopping_cart.add(20)

        assert shopping_cart.number_of_products() == 2

    def test_total_price_of_the_cart_is_total_of_items_price(self, shopping_cart):
        shopping_cart.add(10)
        shopping_cart.add(20)

        assert shopping_cart.calculate_total_price() == 30