import requests as req


class Post:
    ENDPOINT = "https://api.npoint.io/311350e08e470a8ea23e"

    def __init__(self):
        pass

    def get_allposts(self):
        res = req.get(url=self.ENDPOINT)
        res.raise_for_status()
        all_posts = res.json()
        return all_posts

    def get_post_with_id(self, id_):
        posts = self.get_allposts()
        for post in posts:
            if post['id'] == id_:
                return post

    def add_post(self, id_: int, title: str, subtitle: str, body: str):
        blog = {
            "id": id_,
            "title": title,
            "subtitle": subtitle,
            "body": body,
        }
        res = req.post(url=self.ENDPOINT,data=blog)
        return res.status_code


if __name__ == "__main__":
    mp = Post()
    print(mp.get_allposts())
    print(mp.add_post(id_=4,title="title",body ="body",subtitle="subtitle"))


