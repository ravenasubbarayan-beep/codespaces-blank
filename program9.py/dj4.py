posts = []

def create_post():
    title = input("Enter title: ")
    content = input("Enter content: ")

    posts.append({
        "title": title,
        "content": content,
        "comments": []
    })

    print("Post created successfully!")


def edit_post():
    title = input("Enter title: ")

    for p in posts:
        if p["title"] == title:
            p["content"] = input("Enter new content: ")
            print("Post edited!")
            return

    print("Post not found.")


def show_posts():
    for p in posts:
        print("\nTITLE:", p["title"])
        print("CONTENT:", p["content"])
        print("COMMENTS:", p["comments"])


def add_comment():
    title = input("Enter post title: ")

    for p in posts:
        if p["title"] == title:
            p["comments"].append(input("Enter comment: "))
            print("Comment added!")
            return

    print("Post not found.")


def admin_moderation():
    password = input("Enter admin password: ")

    if password != "admin123":
        print("Access denied!")
        return

    title = input("Enter post title: ")

    for p in posts:
        if p["title"] == title:
            print("Comments:", p["comments"])
            c = input("Enter comment to remove: ")

            if c in p["comments"]:
                p["comments"].remove(c)
                print("Comment deleted by admin.")
            else:
                print("Comment not found.")
            return

    print("Post not found.")


while True:
    print("\n===== BLOG MANAGEMENT =====")
    print("1. Create")
    print("2. Edit")
    print("3. View")
    print("4. Comment")
    print("5. Admin")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_post()
    elif choice == "2":
        edit_post()
    elif choice == "3":
        show_posts()
    elif choice == "4":
        add_comment()
    elif choice == "5":
        admin_moderation()
    elif choice == "6":
        print("Goodbye!")
        break