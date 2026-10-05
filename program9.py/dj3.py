import json

filename = "blog.json"

try:
    with open(filename, "r") as file:
        posts = json.load(file)
except:
    posts = []


def save_data():
    with open(filename, "w") as file:
        json.dump(posts, file, indent=4)


def create():
    title = input("Enter title: ")
    content = input("Enter content: ")

    post = {
        "title": title,
        "content": content,
        "comments": []
    }

    posts.append(post)
    save_data()

    print("Post saved successfully!")


def edit():
    title = input("Enter title to edit: ")

    for post in posts:
        if post["title"] == title:
            post["content"] = input("Enter new content: ")
            save_data()
            print("Post updated!")
            return

    print("Post not found.")


def display():
    for post in posts:
        print("\nTitle:", post["title"])
        print("Content:", post["content"])
        print("Comments:", post["comments"])


def comment():
    title = input("Enter post title: ")

    for post in posts:
        if post["title"] == title:
            c = input("Enter comment: ")
            post["comments"].append(c)
            save_data()
            print("Comment added!")
            return

    print("Post not found.")


def moderate():
    title = input("Enter post title: ")

    for post in posts:
        if post["title"] == title:
            print(post["comments"])
            c = input("Enter comment to remove: ")

            if c in post["comments"]:
                post["comments"].remove(c)
                save_data()
                print("Comment removed!")
            else:
                print("Comment not found.")
            return


while True:
    print("\n===== BLOG MENU =====")
    print("1.Create")
    print("2.Edit")
    print("3.View")
    print("4.Comment")
    print("5.Moderate")
    print("6.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create()
    elif choice == "2":
        edit()
    elif choice == "3":
        display()
    elif choice == "4":
        comment()
    elif choice == "5":
        moderate()
    elif choice == "6":
        break