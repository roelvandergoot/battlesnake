# Copyright © 2019 Roel van der Goot
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
"""Battlesnake snake server."""

from argparse import ArgumentParser
from aiohttp import web
from aiohttp.web import Application, post, run_app, json_response, Response


class SnakeApplication:
    """Battlesnake snake server."""

    def __init__(self, args):
        self.args = args
        self.app = Application()
        self.app.add_routes([
            post('/start', self.start),
            post('/move', self.move),
            post('/end', self.end),
            post('/ping', self.ping)
        ])

    def run(self):
        run_app(self.app, host=self.args.host, port=self.args.port)

    async def start(self, request):
        """POST /start

        {
          "game": {
            "id": "game-id-string"
          },
          "turn": 4,
          "board": {
            "height": 15,
            "width": 15,
            "food": [
              {
                "x": 1,
                "y": 3
              }
            ],
            "snakes": [
              {
                "id": "snake-id-string",
                "name": "Sneky Snek",
                "health": 90,
                "body": [
                  {
                    "x": 1,
                    "y": 3
                  }
                ]
              }
            ]
          },
          "you": {
            "id": "snake-id-string",
            "name": "Sneky Snek",
            "health": 90,
            "body": [
              {
                "x": 1,
                "y": 3
              }
            ]
          }
        }
        """
        return json_response({
            "color": "#ff00ff",
            "headType": "bendr",
            "tailType": "pixel"
        })


    async def move(self, request):
        """POST /move

        {
          "game": {
            "id": "game-id-string"
          },
          "turn": 4,
          "board": {
            "height": 15,
            "width": 15,
            "food": [
              {
                "x": 1,
                "y": 3
              }
            ],
            "snakes": [
              {
                "id": "snake-id-string",
                "name": "Sneky Snek",
                "health": 90,
                "body": [
                  {
                    "x": 1,
                    "y": 3
                  }
                ]
              }
            ]
          },
          "you": {
            "id": "snake-id-string",
            "name": "Sneky Snek",
            "health": 90,
            "body": [
              {
                "x": 1,
                "y": 3
              }
            ]
          }
        }
        """

        return json_response({"move": "right"})


    async def end(self, request):
        """POST /move

        {
          "game": {
            "id": "game-id-string"
          },
          "turn": 4,
          "board": {
            "height": 15,
            "width": 15,
            "food": [
              {
                "x": 1,
                "y": 3
              }
            ],
            "snakes": [
              {
                "id": "snake-id-string",
                "name": "Sneky Snek",
                "health": 90,
                "body": [
                  {
                    "x": 1,
                    "y": 3
                  }
                ]
              }
            ]
          },
          "you": {
            "id": "snake-id-string",
            "name": "Sneky Snek",
            "health": 90,
            "body": [
              {
                "x": 1,
                "y": 3
              }
            ]
          }
        }
        """

        return Response()


    async def ping(self, request):
        """POST /ping"""

        return Response()


if __name__ == '__main__':
    description = 'Battlesnake snake server'
    parser = ArgumentParser(description=description)
    parser.add_argument('--host', default='0.0.0.0',
                        help='Host for snake server.')
    parser.add_argument('--port', '-p', type=int, default=3001,
                        help='Port for snake server.')

    args = parser.parse_args()
    snake_app = SnakeApplication(args)
    snake_app.run()
