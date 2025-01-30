import pytest

from parallel_change.solution.src import field, method


class TestAuthenticator:

    def test_administrator_role_is_always_authenticated(self):
        service = method.AuthenticationService()

        user_role, user_id = "admin", 12345

        assert service.is_authenticated_with_role(user_role, user_id)

    def test_normal_user_role_is_not_authenticated(self):
        service = method.AuthenticationService()

        user_role, user_id = "user", 11111

        assert service.is_authenticated_with_role(user_role, user_id) == False


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

    def test_has_discount_when_cart_has_at_least_one_premium_item(self, shopping_cart):
        shopping_cart.add(200)
        shopping_cart.add(10)

        assert shopping_cart.has_discount() == True

    def test_discount_is_not_applied_if_sum_of_items_is_greater_than_100(self, shopping_cart):
        shopping_cart.add(50)
        shopping_cart.add(50)

        assert shopping_cart.has_discount() == False