import streamlit as st
from datetime import datetime


# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Jiya's Library Management System",
    page_icon="📚",
    layout="wide"
)

# ---------------- ANIMATED UI ----------------
st.markdown("""
<style>

body {
    background: linear-gradient(-45deg, #e8f5e9, #e3f2fd, #f3e5f5, #fff3e0);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Main title */
.title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    margin-top: 10px;
    animation: titleMove 2s ease-in-out infinite alternate;
}

@keyframes titleMove {
    from {transform: translateY(0px);}
    to {transform: translateY(-8px);}
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 20px;
    margin-bottom: 25px;
}

/* Floating books */
.book {
    position: fixed;
    font-size: 35px;
    animation: floatBook 8s linear infinite;
    z-index: 0;
}

.book1 {
    left: 5%;
    bottom: -50px;
    animation-delay: 0s;
}

.book2 {
    left: 25%;
    bottom: -50px;
    animation-delay: 2s;
}

.book3 {
    right: 20%;
    bottom: -50px;
    animation-delay: 4s;
}

.book4 {
    right: 5%;
    bottom: -50px;
    animation-delay: 6s;
}

@keyframes floatBook {
    0% {
        transform: translateY(0) rotate(0deg);
        opacity: 0;
    }

    20% {
        opacity: 1;
    }

    80% {
        opacity: 1;
    }

    100% {
        transform: translateY(-100vh) rotate(360deg);
        opacity: 0;
    }
}

/* Cards */
.card {
    background: rgba(255, 255, 255, 0.80);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    color: #7b1e3a;
    box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.12);
    margin: 10px;
    transition: 0.3s;
}

.card h1,
.card h2,
.card p {
    color: #7b1e3a;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 15px 30px rgba(0,0,0,0.18);
}

/* Section headings */
.section-title {
    font-size: 30px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 15px;
}

/* Buttons */
.stButton > button {
    border-radius: 12px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.05);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #e3f2fd, #f3e5f5);
}

/* Sidebar Text & Labels changed to Rose color */
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] .stMarkdown {
        color: #FF007F !important;  /* Classic Rose Pink */
    }
    </style>
    """,
    unsafe_allow_html=True
)



# ---------------- FILE FUNCTIONS ----------------

