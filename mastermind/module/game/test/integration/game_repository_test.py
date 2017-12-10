from mastermind.module.game.domain.game_repository import GameRepository
from mastermind.module.game.test.infrastructure.random.random_game import random_game
from mastermind.module.game.test.infrastructure.random.random_game_id import random_game_id
from mastermind.module.shared.test.infrastructure.context.context_aware_test_case import ContextAwareTestCase


class GameRepositoryTest(ContextAwareTestCase):
    def test_should_insert_game(self):
        game = random_game()
        self.game_repository.insert(game)

    def test_should_not_find_unexisting_game(self):
        self.assertIsNone(self.game_repository.search(random_game_id()))

    def test_should_find_existing_game(self):
        game = random_game()
        self.game_repository.insert(game)
        self.assertEqual(
            self.game_repository.search(game.game_id),
            game
        )

    @property
    def game_repository(self) -> GameRepository:
        return self.context.game_repository
