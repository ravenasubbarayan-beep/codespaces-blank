blogs = []

def add_blog():
    title = input("Enter blog title: ")
    text = input("Enter blog content: ")

    blogs.append({
        "title": title,
        "text": text,
        "comments": []
    })

    print("Blog added successfully!")


def update_blog():
    title = input("Enter blog title to edit: ")

    for blog in blogs:
        if blog["title"] == title:
            blog["text"] = input("Enter new content: ")
            print("Blog updated!")
            return

    print("Blog not found.")


def show_blogs():
    if len(blogs) == 0:
        print("No blogs available.")
        return

    for blog in blogs:
        print("\nTitle:", blog["title"])
        print("Content:", blog["text"])
        print("Comments:", blog["comments"])


def comment_blog():
    title = input("Enter blog title: ")

    for blog in blogs:
        if blog["title"] == title:
            c = input("Enter comment: ")
            blog["comments"].append(c)
            print("Comment added!")
            return

    print("Blog not found.")


def remove_comment():
    title = input("Enter blog title: ")

    for blog in blogs:
        if blog["title"] == title:
            print("Comments:", blog["comments"])
            c = input("Enter comment to delete: ")

            if c in blog["comments"]:
                blog["comments"].remove(c)
                print("Admin removed comment.")
            else:
                print("Comment not found.")
            return

    print("Blog not found.")


while True:
    print("\n1.Add Blog")
    print("2.Edit Blog")
    print("3.View Blogs")
    print("4.Comment")
    print("5.Moderate")
    print("6.Exit")

    ch = input("Choice: ")

    if ch == "1":
        add_blog()
    elif ch == "2":
        update_blog()
    elif ch == "3":
        show_blogs()
    elif ch == "4":
        comment_blog()
    elif ch == "5":
        remove_comment()
    elif ch == "6":
        break
    else:
        print("Invalid choice")