def read_book():
    try:
        with open("books_data.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def read_user():
    try:
        with open("users_data.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


# ---------------- HOME ----------------

def home():

    st.markdown(
        '<div class="title">📚 Library Management System</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">✨ Manage your library in a simple and interactive way ✨</div>',
        unsafe_allow_html=True
    )

    books = read_book()
    users = read_user()

    book_count = 0
    user_count = 0

    for line in books:
        if line.strip():
            book_count += 1

    for line in users:
        if line.strip():
            user_count += 1

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="card">
                <h1>📚</h1>
                <h2>{book_count}</h2>
                <p>Total Books</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="card">
                <h1>👩‍🎓</h1>
                <h2>{user_count}</h2>
                <p>Registered Users</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="card">
                <h1>✨</h1>
                <h2>Ready</h2>
                <p>Library Status</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.markdown(
        '<div class="section-title">🌟 Welcome to Your Library</div>',
        unsafe_allow_html=True
    )

    st.info(
        "Use the menu on the left to add books, view books, "
        "search books, register users and issue books."
    )


# ---------------- ADD BOOK ----------------

def add_book():

    st.markdown(
        '<div class="section-title">📕 Add New Book</div>',
        unsafe_allow_html=True
    )

    book_name = st.text_input("📖 Enter Book Name")
    book_author = st.text_input("✍️ Enter Book Author")
    book_quantity = st.number_input(
        "🔢 Enter Book Quantity",
        min_value=1,
        step=1
    )

    if st.button("➕ Add Book"):

        if not book_name.strip():
            st.error("Please enter Book Name.")

        elif not book_author.strip():
            st.error("Please enter Book Author.")

        else:

            book_name = book_name.strip().title()
            book_author = book_author.strip().title()

            # Check duplicate book
            name_exists = False

            for line in read_book():

                parts = line.strip().split(",")

                if len(parts) >= 2:

                    existing_book_name = parts[1].strip()

                    if existing_book_name.lower() == book_name.lower():
                        name_exists = True
                        break

            if name_exists:

                st.error(
                    "❌ Book Name already exists! "
                    "Please enter a different Book Name."
                )

            else:

                last_id = 0

                for line in read_book():

                    parts = line.strip().split(",")

                    if len(parts) >= 1:

                        if parts[0].strip().startswith("B"):

                            try:
                                number = int(parts[0].strip()[1:])

                                if number > last_id:
                                    last_id = number

                            except ValueError:
                                pass

                book_id = f"B{last_id + 1:03d}"

                with open("books_data.txt", "a") as file:

                    file.write(
                        f"{book_id} , {book_name} , "
                        f"{book_author} , {int(book_quantity)}\n"
                    )

                st.success(
                    f"🎉 Book Added Successfully! Book ID: {book_id}"
                )

                st.balloons()


# ---------------- VIEW BOOKS ----------------

def view_books():

    st.markdown(
        '<div class="section-title">📚 Available Books</div>',
        unsafe_allow_html=True
    )

    books = []

    for line in read_book():

        parts = line.strip().split(",")

        if len(parts) >= 4:

            books.append({
                "Book ID": parts[0].strip(),
                "Book Name": parts[1].strip(),
                "Author": parts[2].strip(),
                "Quantity": parts[3].strip()
            })

    if not books:

        st.warning("📭 No books available in the library.")

    else:

        st.dataframe(
            books,
            use_container_width=True,
            hide_index=True
        )


# ---------------- SEARCH BOOK ----------------

def search_book():

    st.markdown(
        '<div class="section-title">🔍 Search Book</div>',
        unsafe_allow_html=True
    )

    search = st.text_input(
        "Enter Book Name or Book ID"
    )

    if st.button("🔎 Search"):

        found = False

        for line in read_book():

            parts = line.strip().split(",")

            if len(parts) >= 4:

                book_id = parts[0].strip()
                book_name = parts[1].strip()
                book_author = parts[2].strip()
                book_quantity = parts[3].strip()

                if (
                    search.strip().lower() == book_name.lower()
                    or
                    search.strip().lower() == book_id.lower()
                ):

                    st.success("📖 Book Found!")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.write("*Book ID:*", book_id)
                        st.write("*Book Name:*", book_name)

                    with col2:
                        st.write("*Author:*", book_author)
                        st.write("*Available Quantity:*", book_quantity)

                    found = True
                    break

        if not found:

            st.error("❌ Book not found in the library.")


# ---------------- REGISTER USER ----------------

def register_user():

    st.markdown(
        '<div class="section-title">👩‍🎓 Register User</div>',
        unsafe_allow_html=True
    )

    user_name = st.text_input("👤 Enter User Name")
    mobile_no = st.text_input("📱 Enter Mobile Number")

    if st.button("📝 Register User"):

        if not user_name.strip():

            st.error("Please enter User Name.")

        else:

            mobile = mobile_no.replace(" ", "")

            if (
                not mobile.isdigit()
                or len(mobile) != 10
                or mobile[0] not in "6789"
            ):

                st.error(
                    "❌ Invalid Mobile Number! "
                    "Enter a valid 10-digit number."
                )

            else:

                last_id = 0

                for line in read_user():

                    parts = line.strip().split(",")

                    if len(parts) >= 1:

                        if parts[0].strip().startswith("U"):

                            try:

                                number = int(
                                    parts[0].strip()[1:]
                                )

                                if number > last_id:
                                    last_id = number

                            except ValueError:
                                pass

                user_id = f"U{last_id + 1:03d}"

                user_name = user_name.strip().title()

                with open("users_data.txt", "a") as file:

                    file.write(
                        f"{user_id} , {user_name} , {mobile}\n"
                    )

                st.success(
                    f"🎉 User Registered Successfully! "
                    f"User ID: {user_id}"
                )

                st.balloons()


# ---------------- ISSUE BOOK ----------------

def issue_book():

    st.markdown(
        '<div class="section-title">📤 Issue Book</div>',
        unsafe_allow_html=True
    )

    user_id = st.text_input("👤 Enter User ID")

    book_input = st.text_input(
        "📚 Enter Book ID or Book Name"
    )

    quantity = st.number_input(
        "🔢 Enter Quantity",
        min_value=1,
        step=1
    )

    if st.button("📤 Issue Book"):

        # Check user
        user_found = False

        for line in read_user():

            parts = line.strip().split(",")

            if len(parts) >= 1:

                if parts[0].strip().lower() == user_id.strip().lower():

                    user_found = True
                    break

        if not user_found:

            st.error("❌ User does not exist.")

        else:

            book_found = False
            book_id = ""
            book_name = ""
            book_quantity = 0

            # Find book
            for line in read_book():

                parts = line.strip().split(",")

                if len(parts) >= 4:

                    if (
                        parts[0].strip().lower()
                        == book_input.strip().lower()
                        or
                        parts[1].strip().lower()
                        == book_input.strip().lower()
                    ):

                        book_found = True

                        book_id = parts[0].strip()
                        book_name = parts[1].strip()
                        book_quantity = int(
                            parts[3].strip()
                        )

                        break

            if not book_found:

                st.error("❌ Book does not exist.")

            elif book_quantity <= 0:

                st.error(
                    "❌ This book is currently unavailable."
                )

            elif quantity > book_quantity:

                st.error(
                    "❌ Not enough books available!"
                )

            else:

                new_quantity = (
                    book_quantity - int(quantity)
                )

                lines = read_book()

                with open(
                    "books_data.txt",
                    "w"
                ) as file:

                    for line in lines:

                        parts = line.strip().split(",")

                        if len(parts) >= 4:

                            if parts[0].strip() == book_id:

                                parts[3] = str(
                                    new_quantity
                                )

                        file.write(
                            ",".join(parts) + "\n"
                        )

                issue_date = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

                st.success(
                    "🎉 Book Issued Successfully!"
                )

                st.info(
                    f"""
                    📚 *Book:* {book_name}

                    🔢 *Quantity:* {int(quantity)}

                    👤 *User ID:* {user_id}

                    📅 *Issue Date:* {issue_date}
                    """
                )

                st.balloons()


# ---------------- SIDEBAR ----------------

st.sidebar.title("📚 Library Menu")

choice = st.sidebar.radio(
    "Choose an option:",
    [
        "🏠 Home",
        "➕ Add Book",
        "📚 View Books",
        "🔍 Search Book",
        "👩‍🎓 Register User",
        "📤 Issue Book"
    ]
)

# ---------------- PAGE ROUTING ----------------

if choice == "🏠 Home":

    home()

elif choice == "➕ Add Book":

    add_book()

elif choice == "📚 View Books":

    view_books()

elif choice == "🔍 Search Book":

    search_book()

elif choice == "👩‍🎓 Register User":

    register_user()

elif choice == "📤 Issue Book":

    issue_book()


# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;">
        📖✨ <b>Library Management System</b> ✨📖<br>
        <small>Manage • Search • Register • Issue</small>
    </div>
    """,
    unsafe_allow_html=True
)