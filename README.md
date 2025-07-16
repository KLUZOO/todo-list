# ✅ Todo List Web Application

A simple Django-based web application to manage tasks using tags.  
Users can add, update, delete, and mark tasks as done/undone. Tasks can also be grouped using tags.

---

## 🏗️ Features

- 📋 View all tasks on the home page.
- ✅ Mark tasks as complete or undo completion.
- 🕒 Tasks are sorted:
  - First by completion status (`not done` → `done`)
  - Then by creation date (`newest → oldest`)
- 🏷️ Assign one or more tags to each task.
- 🗂️ View, add, update, and delete tags.
- 🧭 Persistent sidebar navigation (on all pages).

---

## 🧩 Models

### `Task`
- `content`: What needs to be done (text)
- `created_at`: Datetime of creation (auto)
- `deadline`: Optional due date
- `is_done`: Boolean — done or not
- `tags`: Many-to-many relation with `Tag`

### `Tag`
- `name`: Tag name (string)
- A tag can be assigned to multiple tasks.

---

## 🖼️ User Interface Overview

### 🌐 Home Page (`127.0.0.1:8000/`)
- Displays all tasks with full info
- Tasks ordered from not done to done and from newest to oldest
- Buttons:
  - ➕ Add Task
  - ✏️ Edit
  - ❌ Delete
  - ✅ Complete / 🔄 Undo
- Sidebar:
  - Home
  - Tag List

### 🏷️ Tag List Page (`127.0.0.1:8000/tags/`)
- Table of all tags
- Buttons:
  - ➕ Add Tag
  - ✏️ Edit
  - ❌ Delete

---

## 🛠️ Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
