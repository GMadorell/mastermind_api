from itertools import chain

from mastermind.module.game.test.infrastructure.random.random_game_id\
    import random_game_id
from mastermind.module.guess.domain.guess_repository import GuessRepository
from mastermind.module.guess.test.infrastructure.random.random_guess\
    import random_guess
from mastermind.module.shared.test.infrastructure.context\
    .context_aware_test_case import ContextAwareTestCase


class GuessRepositoryTest(ContextAwareTestCase):
    def test_should_insert_guess(self):
        guess = random_guess()
        self.guess_repository.insert(guess)

    def test_should_search_guess(self):
        guess = random_guess()
        self.guess_repository.insert(guess)
        self.assertEqual(
            guess,
            self.guess_repository.search(guess.guess_id)
        )

    def test_should_search_guesses_by_game_id(self):
        game_id = random_game_id()
        guesses_of_game = [random_guess(game_id=game_id) for _ in range(5)]
        guesses_not_of_game = [random_guess() for _ in range(5)]

        for guess in chain(guesses_of_game, guesses_not_of_game):
            self.guess_repository.insert(guess)

        found = self.guess_repository.search_by_game_id(game_id)
        self.assertEqual(len(found), len(guesses_of_game))
        for guess in guesses_of_game:
            self.assertIn(guess, found)
        for guess in guesses_not_of_game:
            self.assertNotIn(guess, found)

    @property
    def guess_repository(self) -> GuessRepository:
        return self.context.guess_repository
