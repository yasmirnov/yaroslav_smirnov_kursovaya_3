import json
from dao.post import Post


class PostsDAO:
    def __init__(self, post_path, comment_path):
        self.post_path = post_path
        self.comment_path = comment_path

    def load_posts(self):
        """
        возвращает список экземпляров класса Post
        """
        with open(self.post_path, "r") as file:
            new_post = []
            posts_data = json.load(file)

            for post in posts_data:
                new_post.append(Post(
                    post["poster_name"],
                    post["poster_avatar"],
                    post["pic"],
                    post["content"],
                    post["views_count"],
                    post["likes_count"],
                    post["pk"]
                ))
        return new_post

    def load_posts_json(self):
        """
        загружает данные постов
        """
        with open(self.post_path, "r") as file:
            posts_data = json.load(file)
        return posts_data

    def load_comments(self):
        """
        загружает данные комментов
        """
        with open(self.comment_path, "r") as file:
            comments_data = json.load(file)
            return comments_data

    def get_all_posts(self):
        """
        возвращает список экземпляров класса Post
        """
        return self.load_posts()

    def get_posts_by_username(self, user_name):
        """
        возвращает список постов опред пользователя
        """
        posts = self.load_posts()
        user_posts = []
        for post in posts:
            if post.poster_name.lower() == user_name.lower():
                user_posts.append(post)
        return user_posts

    def get_comments_by_post_id(self, post_id):
        """
        возвращает список комментариев по id поста
        """
        comments = self.load_comments()
        post_comments = []
        for comment in comments:
            if comment["post_id"] == post_id:
                post_comments.append(comment)
        return post_comments

    def search_posts(self, substr):
        """
        возвращает список постов по запросу
        """
        posts = self.load_posts()
        new_posts = []
        for post in posts:
            if substr.lower() in post.content.lower():
                new_posts.append(post)
        return new_posts

    def get_post_by_pk(self, pk):
        """
        возвращает пост по pk
        """
        posts = self.load_posts()
        for post in posts:
            if post.pk == pk:
                return post
        return
