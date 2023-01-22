from flask import jsonify, Blueprint

from logs.logger import get_logger
from dao.dao import PostsDAO


api_blueprint = Blueprint('api_blueprint', __name__)
posts = PostsDAO('./data/posts.json', './data/comments.json')

logger = get_logger(__name__)


@api_blueprint.route('/api/posts/', methods=['GET'])
def get_all_posts():
    logger.info('Был запрос к api/posts')
    return jsonify(posts.load_posts_json())


@api_blueprint.route('/api/posts/<int:postid>', methods=['GET'])
def get_post_by_id(postid):
    logger.info('Был запрос к api/post')
    return jsonify(posts.get_post_by_pk_json(postid))
