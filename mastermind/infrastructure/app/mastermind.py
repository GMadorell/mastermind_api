from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


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

    def post(self):
        args = self.post_parser.parse_args()
        return args


"""
POST /games
- passing game_id and color_code

POST /games/{game-id}/guesses
- passing color_code
- return guess_result

GET /game/{game-id}/guesses
- return a list of color_codes and guess_results
"""

api.add_resource(GamesController, '/games')

if __name__ == '__main__':
    app.run(debug=True)
