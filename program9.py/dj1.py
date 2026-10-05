class Blog:
    def __init__(self):
        self.posts = []
        self.post_id = 1

    def create_post(self):
        title = input("Enter title: ")
        content = input("Enter content: ")

        self.posts.append({
            "id": self.post_id,
            "title": title,
            "content": content,
            "comments": []
        })

        print("Post created!")
        self.post_id += 1

    def edit_post(self):
        pid = int(input("Enter post ID: "))

        for post in self.posts:
            if post["id"] == pid:
                post["title"] = input("New title: ")
                post["content"] = input("New content: ")
                print("Post edited!")
                return

        print("Post not found.")

    def view_posts(self):
        for post in self.posts:
            print("\nID:", post["id"])
            print("Title:", post["title"])
            print("Content:", post["content"])
            print("Comments:", post["comments"])

    def add_comment(self):
        pid = int(input("Enter post ID: "))

        for post in self.posts:
            if post["id"] == pid:
                comment = input("Enter comment: ")
                post["comments"].append(comment)
                print("Comment added!")
                return

        print("Post not found.")

    def moderate(self):
        pid = int(input("Enter post ID: "))

        for post in self.posts:
            if post["id"] == pid:
                print("Comments:", post["comments"])
                comment = input("Comment to remove: ")

                if comment in post["comments"]:
                    post["comments"].remove(comment)
                    print("Comment removed!")
                else:
                    print("Comment not found.")
                return

        print("Post not found.")


blog = Blog()

while True:
    print("\n===== BLOG SYSTEM =====")
    print("1. Create Post")
    print("2. Edit Post")
    print("3. View Posts")
    print("4. Add Comment")
    print("5. Admin Moderation")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        blog.create_post()
    elif choice == "2":
        blog.edit_post()
    elif choice == "3":
        blog.view_posts()
    elif choice == "4":
        blog.add_comment()
    elif choice == "5":
        blog.moderate()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")