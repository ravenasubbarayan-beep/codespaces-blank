posts = []
next_id = 101


def create_post():
    global next_id

    title = input("Enter title: ")
    content = input("Enter content: ")

    posts.append({
        "id": next_id,
        "title": title,
        "content": content,
        "comments": []
    })

    print("Post ID:", next_id)
    print("Post created!")
    next_id += 1


def edit_post():
    pid = int(input("Enter post ID: "))

    for p in posts:
        if p["id"] == pid:
            p["title"] = input("Enter new title: ")
            p["content"] = input("Enter new content: ")
            print("Post updated!")
            return

    print("Post not found.")


def delete_post():
    pid = int(input("Enter post ID to delete: "))

    for p in posts:
        if p["id"] == pid:
            posts.remove(p)
            print("Post deleted!")
            return

    print("Post not found.")


def view_posts():
    if not posts:
        print("No posts available.")
        return

    for p in posts:
        print("\nID:", p["id"])
        print("Title:", p["title"])
        print("Content:", p["content"])
        print("Comments:", p["comments"])


def add_comment():
    pid = int(input("Enter post ID: "))

    for p in posts:
        if p["id"] == pid:
            comment = input("Enter comment: ")
            p["comments"].append(comment)
            print("Comment added!")
            return

    print("Post not found.")


def admin():
    pid = int(input("Enter post ID: "))

    for p in posts:
        if p["id"] == pid:
            print("Comments:", p["comments"])
            comment = input("Enter unwanted comment: ")

            if comment in p["comments"]:
                p["comments"].remove(comment)
                print("Comment moderated!")
            else:
                print("Comment not found.")
            return

    print("Post not found.")


while True:
    print("\n===== BLOG MANAGEMENT SYSTEM =====")
    print("1. Create Post")
    print("2. Edit Post")
    print("3. Delete Post")
    print("4. View Posts")
    print("5. Add Comment")
    print("6. Admin Moderation")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_post()
    elif choice == "2":
        edit_post()
    elif choice == "3":
        delete_post()
    elif choice == "4":
        view_posts()
    elif choice == "5":
        add_comment()
    elif choice == "6":
        admin()
    elif choice == "7":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")  