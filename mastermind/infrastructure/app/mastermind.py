from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

from mastermind.infrastructure.context.context import Context
from mastermind.module.game.application.create_game_use_case import CreateGameCommand
from mastermind.module.game.domain.error.game_errors import GameError, GameAlreadyExists
from mastermind.module.shared.domain.validation.validation_exception import ValidationException


class GamesController(Resource):
    post_parser = reqparse.RequestParser() \
        .add_argument(
            "game_id",
            required=False,
            help="Assigned to the new game") \
        .add_argument(
            "first_code_peg",
            type=int,
            required=True,
            help="First peg of the code") \
        .add_argument(
            "second_code_peg",
            type=int,
            required=True,
            help="Second peg of the code")\
        .add_argument(
            "third_code_peg",
            type=int,
            required=True,
            help="Third peg of the code")\
        .add_argument(
            "fourth_code_peg",
            type=int,
            required=True,
            help="Fourth peg of the code")

    def __init__(self, context: Context):
        self.context = context

    def post(self):
        args = self.post_parser.parse_args()
        command = CreateGameCommand(args["game_id"], args["first_code_peg"], args["second_code_peg"], args["third_code_peg"], args["fourth_code_peg"])
        self.context.create_game_command_handler.handle(command)
        return {}, 201


"""
POST /games
- passing game_id and color_code

POST /games/{game-id}/guesses
- passing color_code
- return guess_result

GET /game/{game-id}/guesses
- return a list of color_codes and guess_results
"""


def validation_exception_handler(error: ValidationException):
    response = jsonify({"error": "validation error - {}".format(error.__str__())})
    response.status_code = 422
    return response


def game_error_handler(error: GameError):
    response = jsonify({"error": error.__str__()})
    if isinstance(error, GameAlreadyExists):
        response.status_code = 409
    else:
        response.status_code = 500
    return response


def create_app(app_context: Context) -> Flask:
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(GamesController, '/games', resource_class_kwargs={"context": app_context})
    app.register_error_handler(ValidationException, validation_exception_handler)
    app.register_error_handler(GameError, game_error_handler)

    return app


if __name__ == '__main__':
    context = Context()
    app = create_app(context)
    app.run(debug=True)
